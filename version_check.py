# PyQt version check
from PyQt6.QtCore import QT_VERSION_STR
print("PyQt6 version: ", QT_VERSION_STR)

# PySide version check
import PySide6
print("PySide6 version: ", PySide6.__version__)

# Python version check
import sys
print("Python version:", sys.version)

# Platform Check
import platform
print(platform.platform())

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QPushButton,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.screen_width = 1366
        self.screen_height = 768
        self.setWindowTitle("Manhua Reader")

        # Create a vertical layout
        """
        layout = QVBoxLayout()
        # Add widgets to the layout
        layout.addWidget(QPushButton("top"),0)
        layout.addWidget(QPushButton("middle"), 2)
        layout.addWidget(QPushButton("buttom"), 0)
        """

        # Create an horizontal layout
        #"""
        layout = QHBoxLayout()
        # Add widgets to the layout
        layout.addWidget(QPushButton("Menu"), 0)
        layout.addWidget(QPushButton("Enter Keyword"), 2)
        layout.addWidget(QPushButton("Search online"), 0)
        layout.addWidget(QPushButton("local Search"), 0)
        #"""

        # Add Layout to parent
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())