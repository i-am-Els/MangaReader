import sys
import setup
from PyQt6.QtWidgets import QApplication



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = setup.Window()
    #window.createMainStackWidget()
    window.showMaximized()
    sys.exit(app.exec())