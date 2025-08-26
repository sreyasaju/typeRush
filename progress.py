from ui.ui_progress import Ui_progresswindow
from PySide6.QtWidgets import QMainWindow
from mysql.connector import Error
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from datetime import datetime
from matplotlib import font_manager as fm



import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# Relative path to font
font_path = "assets/font/BalooChettan2-VariableFont_wght.ttf"
custom_font = fm.FontProperties(fname=font_path)

class ProgressWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_progresswindow()
        self.ui.setupUi(self)

        self.ui.homebutton.clicked.connect(self.handle_homebutton)
        # Fetch all progress for plotting
        self.data = self.get_all_progress()

        # Fetch latest session for labels
        latest_data = self.get_latest_progress()
        if latest_data:
            wpm, accuracy, total_chars, timestamp = latest_data
            self.ui.wpm_field.setText(f"{wpm:.2f}")
            self.ui.accuracy_field.setText(f"{accuracy:.2f}%")
            self.ui.nchar_field.setText(str(total_chars))
            self.ui.timestamp_field.setText(str(timestamp.date()))  # only date
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
                ORDER BY timestamp ASC
            """)
            rows = cur.fetchall()
            df = pd.DataFrame(rows, columns=["timestamp", "wpm"])
            # Convert timestamp to date for plotting
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
                ORDER BY timestamp DESC
                LIMIT 1
            """)
            row = cur.fetchone()
            return row  # tuple: (wpm, accuracy, total_chars, timestamp)
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

        # Ensure date column is datetime
        if not pd.api.types.is_datetime64_any_dtype(self.data["date"]):
            self.data["date"] = pd.to_datetime(self.data["date"])

        # Format date for X-axis as DDMMYYYY
        x_labels = self.data["date"].dt.day

        import numpy as np

        # Create figure and axes
        self.fig = Figure(figsize=(4, 2.1), dpi=100)  # 400x210 pixels
        self.ax = self.fig.add_subplot(111)
        self.ax.plot(np.arange(len(x_labels)), self.data["wpm"], marker="o", color="#00877e", lw=2)
        self.ax.set_xticks(np.arange(len(x_labels)))
        self.fig.patch.set_facecolor("#d6f5f9")
        self.ax.set_facecolor('#d6f5f9')
        self.ax.set_xticklabels(x_labels, fontproperties=custom_font)
        self.ax.set_xlabel("Date", fontproperties=custom_font)
        self.ax.set_ylabel("WPM", fontproperties=custom_font)
              
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
        self.home_window = HomeWindow()
        self.home_window.show()
        self.close()

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = ProgressWindow()
    window.show()
    sys.exit(app.exec())