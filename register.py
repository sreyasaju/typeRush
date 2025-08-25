"""
This is the signup module. It will open the signup dialog!
"""
import mysql.connector
from dotenv import load_dotenv
import os
from password_utils import generate_salt, hash_password, encode_salt

from PySide6.QtWidgets import QDialog, QMessageBox
from ui.ui_registerdialog import Ui_registerDialog

load_dotenv()
con = mysql.connector.connect(host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASS"))
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


class RegisterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_registerDialog()
        self.ui.setupUi(self)

        self.ui.reg_ok.clicked.connect(self.handle_ok)
        self.ui.reg_cancel.clicked.connect(self.handle_cancel)

    def is_valid_username(self, username):
        if " " in username or username != username.strip():
            return False
        return username.isalnum()

    def is_valid_password(self, password):
        if " " in password or password != password.strip():
            return False
        return password.isalnum()

    # register button handler
    def handle_ok(self):
        username = self.ui.reg_usernameField.text()
        password = self.ui.reg_passwordField.text()
        
        if not self.is_valid_username(username):
            QMessageBox.warning(self, "Error", "Invalid username format")
            return

        if not self.is_valid_password(password):
            QMessageBox.warning(self, "Error", "Invalid password format")
            return


        salt = generate_salt()
        hashed_pwd = hash_password(password, salt)
        salt_b64 = encode_salt(salt)

        try:
            cur.execute(
                "INSERT INTO users (username, password, salt) VALUES (%s, %s, %s)",
                (username.strip(), hashed_pwd, salt_b64)
            )
            con.commit()
            QMessageBox.information(self, "Success", f"User '{username}' registered successfully!")
            self.accept() 
        except mysql.connector.IntegrityError:
            QMessageBox.warning(self, "Error", "Username already exists")

    # cancel button handler
    def handle_cancel(self):
        self.reject()