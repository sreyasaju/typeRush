import resource_rc
from PySide6.QtWidgets import QMainWindow, QDialog, QTextEdit, QMessageBox
from PySide6.QtCore import QTimer
from PySide6.QtGui import QTextCharFormat, QTextCursor, QColor
from ui.ui_typinggame import Ui_typingGame
import random
import time
import difflib
from core.core import get_paragraphs_from_db, save_results_to_db, compute_results

class TypingGameWindow(QMainWindow):
    def __init__(self, user_id, duration=60, parent=None):
        super().__init__(parent)
        self.ui = Ui_typingGame()
        self.ui.setupUi(self)
        self.user_id = user_id
        self.duration = duration
        self.time_left = duration
        self.current_paragraph = ""
        self.total_typed_text = ""
        self.start_time = None
        self.game_over = False
        self.paragraphs = get_paragraphs_from_db()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.ui.textfield.textChanged.connect(self.handle_changes)

        self.ui.homebutton.clicked.connect(self.handle_homebutton)
        self.ui.restartbutton.clicked.connect(self.handle_restartbutton)

        self.all_paragraphs_shown = []

        self.start_new_paragraph()
    
    def start_new_paragraph(self):
        # paragraph from DB or fallback
        self.current_paragraph = random.choice(self.paragraphs)
        self.all_paragraphs_shown.append(self.current_paragraph)
        self.ui.sentencelabel.setText(self.current_paragraph)
        self.ui.textfield.clear()

    def handle_changes(self):
        typed_text = self.ui.textfield.toPlainText()
        reference = self.current_paragraph

        if not typed_text:
            self.ui.textfield.setExtraSelections([])  # clear highlights
            return

        # start timer on first keypress
        if not self.timer.isActive():
            self.start_time = time.time()
            self.timer.start(1000)

        # create extra selections for highlighting wrong chars
        selections = []

        matcher = difflib.SequenceMatcher(None, typed_text, reference)  # Levenshtein distance calculations

        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag in ("replace", "delete", "insert"):
                for position in range(i1, i2):
                    selection = QTextEdit.ExtraSelection()
                    format = QTextCharFormat()
                    format.setBackground(QColor("#ffcccc"))  # mistakes.....
                    selection.format = format
                    cursor = self.ui.textfield.textCursor()
                    cursor.setPosition(position)
                    cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, 1)   
                    selection.cursor = cursor
                    selections.append(selection)

        # apply highlights
        self.ui.textfield.setExtraSelections(selections)

        if len(typed_text.strip()) >= len(reference.strip()):
            self.total_typed_text += " " + typed_text.strip()
            self.start_new_paragraph()  # fast user? next paragraph!!!
            
    def update_timer(self):
        if self.game_over:
            return
            
        self.time_left -= 1
        self.ui.timer.setText(str(self.time_left))
        if self.time_left <= 0:
            self.timer.stop()
            self.total_typed_text += " " + self.ui.textfield.toPlainText().strip()
            self.show_results()
            self.game_over = True
            self.ui.textfield.setReadOnly(True)
            
    def show_results(self):
        if not self.start_time:
            elapsed_time = self.duration
        else:
            elapsed_time = time.time() - self.start_time
            if elapsed_time <= 0:
                elapsed_time = self.duration

        accuracy, wpm, total_chars = compute_results(
            self.total_typed_text,
            self.all_paragraphs_shown,
            elapsed_time
        )

        QMessageBox.information(
            self,
            "Results",
            f"Accuracy: {accuracy:.2f}% \nWPM: {wpm:.2f} \nTotal Characters: {total_chars}",
        )

        save_results_to_db(self.user_id, accuracy, wpm, total_chars)

    def handle_homebutton(self):
        from home import HomeWindow
        self.home_window = HomeWindow(user_id=self.user_id)
        self.home_window.show()
        self.close()
    
    def handle_restartbutton(self):
        from settings import SettingsDialog
        self.settings_dialog = SettingsDialog(self)
        if self.settings_dialog.exec() == QDialog.Accepted:
            new_duration = self.settings_dialog.duration
            # reset game state
            self.duration = new_duration
            self.time_left = new_duration
            self.total_typed_text = ""
            self.all_paragraphs_shown = []
            self.start_new_paragraph()
            self.ui.textfield.setReadOnly(False)
            self.game_over = False
            self.timer.stop()


if __name__ == "__main__":
    import traceback
    from settings import SettingsDialog
    from PySide6.QtWidgets import QApplication
    import sys
    try:
        app = QApplication(sys.argv)
        settings_dialog = SettingsDialog()

        if settings_dialog.exec() == QDialog.Accepted:
            duration = settings_dialog.duration

            window = TypingGameWindow(user_id=1, duration=duration)
            window.show()

            app.exec()
        else:
            print("Settings canceled, exiting.")

    except Exception:
        traceback.print_exc()