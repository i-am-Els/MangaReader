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
    QTabWidget,
    QWidget,
    QPushButton,
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.screen_width = 1366
        self.screen_height = 768
        self.setWindowTitle("Manhua Reader")

       """ #-----------------------------------------------------------------------------
        # Create a vertical centralLayout
        centralLayout = QVBoxLayout()
        self.setLayout(centralLayout)

        #-----------------------------------------------------------------------------
        # Create an horizontal searchLayout
        searchLayout = QHBoxLayout()
        # Add widgets to the searchLayout
        searchLayout.addWidget(QPushButton("Menu"), 0)
        searchLayout.addWidget(QPushButton("Enter Keyword"), 2)
        searchLayout.addWidget(QPushButton("Search online"), 0)
        searchLayout.addWidget(QPushButton("local Search"), 0)
                
        #-----------------------------------------------------------------------------   
        # Create an vertical homeLayout
        homeLayout = QVBoxLayout()
        # Create the tabWidget in homeLayout
        tabWidget = QTabWidget()
        # Set Position of tabBar to left
        # tabWidget.setTabPosition(QTabWidget.West)
        # Add tabs to the tabWidget
        tabWidget.addTab(self.genHomeTab(), "Home")
        tabWidget.addTab(self.genLibraryTab(), "Library")
        # Add tabWidget to the homeLayout
        homeLayout.addWidget(tabWidget)
        #-----------------------------------------------------------------------------

        # Create an vertical historyLayout
        historyLayout = QVBoxLayout()

        #-----------------------------------------------------------------------------
        # Create an horizontal containerLayout
        containerLayout = QHBoxLayout()
        # Add widgets to the containerLayout
        containerLayout.addChildLayout(homeLayout)
        containerLayout.addChildLayout(historyLayout)

        # Add Layout to parent
        centralLayout.addChildLayout(searchLayout)
        centralLayout.addChildLayout(containerLayout)"""

    def genHomeTab(self):
            pass

    def genLibraryTab(self):
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())