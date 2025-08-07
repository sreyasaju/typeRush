import mysql.connector as sqlconnector
import hashlib

mycon = sqlconnector.connect(host="localhost", user="root", passwd="", database="test")
if mycon.is_connected():
    print("Sucessfully connected to MySQL database")
cursor = mycon.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS userdata (
        id INTEGER PRIMARY KEY, 
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")