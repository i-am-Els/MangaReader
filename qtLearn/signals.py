import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # Inheriting from QMainWIndow

        self.setWindowTitle("MyApp")

        self.button_is_checked = False
        self.button = QPushButton("Push Me")
        self.setFixedSize(QSize(900, 600)) # Makes the window unresizable, you can't even maximize 
        self.setMinimumSize(QSize(600, 400)) # Sets the minimum size the window can scale down to
        self.button.setCheckable(True) # Triggers the effect that the button has being checked
        self.button.released.connect(self.this_button_was_released)
        self.button.setChecked(self.button_is_checked)
        
        self.setCentralWidget(self.button)

    def this_button_was_released(self):
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec() # Execute event loop