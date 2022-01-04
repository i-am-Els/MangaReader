from PyQt6.QtWidgets import QApplication, QCheckBox, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import QSize, Qt

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()

        self.toggled = False
        self.cb = QCheckBox()
        self.cb.clicked.connect(self.toggled_box)
        self.cb.setChecked(self.toggled)

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.cb)

        container = QWidget()
        container.setLayout(layout)
        self.setMinimumSize(500, 500)

        self.setCentralWidget(container)

    def toggled_box(self):
        self.toggled = self.cb.isChecked()
        print(self.toggled)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
