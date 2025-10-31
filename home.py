
from PySide6.QtWidgets import QMainWindow, QDialog, QApplication
import sys
import mysql.connector
from dotenv import load_dotenv
import os   
from ui.ui_home import Ui_home 
from settings import SettingsDialog
from typinggame import TypingGameWindow
from progress import ProgressWindow
from core.core import initialize_database


load_dotenv()

class HomeWindow(QMainWindow):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        self.ui = Ui_home()
        self.ui.setupUi(self)
        
        self.user_id = user_id
        initialize_database()

        self.ui.startbutton.clicked.connect(self.open_settings)
        self.ui.progressbutton.clicked.connect(self.open_progress_window)
        self.ui.logoutbutton.clicked.connect(self.handle_logout)

    def open_settings(self):
        settings_dialog = SettingsDialog(self)
        if settings_dialog.exec() == QDialog.Accepted:
            duration = settings_dialog.duration
            self.close()
            self.typing_game = TypingGameWindow(user_id=self.user_id, duration=duration)
            self.typing_game.show()

    def open_progress_window(self):
        self.progress_window = ProgressWindow(user_id=self.user_id) 
        self.progress_window.show()

    def handle_logout(self):
        from mainwindow import MainWindow 
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(app.exec())