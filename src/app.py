# Manhua Reader,  An application for reading manhuas and manhuas online and offline
# Copyright (C) 2022  Eniola Emmanuel Olawale

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QMainWindow, QSizePolicy
from PyQt6.QtCore import QSize, Qt
import sys, creator, ctypes
from themes import WindowTitleBar, MoveableWindow

def setTaskBarIcon():
    myappid = u"El's.native_app.manhua_reader.v1.0.01" # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class  App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint|Qt.WindowType.WindowMaximizeButtonHint|Qt.WindowType.WindowMinimizeButtonHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.titleCustom = self.selfTitle = "Manhua Reader"

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.appLayout = QVBoxLayout()
        self.appWidget = QWidget()

        self.stWindow = creator.Window(self)
        self.stWindowLayout = QVBoxLayout()
        self.stWindowLayout.addWidget(self.stWindow)

        self.customTitleBar = WindowTitleBar(self, self.titleCustom, self.stWindow)
        self.cLayout = QVBoxLayout()
        self.cWidget = MoveableWindow(self, self.stWindow)
        self.cWidget.setSizePolicy(sizePolicy)
        self.cWidget.setFixedHeight(30)
        self.cWidget.refIcon = self.customTitleBar.restoreIcon
        self.cWidget.refIconIcon = self.customTitleBar.restoreIconIcon
        
        self.cWidget.setLayout(self.customTitleBar)
        self.cWidget.setMaximumHeight(30)
        self.cWidget.setStyleSheet("QWidget{background-color: rgba(72, 75, 106, 0.65); color: white;}")
        self.cLayout.addWidget(self.cWidget)
        self.cLayout.setSpacing(0)
        self.cLayout.setContentsMargins(0,0,0,0)
        
        self.appLayout.addLayout(self.cLayout)
        self.appLayout.addLayout(self.stWindowLayout)

        self.appLayout.setStretch(0, 1)
        self.appLayout.setStretch(1, 11)
        self.appLayout.setSpacing(0)

        self.appLayout.setContentsMargins(0,0,0,0)

        self.appWidget.setLayout(self.appLayout)

        # self.setWindowIcon(stWindow.windowIcon)
        
        
        self.setCentralWidget(self.appWidget)

        self.min_screen_width = 1092
        self.min_screen_height = 614

        self.setMinimumSize(QSize(self.min_screen_width, self.min_screen_height))
        self.setWindowTitle(self.selfTitle)

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    app.setOrganizationName("El's")
    app.setOrganizationDomain("els.ng")
    app.setApplicationName("Manhua Reader")
    

    setTaskBarIcon()
    appWindow = App()
    app.setWindowIcon(appWindow.stWindow.windowIcon)
    appWindow.showMaximized()

    sys.exit(app.exec())