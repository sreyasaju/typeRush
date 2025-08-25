"""
This is the login module. It will open the login dialog!
"""

from PySide6.QtWidgets import QDialog, QMessageBox
from ui.ui_logindialog import Ui_loginDialog

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_loginDialog()
        self.ui.setupUi(self)
        # connect buttons
        self.ui.log_ok.clicked.connect(self.handle_ok)
        self.ui.log_cancel.clicked.connect(self.reject)

    def handle_ok(self):
        username = self.ui.usernameLineEdit.text()
        password = self.ui.passwordLineEdit.text()

        # validation, TODO: replace with real validation
        if username == "admin" and password == "1234":
            QMessageBox.information(self, "Success", "Login successful!")
            self.accept()  
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials")
            self.ui.usernameLineEdit.clear()
            self.ui.passwordLineEdit.clear()
       
