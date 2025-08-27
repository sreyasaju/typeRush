import mysql.connector
from dotenv import load_dotenv
import os
from password_utils import verify_password, decode_salt
from mainwindow import show_message
from PySide6.QtWidgets import QDialog, QMessageBox
from ui.ui_logindialog import Ui_loginDialog
from home import HomeWindow 

load_dotenv()

# Connect to MySQL
con = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME")
)
cur = con.cursor()

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_loginDialog()
        self.ui.setupUi(self)
        self.user_id = None

        self.ui.log_ok.clicked.connect(self.handle_ok)
        self.ui.log_cancel.clicked.connect(self.handle_cancel)

    def is_valid_username(self, username):
        if " " in username or username != username.strip():
            return False
        return username.isalnum() and username.isascii()

    def is_valid_password(self, password):
        if " " in password or password != password.strip():
            return False
        return password.isalnum() and password.isascii()

    # login button handler
    def handle_ok(self):
        username = self.ui.log_usernameField.text()
        password = self.ui.log_passwordField.text()

        if not self.is_valid_username(username):
            show_message(self, "Error", "Invalid username format", icon=QMessageBox.Warning)
            return

        if not self.is_valid_password(password):
            show_message(self, "Error", "Invalid password format", icon=QMessageBox.Warning)
            return

        cur.execute("SELECT password, salt FROM users WHERE username = %s", (username.strip(),))
        row = cur.fetchone()

        if row and verify_password(password, row[0], decode_salt(row[1])):
            show_message(self, "Success", f"Welcome, {username}!", icon=QMessageBox.Information)
            self.user_id = username
            self.accept()  # close login dialog

        else:
            show_message(self, "Error", "Invalid username or password", icon=QMessageBox.Warning)
            self.ui.log_usernameField.clear()
            self.ui.log_passwordField.clear()

    # cancel button handler
    def handle_cancel(self):
        self.reject()