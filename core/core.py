# core/core.py

import mysql.connector
import os
import sys
import pandas as pd
from dotenv import load_dotenv
from core.utils import calculate_wpm, calculate_accuracy
from core.constants import paragraphs

if getattr(sys, "frozen", False):
    env_path = os.path.join(os.path.dirname(sys.executable), ".env")
else: 
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")

if os.path.exists(env_path):
    load_dotenv(env_path)
else:
    print(".env file not found at", env_path)


def run_sql_file(filename):
    con = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASS", "")
    )

    with open(filename, 'r') as f:
       sql_script = f.read()
        
    with con.cursor() as cur:
        cur.execute("CREATE DATABASE IF NOT EXISTS typerush_db;")
        con.database = "typerush_db"
        cur.execute(sql_script)
    
    con.commit()        

    print(f"Executed {filename} successfully!")

def initialize_database():
    run_sql_file("databases/paragraphs.sql")
    run_sql_file("databases/paragraphs_data.sql")
    run_sql_file("databases/results.sql")


def get_paragraphs_from_db():
    try:
        con = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASS", ""),
            database="typerush_db"
        )
        try:
            cur = con.cursor()
            cur.execute("SELECT text FROM typing_paragraphs")
            rows = cur.fetchall()
            if rows:
                return [row[0] for row in rows]
            else:
                # fallback
                return paragraphs
        finally:
            if 'cur' in locals():
                cur.close()
            if con.is_connected():
                con.close()
    except Exception:
        return paragraphs


def save_results_to_db(user_id, accuracy, wpm, total_chars):
    try:
        con = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database="typerush_db"
        )
        try:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO typing_results (user_id, accuracy, wpm, total_chars) VALUES (%s, %s, %s, %s)",
                (user_id, accuracy, wpm, total_chars)
            )
            con.commit()
        finally:
            if 'cur' in locals():
                cur.close()
    except mysql.connector.Error as e:
        print(f"Error saving results: {e}")
    finally:
        if 'con' in locals() and con.is_connected():
            con.close()


def compute_results(total_typed_text, paragraphs, elapsed_time_seconds):
    if not total_typed_text.strip():
        return 0.0, 0.0, 0
    reference_text = " ".join(paragraphs)
    accuracy = calculate_accuracy(total_typed_text, reference_text)
    wpm = calculate_wpm(total_typed_text, elapsed_time_seconds)
    total_chars = len(total_typed_text.strip())
    return accuracy, wpm, total_chars


load_dotenv()

def get_user_progress(user_id):
    try:
        con = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database="typerush_db"
        )
        cur = con.cursor()
        cur.execute("""
            SELECT timestamp, wpm, accuracy, total_chars
            FROM typing_results
            WHERE user_id = %s
            ORDER BY timestamp ASC
        """, (user_id,))
        rows = cur.fetchall()
        df = pd.DataFrame(rows, columns=["timestamp", "wpm", "accuracy", "total_chars"])
        df["date"] = pd.to_datetime(df["timestamp"]).dt.date
        return df
    except mysql.connector.Error as e:
        print(f"Error fetching progress: {e}")
        return pd.DataFrame(columns=["timestamp", "wpm", "accuracy", "total_chars", "date"])
    finally:
        if 'cur' in locals():
            cur.close()
        if 'con' in locals() and con.is_connected():
            con.close()