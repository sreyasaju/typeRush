import resource_rc
from PySide6.QtWidgets import QDialog, QMessageBox
from ui.ui_registerdialog import Ui_registerDialog
from mainwindow import show_message
from core.auth_controller import AuthController

class RegisterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_registerDialog()
        self.ui.setupUi(self)
        self.auth_controller = AuthController()

        self.ui.reg_ok.clicked.connect(self.handle_ok)
        self.ui.reg_cancel.clicked.connect(self.handle_cancel)

    def handle_ok(self):
            username = self.ui.reg_usernameField.text()
            password = self.ui.reg_passwordField.text()

            success, msg = self.auth_controller.register(username, password)

            if success:
                title = "Success"
                icon = QMessageBox.Information
            else:
                title = "Error"
                icon = QMessageBox.Warning

            show_message(self, title, msg, icon=icon)

            if success:
                self.accept()  

    def handle_cancel(self):
        self.reject()