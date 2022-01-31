from PyQt6.QtWidgets import QWidget



class Reader(QWidget):
    def __init__(self, obj, win_dow):
        super().__init__()

        self.obj = obj
        self.win_dow = win_dow

