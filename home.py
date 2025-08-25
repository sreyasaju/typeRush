# home.py
from PySide6.QtWidgets import QMainWindow
from ui.ui_home import Ui_home 
from settings import SettingsDialog
from typinggame import TypingGameWindow

class HomeWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_home()
        self.ui.setupUi(self)

        self.ui.startbutton.clicked.connect(self.open_settings)
        #self.ui.progressbutton.clicked.connect(self.open_progress_window)
        #self.ui.logoutbutton.clicked.connect(self.handle_logout)

    def open_settings(self):
        settings_dialog = SettingsDialog(self)
        if settings_dialog.exec() == SettingsDialog.Accepted:
            # settings dialog closed with Ready
            duration = settings_dialog.duration
            self.close()
            self.typing_game = TypingGameWindow(duration)
            self.typing_game.show()