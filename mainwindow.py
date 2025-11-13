import sys
import resource_rc
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PySide6.QtGui import QFontDatabase, QFont
from ui.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scale_fonts_by_dpi()

        self.ui.loginbutton.clicked.connect(self.open_login_dialog)
        self.ui.registerbutton.clicked.connect(self.open_register_dialog)

    def scale_fonts_by_dpi(self):
        screen = self.screen()
        dpi = screen.logicalDotsPerInch()
        base_font_size = 20
        scaled_font_size = max(10, int(base_font_size * dpi / 96))  # 96 DPI is standard
        fid = QFontDatabase.addApplicationFont(":/font/assets/font/BalooChettan2-VariableFont_wght.ttf")
        if fid != -1:
            fam = QFontDatabase.applicationFontFamilies(fid)[0]
            font = QFont(fam, scaled_font_size)
            self.setFont(font)
            QApplication.instance().setFont(font)
        else:
            font = QFont("", scaled_font_size)
            self.setFont(font)
            QApplication.instance().setFont(font)

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
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    dpi = screen.logicalDotsPerInch()
    base_font_size = 20
    scaled_font_size = max(10, int(base_font_size * dpi / 96))  # 96 DPI standard
    fid = QFontDatabase.addApplicationFont(":/font/assets/font/BalooChettan2-VariableFont_wght.ttf")
    if fid != -1:
        fam = QFontDatabase.applicationFontFamilies(fid)[0]
        app.setFont(QFont(fam, scaled_font_size))
    else:
        print("Failed to load custom font, using system default.")
        app.setFont(QFont("", scaled_font_size))

    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
