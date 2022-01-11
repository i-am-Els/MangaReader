import sys
from PyQt6.QtWidgets import QApplication
import setup


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = setup.Window()
    window.showMaximized()
    sys.exit(app.exec())