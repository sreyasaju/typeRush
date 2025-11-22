# main.py

import sys
import resource_rc

def main():
    if "--cli" in sys.argv:
        from cli import main as cli_main
        cli_main()
    else:
        from PySide6.QtWidgets import QApplication
        from PySide6.QtGui import QFontDatabase, QFont
        from mainwindow import MainWindow

        app = QApplication(sys.argv)

        fid = QFontDatabase.addApplicationFont(":/font/assets/font/BalooChettan2-VariableFont_wght.ttf")
        print(fid)
        fam = QFontDatabase.applicationFontFamilies(fid)[0]
        app.setFont(QFont(fam, 20))

        app.setStyleSheet("""
        QLabel { color: white; }
        QPushButton {
            background-color: #00dacc;
            color: white;
            border-radius: 15px;
            font-weight: bold;
        }
        """)

        window = MainWindow()
        window.show()
        sys.exit(app.exec())

if __name__ == "__main__":
    main()
