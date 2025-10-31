import resource_rc
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from ui.ui_settings import Ui_settings

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_settings()
        self.ui.setupUi(self)
        
        self.ui.settings_cancelbutton.clicked.connect(self.reject)
        self.ui.settings_readybutton.clicked.connect(self.handle_ready)

    def handle_ready(self):
        duration_text = self.ui.durationField.text()
        if not duration_text.isdigit() or int(duration_text) <= 0:
            QMessageBox.warning(self, "Invalid Input", "Please enter a positive number for duration.")
            return
        if int(duration_text) > 1200:
            QMessageBox.warning(self, "Invalid Input", "Duration cannot be longer than 1200 seconds.")
            return

        self.duration = int(duration_text)
        self.accept()