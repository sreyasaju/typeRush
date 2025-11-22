# core/auth_controller.py

import os
import mysql.connector
from dotenv import load_dotenv
from password_utils import verify_password, decode_salt, generate_salt, hash_password, encode_salt

load_dotenv()

def mysql_connection():
    con = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )
    return con

class AuthController:
    def __init__(self):
        self.user_id = None
        self.init_db()

    def init_db(self):
        con = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
        )
        cur = con.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS typerush_db")
        con.database = "typerush_db"
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username VARCHAR(50) PRIMARY KEY,
                password VARCHAR(64),
                salt VARCHAR(24)
            )
        """)
        con.commit()
        cur.close()
        con.close()
    
    def is_valid_username(self, username):
        if " " in username or username != username.strip():
            return False
        return username.isalnum() and username.isascii()

    def is_valid_password(self, password):
        if " " in password or password != password.strip():
            return False
        return password.isalnum() and password.isascii()
    

    def register(self,username,password):

        if not self.is_valid_username(username):
            return False, "Invalid username format"

        if not self.is_valid_password(password):
            return False, "Invalid password format"


        salt = generate_salt()
        hashed_pwd = hash_password(password, salt)
        salt_b64 = encode_salt(salt)

        con = mysql_connection()
        cur = con.cursor()

        try:
            cur.execute(
                "INSERT INTO users (username, password, salt) VALUES (%s, %s, %s)",
                (username.strip(), hashed_pwd, salt_b64)
            )
            con.commit()
            return True, f"User '{username}' registered successfully!"
        except mysql.connector.IntegrityError:
            return False, "Username already exists"
        finally:
            cur.close()
            con.close()

    
    
    def login(self,username,password):
        if not self.is_valid_username(username):
            return False, "Invalid username format"


        if not self.is_valid_password(password):
            return False, "Invalid password format"

        con = mysql_connection()
        cur = con.cursor()

        cur.execute("SELECT password, salt FROM users WHERE username = %s", (username.strip(),)) # parameterized query to prevent SQL injection
        row = cur.fetchone()

        cur.close()
        con.close()

        if row and verify_password(password, row[0], decode_salt(row[1])):
            self.user_id = username
            return True, f"Welcome, {username}!"

        else:
            return False, "Invalid username or password"
        





