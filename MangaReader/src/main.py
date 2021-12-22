import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # Inheriting from QMainWIndow

        self.setWindowTitle("MyApp")
        button = QPushButton("Push Me")
        
        self.setFixedSize(QSize(900, 600)) # Makes the window unresizable, you can't even maximize 
        self.setMinimumSize(QSize(600, 400)) # Sets the minimum size the window can scale down to

        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec() # Execute event loop