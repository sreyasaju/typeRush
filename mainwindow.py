# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connect buttons to handlers
        self.ui.loginbutton.clicked.connect(self.open_login_dialog)
        self.ui.registerbutton.clicked.connect(self.open_register_dialog)

    def open_login_dialog(self):
        from login import LoginDialog
        logindialog = LoginDialog(self)
        logindialog.exec()    

    def open_register_dialog(self):
        from register import RegisterDialog
        registerdialog = RegisterDialog(self)
        registerdialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()

    widget.show()
    sys.exit(app.exec())
