from PyQt6.QtWidgets import QWidget, QStackedWidget

from themes import Themes
from settings import Settings

class Reader(QWidget):
    def __init__(self, obj, win_dow):
        super().__init__()

        self.obj = obj
        self.win_dow = win_dow

        
        self.themeObj = object()
        self.setting = object()

        self.themeIndex = object()

