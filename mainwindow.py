import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

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
        result = logindialog.exec()
        if result == QDialog.Accepted:
            from home import HomeWindow
            self.home_window = HomeWindow()
            self.home_window.show()
            self.close()

    def open_register_dialog(self):
        from register import RegisterDialog
        registerdialog = RegisterDialog(self)
        registerdialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
    QMessageBox {
        background-color: #e6faff;  
        font-size: 14px;
        font-family: 'Baloo Chettan 2';
    }
    QMessageBox QLabel {
        color: #053b37;
    }
    """)
    widget = MainWindow()

    widget.show()
    sys.exit(app.exec())
