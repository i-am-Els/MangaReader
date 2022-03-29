# Manhua Reader,  An application for reading mangas and manhuas online and offline
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
from PyQt6.QtCore import QSize
import sys, setup, ctypes
from themes import WindowTitleBar, MoveableWindow

def setTaskBarIcon():
    myappid = u"El's.native_app.manhua_reader.v1.0.01" # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    app.setOrganizationName("El's")
    app.setOrganizationDomain("els.ng")
    app.setApplicationName("Manhua Reader")
    

    setTaskBarIcon()
    appWindow = QMainWindow()
    appWindowTitleCustom = appWindow.appWindowTitle = "Manhua Reader"

    sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    appLayout = QVBoxLayout()
    appWidget = QWidget()

    stWindow = setup.Window()
    stWindowLayout = QVBoxLayout()
    stWindowLayout.addWidget(stWindow)

    customTitleBar = WindowTitleBar(appWindow, appWindowTitleCustom, stWindow.windowIcon)

    cLayout = QVBoxLayout()
    cWidget = MoveableWindow(appWindow)
    cWidget.setSizePolicy(sizePolicy)
    cWidget.setFixedHeight(30)
    cWidget.refIcon = customTitleBar.restoreIcon
    cWidget.refIconIcon = customTitleBar.restoreIconIcon
    
    cWidget.setLayout(customTitleBar)
    cWidget.setMaximumHeight(30)
    cWidget.setStyleSheet("QWidget{background-color: rgba(72, 75, 106, 0.65); color: white;}")
    cLayout.addWidget(cWidget)
    cLayout.setSpacing(0)
    cLayout.setContentsMargins(0,0,0,0)
    
    appLayout.addLayout(cLayout)
    appLayout.addLayout(stWindowLayout)

    appLayout.setStretch(0, 1)
    appLayout.setStretch(1, 20)
    appLayout.setSpacing(0)

    appLayout.setContentsMargins(0,0,0,0)

    appWidget.setLayout(appLayout)

    # appWindow.setWindowIcon(stWindow.windowIcon)
    
    
    appWindow.setCentralWidget(appWidget)

    appWindow.min_screen_width = 1092
    appWindow.min_screen_height = 614

    appWindow.setMinimumSize(QSize(appWindow.min_screen_width, appWindow.min_screen_height))
    appWindow.setWindowTitle(appWindow.appWindowTitle)

    app.setWindowIcon(stWindow.windowIcon)
    appWindow.showMaximized()
    

    sys.exit(app.exec())