import time
import os
from dotenv import load_dotenv
import random
from mainwindow import MainWindow   
import mysql.connector
from mysql.connector import Error
from PySide6.QtWidgets import QDialog, QMainWindow
from utils import calculate_wpm, calculate_accuracy
from settings import SettingsDialog
from ui.ui_typinggame import Ui_typingGame
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMessageBox

# fallback sample paragraphs
paragraphs = [
    "Global warming is one of the most pressing environmental issues facing our planet today",
    "Reducing carbon emissions is essential to slowing global warming.",
    "Renewable energy sources like solar and wind power are key to sustainability.",
    "Recycling and reusing materials can significantly reduce environmental waste.",
    "Planting trees helps absorb carbon dioxide from the atmosphere.",
    "Melting glaciers are a visible sign of rising global temperatures.",
    "The ocean absorbs most of the heat caused by greenhouse gas emissions.",
    "Electric vehicles produce fewer emissions than gasoline-powered cars.",
    "Single-use plastics contribute to pollution in oceans and landfills.",
    "Switching to energy-efficient appliances helps reduce electricity consumption.",
    "Public transportation reduces the number of cars on the road and cuts emissions.",
    "Biodiversity is threatened by habitat loss and climate change.",
    "Sustainable agriculture supports food production while protecting the planet.",
    "Water conservation is vital in regions affected by drought and heatwaves.",
    "Deforestation increases the amount of carbon dioxide in the atmosphere.",
    "Rising sea levels threaten coastal communities around the world.",
    "Composting organic waste reduces methane emissions from landfills.",
    "Educating others about climate change promotes environmental action.",
    "Global cooperation is necessary to combat the effects of climate change.",
    "Buying local and seasonal food reduces the carbon footprint of transportation.",
    "Green buildings are designed to minimize energy and water use.",
    "Extreme weather events are becoming more frequent due to climate change.",
    "Overfishing and ocean acidification threaten marine ecosystems.",
    "Advocating for policy changes is an important part of climate activism.",
    "Using a reusable water bottle helps cut down on plastic waste.",
    "Switching to LED bulbs can lower energy use and utility bills.",
    "Air pollution contributes to climate change and harms human health.",
    "Supporting companies with sustainable practices encourages green innovation.",
    "Climate justice ensures vulnerable communities are not left behind.",
    "Every small action counts in the fight against climate change."
]


load_dotenv()
class TypingGameWindow(QMainWindow):
    def __init__(self, duration=60, parent=None):
        super().__init__(parent)
        self.ui = Ui_typingGame()
        self.ui.setupUi(self)
        self.duration = duration
        self.time_left = duration
        self.current_paragraph = ""
        self.total_typed_text = ""
        self.start_time = None
        self.game_over = False
        self.paragraphs = get_paragraphs_from_db() or paragraphs

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.ui.textfield.textChanged.connect(self.handle_changes)

        self.all_paragraphs_shown = []

        self.start_new_paragraph()
    
    def start_new_paragraph(self):
        # paragraph from DB or fallback
        self.current_paragraph = random.choice(self.paragraphs)
        self.all_paragraphs_shown.append(self.current_paragraph)
        self.ui.sentencelabel.setText(self.current_paragraph)
        self.ui.textfield.clear()
        self.time_left = self.duration
        self.ui.timer.setText(str(self.time_left))

    def handle_changes(self):
        typed_text = self.ui.textfield.toPlainText()
        if not typed_text:
            return
        # start timer on first keypress
        if not self.timer.isActive() and self.ui.textfield.toPlainText():
            self.start_time = time.time()
            self.timer.start(1000)

        if typed_text.strip() == self.current_paragraph.strip(): #if the user is so fast, and finished before time ended!
            self.total_typed_text += " " + typed_text.strip()

            # start a new paragraph immediately
            self.start_new_paragraph()
            
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
        reference_text = " ".join(self.all_paragraphs_shown)
        elapsed_time = self.duration 
        accuracy = calculate_accuracy(self.total_typed_text, reference_text) 
        wpm = calculate_wpm(self.total_typed_text, elapsed_time)
        
        QMessageBox.information(
            self,
            "Results",
            f"Accuracy: {accuracy:.2f}% \n WPM: {wpm:.2f} \n Total Characters: {len(self.total_typed_text.strip())}"
        )


def run_sql_file(filename):
    con = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )
    cur = con.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS typing_game")
    cur.execute("USE typing_game")
    
    with open(filename, 'r') as f:
        sql_commands = f.read().split(';')

    for command in sql_commands:
        cmd = command.strip()
        if cmd:
            cur.execute(cmd)
    con.commit()
    cur.close()
    con.close()


def get_paragraphs_from_db():
    try:
        con = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASS", ""),
            database="typing_game"
        )
        cur = con.cursor()
        cur.execute("SELECT text FROM typing_paragraphs")
        rows = cur.fetchall()
        return [row[0] for row in rows]

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return []

    finally:
        if 'cur' in locals():
            cur.close()
        if 'con' in locals() and con.is_connected():
            con.close()



if __name__ == "__main__":
    import traceback
    from settings import SettingsDialog
    from PySide6.QtWidgets import QApplication
    import sys
    try:
        run_sql_file("paragraphs.sql")

        app = QApplication(sys.argv)
        settings_dialog = SettingsDialog()

        if settings_dialog.exec() == QDialog.Accepted:
            duration = settings_dialog.duration

            global window
            window = TypingGameWindow(duration=duration)
            window.show()

            app.exec()
        else:
            print("Settings canceled, exiting.")

    except Exception:
        traceback.print_exc()