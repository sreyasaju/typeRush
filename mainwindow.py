import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox

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
            user_id = logindialog.user_id
            from home import HomeWindow
            self.home_window = HomeWindow(user_id=user_id)
            self.home_window.show()
            self.close()

    def open_register_dialog(self):
        from register import RegisterDialog
        registerdialog = RegisterDialog(self)
        registerdialog.exec()

def show_message(parent, title, text, icon=QMessageBox.Information):
    msg = QMessageBox(parent)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setIcon(icon)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setOption(QMessageBox.DontUseNativeDialog, True) # strictly use Qt dialog

    msg.setStyleSheet("""
        QMessageBox {
            background-color: #E2FBFF;
            color: #004A55;
            font-family: 'Baloo Chettan 2', sans-serif;
            font-size: 14px;
        }
        QMessageBox QLabel {
            color: #004A55;
        }
        QMessageBox QDialogButtonBox QPushButton {
            background-color: #C4DADD;
            color: #004A55;
            font-weight: bold;
            min-width: 70px;
            min-height: 25px;
        }
        QMessageBox QDialogButtonBox QPushButton:hover {
            background-color: #A7C9CE;
        }
    """)
    
    msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    import os
    from PySide6.QtGui import QFontDatabase, QFont

    font_path = os.path.join(os.path.dirname(__file__), "assets", "font", "BalooChettan2-VariableFont_wght.ttf")
    font_id = QFontDatabase.addApplicationFont(font_path)
    if font_id != -1:
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        app.setFont(QFont(font_family)) 
    else:
        print("Failed to load custom font. Using system default.")


    app.setStyleSheet("""
        QMessageBox QLabel { 
            color: #004C58; 
        }
        QMessageBox QPushButton { 
            color: #004C58; 
        }
    """)
    widget = MainWindow()

    widget.show()
    sys.exit(app.exec())
