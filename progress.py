# progress.py

import resource_rc
from ui.ui_progress import Ui_progresswindow
from PySide6.QtWidgets import QMainWindow
from mysql.connector import Error
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from datetime import datetime
from matplotlib import font_manager as fm
from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtCore import QFile
import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os
import tempfile

load_dotenv()

class ProgressWindow(QMainWindow):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        self.ui = Ui_progresswindow()
        self.ui.setupUi(self)
        self.user_id = user_id

        fid = QFontDatabase.addApplicationFont(":/font/assets/font/BalooChettan2-VariableFont_wght.ttf")
        fam = QFontDatabase.applicationFontFamilies(fid)[0]
        self.setFont(QFont(fam, 20))

        res_file = QFile(":/font/assets/font/BalooChettan2-VariableFont_wght.ttf")
        res_file.open(QFile.ReadOnly)
        font_data = res_file.readAll()
        res_file.close()
        tmp_font = tempfile.NamedTemporaryFile(delete=False, suffix=".ttf")
        tmp_font.write(font_data)
        tmp_font.close()
        self.custom_font = fm.FontProperties(fname=tmp_font.name)

        self.ui.homebutton.clicked.connect(self.handle_homebutton)
        self.data = self.get_all_progress()

        latest_data = self.get_latest_progress()
        if latest_data:
            wpm, accuracy, total_chars, timestamp = latest_data
            self.ui.wpm_field.setText(f"{wpm:.2f}")
            self.ui.accuracy_field.setText(f"{accuracy:.2f}%")
            self.ui.nchar_field.setText(str(total_chars))
            self.ui.timestamp_field.setText(str(timestamp.date()))
        else:
            self.ui.timestamp_field.setText("N/A")
            self.ui.wpm_field.setText("N/A")
            self.ui.accuracy_field.setText("N/A")
            self.ui.nchar_field.setText("N/A")

        self.plot_wpm()

    def get_all_progress(self):
        try:
            con = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASS"),
                database="typerush_db"
            )
            cur = con.cursor()
            cur.execute("""
                SELECT timestamp, wpm
                FROM typing_results
                WHERE user_id = %s
                ORDER BY timestamp ASC
            """, (self.user_id,))
            rows = cur.fetchall()
            df = pd.DataFrame(rows, columns=["timestamp", "wpm"])
            df["date"] = pd.to_datetime(df["timestamp"]).dt.date
            return df
        except Error as e:
            print(f"Error fetching progress data: {e}")
            return pd.DataFrame(columns=["timestamp", "wpm", "date"])
        finally:
            if 'cur' in locals():
                cur.close()
            if 'con' in locals() and con.is_connected():
                con.close()

    def get_latest_progress(self):
        try:
            con = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASS"),
                database="typerush_db"
            )
            cur = con.cursor()
            cur.execute("""
                SELECT wpm, accuracy, total_chars, timestamp
                FROM typing_results
                WHERE user_id = %s
                ORDER BY timestamp DESC
                LIMIT 1
            """, (self.user_id,))
            row = cur.fetchone()
            return row
        except Error as e:
            print(f"Error fetching latest progress: {e}")
            return None
        finally:
            if 'cur' in locals():
                cur.close()
            if 'con' in locals() and con.is_connected():
                con.close()

    def plot_wpm(self):
        if self.data.empty:
            return

        if not pd.api.types.is_datetime64_any_dtype(self.data["date"]):
            self.data["date"] = pd.to_datetime(self.data["date"])

        x_labels = self.data["date"].dt.day

        import numpy as np

        self.fig = Figure(figsize=(4, 2.1), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.plot(np.arange(len(x_labels)), self.data["wpm"], marker="o", color="#00877e", lw=2)
        self.ax.set_xticks(np.arange(len(x_labels)))
        self.fig.patch.set_facecolor("#d6f5f9")
        self.ax.set_facecolor('#d6f5f9')
        self.ax.set_xticklabels(x_labels, fontproperties=self.custom_font)
        self.ax.set_xlabel("Date", fontproperties=self.custom_font)
        self.ax.set_ylabel("WPM", fontproperties=self.custom_font)

        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['left'].set_visible(False)
        self.ax.spines['bottom'].set_visible(False)

        self.ax.tick_params(axis='x', colors='#00877e')
        self.ax.tick_params(axis='y', colors='#00877e')
        self.ax.xaxis.label.set_color('#00877e')
        self.ax.yaxis.label.set_color('#00877e')
        self.ax.title.set_color('#00877e')

        if hasattr(self, "canvas"):
            self.canvas.setParent(None)

        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.ui.plotframe)
        self.canvas.setGeometry(self.ui.plotframe.rect())
        self.canvas.draw()

    def handle_homebutton(self):
        from home import HomeWindow
        self.home_window = HomeWindow(user_id=self.user_id)
        self.home_window.show()
        self.close()

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = ProgressWindow(user_id=1)
    window.show()
    sys.exit(app.exec())
