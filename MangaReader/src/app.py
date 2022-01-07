import sys
from PyQt6.QtWidgets import QApplication
import main


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main.Window()
    window.showMaximized()
    sys.exit(app.exec())