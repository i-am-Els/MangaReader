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


import time
from PyQt6.QtWidgets import (
    QFrame, 
    QVBoxLayout,
    QWidget, 
    QProgressBar, 
    QLabel 
)
from settings import Settings

from PyQt6.QtCore import Qt, QTimer

class SplashScreen(QWidget):
    def __init__(self, appWindow) -> None:
        super().__init__()
        self.appWindow = appWindow
        self.setFixedSize(480, 300)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowTitle("Splash Screen")

        self.counter = 0
        self._n = 300
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.loading())
        self.timer.start(30)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.frame = QFrame()
        self.layout.addWidget(self.frame)

        self.labelTitle = QLabel(self.frame)
        self.labelTitle.setObjectName("labelTitle")
        self.labelTitle.resize(self.width() - 10, 150)
        self.labelTitle.move(0, 20)
        self.labelTitle.setText("Manhua Reader")
        self.labelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.labelDescription = QLabel(self.frame)
        self.labelDescription.setObjectName("labelDesc")
        self.labelDescription.resize(240, 20)
        self.labelDescription.move(100, self.labelTitle.height())
        self.labelDescription.setText("<strong>welcome on board to this great app</strong>")
        self.labelDescription.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.resize(440, 30)
        self.progressBar.move(10, self.labelDescription.y() + 40)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, self._n)
        self.progressBar.setValue(20)

        self.labelLoading = QLabel(self.frame)
        self.labelLoading.resize(self.width() - 10, 20)
        self.labelLoading.move(0, self.progressBar.y() + 40)
        self.labelLoading.setObjectName("loading")
        self.labelLoading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelLoading.setText("Loading...")

        self.setStyleSheet("""
            #labelTitle {
                font-size: 40px;
                color: rgb(239, 73, 55);
            }

            #labelDesc {
                font-size: 10px;
                color: rgb(250, 172, 63);
            }

            QFrame {
                background-color: rgb(72, 75, 105);
                color: rgb(220, 220, 220);
            }

            QProgressBar {
                background-color: rgba(239, 73, 55, 70);
                color: rgb(200, 200, 200);
                border: none;
                border-radius: 10px;
                text-align: center;
                font-size: 10px;
            }

            QProgressBar::chunk {
                border-radius: 10px;
                background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.5, y2:0.5, stop:0 rgb(239, 73, 55), stop:1 rgb(250, 172, 63))
            }
        """)

    def loading(self):
        self.progressBar.setValue(self.counter)
        if self.counter == int(self._n * 0.33):
            self.labelDescription.setText("<strong>we are working on loading your lovely app</strong>")
        elif self.counter == int(self._n * 0.67):
            self.labelDescription.setText("<strong>wait a little while as we get everything ready...</strong>")
        elif self.counter >= self._n:
            self.timer.stop()
            self.close()
            time.sleep(.5)
            self.appWindow.showMaximized()
            # if Settings.viewIsGrid:
            #     self.appWindow.stWindow.objMainWindow.selectViewTypeByObj(True)

            self.appWindow.stWindow.objMainWindow.library.switchLayout()
        self.counter += 1
        
