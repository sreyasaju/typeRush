# home.py
from PySide6.QtWidgets import QMainWindow
from ui.ui_home import Ui_home 

class HomeWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_home()
        self.ui.setupUi(self)

        self.ui.startbutton.clicked.connect(self.open_typinggame)
        #self.ui.progressbutton.clicked.connect(self.open_progress_window)
        #self.ui.logoutbutton.clicked.connect(self.handle_logout)

    def open_typinggame(self):
        from typinggame import TypingGameWindow
        self.typing_game_window = TypingGameWindow()
        self.typing_game_window.show()
        self.close()