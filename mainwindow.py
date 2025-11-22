# mainwindow.py

import sys
import resource_rc
import os

os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"   


from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PySide6.QtGui import QFontDatabase, QFont
from ui.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        fid = QFontDatabase.addApplicationFont(":/font/assets/font/BalooChettan2-VariableFont_wght.ttf")
        fam = QFontDatabase.applicationFontFamilies(fid)[0]
        self.setFont(QFont(fam, 20))

        if sys.platform.startswith("win"):
            self.ui.typerush.setFont(QFont(fam, 50, 700))
            self.ui.subtitle.setFont(QFont(fam, 20))
            # self.ui.typerush.setFont

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
    msg.setOption(QMessageBox.DontUseNativeDialog, True)
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
    from PySide6 import QtCore

    
    app = QApplication(sys.argv)
    fid = QFontDatabase.addApplicationFont(":/font/assets/font/BalooChettan2-VariableFont_wght.ttf")
    if fid != -1:
        fam = QFontDatabase.applicationFontFamilies(fid)[0]
        app.setFont(QFont(fam, 20))
    else:
        print("Failed to load custom font, using system default.")

    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
