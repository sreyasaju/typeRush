# login.py

import resource_rc
from mainwindow import show_message
from PySide6.QtWidgets import QDialog, QMessageBox
from ui.ui_logindialog import Ui_loginDialog
from home import HomeWindow 
from core.auth_controller import AuthController
from PySide6.QtGui import QFontDatabase, QFont


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_loginDialog()
        self.ui.setupUi(self)
        self.user_id = None
        self.auth_controller = AuthController()

        fid = QFontDatabase.addApplicationFont(":/font/assets/font/BalooChettan2-VariableFont_wght.ttf")
        fam = QFontDatabase.applicationFontFamilies(fid)[0]
        self.setFont(QFont(fam, 20))

        self.ui.log_ok.clicked.connect(self.handle_ok)
        self.ui.log_cancel.clicked.connect(self.handle_cancel)
   

    def handle_ok(self):
        username = self.ui.log_usernameField.text()
        password = self.ui.log_passwordField.text()
        success, message = self.auth_controller.login(username, password)
        if success:
            show_message(self, "Success", message, icon=QMessageBox.Information)
            self.user_id = username
            self.accept()
        else:
            show_message(self, "Error", message, icon=QMessageBox.Warning)
            self.ui.log_usernameField.clear()
            self.ui.log_passwordField.clear()

    def handle_cancel(self):
        self.reject()