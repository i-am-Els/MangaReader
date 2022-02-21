from email.charset import QP
from PyQt6.QtWidgets import (
    QStackedWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QWidget,
    QLabel,
    QSizePolicy,
    QPushButton,
)


from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QCursor, QIcon, QPixmap, QFont

from themes import Themes


class Preference(QWidget):
    def __init__(self, obj, win_dow):
        super().__init__()
        self.obj = obj
        self.win_dow = win_dow

        self.max_button_size = QSize(36, 36)
        self.min_button_size = QSize(16, 16)
        self.icon_size = QSize(20, 20)
        self.active = 0
        self.themeIndex = 0

        self.sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        #-----------------------------------------------
        self.gridLayout = QGridLayout()

        # Create baseLayout
        self.baseLayout = QVBoxLayout()        
        self.baseLayout.setSpacing(9)

        #-----------------------------------------------
        # Create an horizontal headerLayout
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setContentsMargins(-1, 10, -1, 10)

        self.bodyLayout = QHBoxLayout()

        #-----------------------------------------------
        # Create a backButton
        self.backButton = QPushButton()
        self.backButton.setObjectName("backButton")

        self.backButton.setSizePolicy(self.sizePolicy)
        self.backButton.setMinimumSize(self.min_button_size)
        self.backButton.setMaximumSize(self.max_button_size)
        self.backButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.backButton.setGeometry(0, 0, 36, 36)

        # Set backIcon to backButton
        self.backIcon = QIcon()
        
        self.backButton.setIconSize(self.icon_size)
        self.backButton.setCheckable(True)

        #-----------------------------------------------
        self.headerLabel = QLabel("Preference | Settings")
        self.headerLabel.setObjectName("headerLabel")
        self.headerLabel.setSizePolicy(self.sizePolicy)
        
        self.headerLabelFont = QFont()
        self.headerLabelFont.setPointSize(16)
        self.headerLabelFont.setBold(True)
        self.headerLabel.setFont(self.headerLabelFont)
        self.headerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #-----------------------------------------------
        self.headerLayout.addWidget(self.backButton)
        self.headerLayout.addWidget(self.headerLabel)

        self.headerLayout.setStretch(0, 1)
        self.headerLayout.setStretch(1, 9)
        #-----------------------------------------------
        self.buttonsLayout = QVBoxLayout()
        self.buttonsLayout.setSpacing(5)

        self.settingsButton = QPushButton("Settings")
        self.settingsButton.setCheckable(True)
        self.settingsButton.setSizePolicy(self.sizePolicy)
        self.settingsButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settingsButton.setObjectName("settingsButton")

        self.downloadButton = QPushButton("Downloads")
        self.downloadButton.setCheckable(True)
        self.downloadButton.setSizePolicy(self.sizePolicy)
        self.downloadButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.downloadButton.setObjectName("downloadButton")

        self.themesButton = QPushButton("Themes")
        self.themesButton.setCheckable(True)
        self.themesButton.setSizePolicy(self.sizePolicy)
        self.themesButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.themesButton.setObjectName("themesButton")

        self.spaceEater = QWidget()
        self.spaceEater.setSizePolicy(self.sizePolicy)

        self.buttonsLayout.addWidget(self.settingsButton)
        self.buttonsLayout.addWidget(self.downloadButton)
        self.buttonsLayout.addWidget(self.themesButton)
        self.buttonsLayout.addWidget(self.spaceEater)

        self.buttonsLayout.setObjectName("buttonsLayout")

        self.buttonsLayout.setStretch(0, 1)
        self.buttonsLayout.setStretch(1, 1)
        self.buttonsLayout.setStretch(2, 1)
        self.buttonsLayout.setStretch(3, 12)


        #-----------------------------------------------
        self.stackLayout = QVBoxLayout()
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.setSizePolicy(self.sizePolicy)
        self.stackedWidget.setObjectName(u"prefStacked")

        self.settingsWidget = QWidget()
        self.settingsWidget.setObjectName("settingsWidget")
        self.settingsLayout = QVBoxLayout()
        
        self.settingsWidgetObj()

        self.settingsWidget.setLayout(self.settingsLayout)

        self.downloadsWidget = QWidget()
        self.downloadsWidget.setObjectName("downloadsWidget")
        self.downloadsLayout = QVBoxLayout()

        self.downloadWidgetObj()
        
        self.downloadsWidget.setLayout(self.downloadsLayout)

        self.themesWidget = QWidget()
        self.themesWidget.setObjectName("themesWidget")
        self.themesLayout = QVBoxLayout()

        self.themesWidgetObj()
        
        self.themesWidget.setLayout(self.themesLayout)

        self.stackedWidget.addWidget(self.settingsWidget)
        self.stackedWidget.addWidget(self.downloadsWidget)
        self.stackedWidget.addWidget(self.themesWidget)

        #---------------------------------------------------
        self.stackLayout.addWidget(self.stackedWidget)

        #-----------------------------------------------
        self.bodyLayout.addLayout(self.buttonsLayout)
        self.bodyLayout.addLayout(self.stackLayout)
        self.bodyLayout.setStretch(0, 2)
        self.bodyLayout.setStretch(1, 8)
        #-----------------------------------------------
        self.headerBackgroundWidget = QWidget()
        self.headerBackgroundLayout = QVBoxLayout()
        self.headerBackgroundWidget.setLayout(self.headerLayout)
        self.headerBackgroundLayout.addWidget(self.headerBackgroundWidget)

        self.baseLayout.addLayout(self.headerBackgroundLayout)
        self.baseLayout.addLayout(self.bodyLayout)

        self.baseLayout.setStretch(0, 1)
        self.baseLayout.setStretch(1, 11)
        #-----------------------------------------------

        self.gridLayout.addLayout(self.baseLayout, 0, 0, 1, 1)

        self.setLayout(self.gridLayout)
        #-----------------------------------------------

        self.backButton.clicked.connect(self.backAction)

        self.settingsButton.clicked.connect(lambda: self.setActive(self.settingsButton, 0))

        self.downloadButton.clicked.connect(lambda: self.setActive(self.downloadButton, 1))
        
        self.themesButton.clicked.connect(lambda: self.setActive(self.themesButton, 2))

    def backAction(self):
        self.obj.talkToStackWidgetIndex(0, self.win_dow)

    def changeStackIndex(self, obj, w_index):
        obj.setCurrentIndex(w_index)

    def setActive(self, cButton, activeIndex):
        self.active = activeIndex

        if self.themeIndex == 0:
            self.themeObj.prefButtonActiveLight(self, cButton)
        else:
            self.themeObj.prefButtonActiveDark(self, cButton)
        self.stackedWidget.setCurrentIndex(self.active)

    def settingsWidgetObj(self):
        self.libraryLabel = QLabel("Library")
        self.libraryLabel.set
        self.libraryLabel.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.settingsLayout.addWidget(self.libraryLabel)
        pass

    def downloadWidgetObj(self):
        self.dowBut = QLabel("Downloads")
        self.downloadsLayout.addWidget(self.dowBut)
        pass

    def themesWidgetObj(self):
        self.theBut = QLabel("Themes")
        self.themesLayout.addWidget(self.theBut)
        pass
