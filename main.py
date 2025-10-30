import sys

def main():
    if "--cli" in sys.argv:
        from cli import main as cli_main
        cli_main()
    else:
        from PySide6.QtWidgets import QApplication
        from mainwindow import MainWindow

        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())

if __name__ == "__main__":
    main()