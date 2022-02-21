from PyQt6.QtWidgets import (
    QStackedWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QWidget,
    QLabel,
    QSizePolicy,
    QPushButton,
    QRadioButton
)


from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QCursor, QIcon, QFont


from themes import ToggleSwitch


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

        self.fontSize1 = 16
        self.fontSize2 = 14
        self.fontSize3 = 12


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
        self.headerLabelFont.setPointSize(self.fontSize1)
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
        self.settingsWidget.setSizePolicy(self.sizePolicy)
        self.settingsLayout = QVBoxLayout()
        
        self.settingsWidgetObj()

        self.settingsWidget.setLayout(self.settingsLayout)
        

        self.downloadsWidget = QWidget()
        self.downloadsWidget.setObjectName("downloadsWidget")
        self.downloadsWidget.setSizePolicy(self.sizePolicy)
        self.downloadsLayout = QVBoxLayout()

        self.downloadWidgetObj()
        
        self.downloadsWidget.setLayout(self.downloadsLayout)

        self.themesWidget = QWidget()
        self.themesWidget.setObjectName("themesWidget")
        self.themesWidget.setSizePolicy(self.sizePolicy)
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
        self.libraryLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.libraryLabel.setSizePolicy(self.sizePolicy)

        self.libraryLabelFont = QFont()
        self.libraryLabelFont.setBold(True)
        self.libraryLabelFont.setPointSize(self.fontSize1)

        self.libraryLabel.setFont(self.libraryLabelFont)

        self.libraryLabelLayout = QVBoxLayout()
        self.libraryLabelLayout.addWidget(self.libraryLabel)

        #----------------------------------------------

        self.autoUpdateLabel = QLabel("Auto Update Library")
        self.autoUpdateLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.autoUpdateLabel.setSizePolicy(self.sizePolicy)
        self.autoUpdateLabelFont = QFont()
        self.autoUpdateLabelFont.setPointSize(self.fontSize2)
        self.autoUpdateLabel.setFont(self.autoUpdateLabelFont)

        self.autoUpdateLabelLayout = QVBoxLayout()
        self.autoUpdateLabelLayout.addWidget(self.autoUpdateLabel)
        #------------------

        self.autoUpdateLabelOne = QLabel("Chapters")
        self.autoUpdateLabelOne.setSizePolicy(self.sizePolicy)

        self.autoUpdateLabelOneFont = QFont()
        self.autoUpdateLabelOneFont.setPointSize(self.fontSize3)
        self.autoUpdateLabelOne.setFont(self.autoUpdateLabelOneFont)

        self.autoUpdateLabelOneLayout = QHBoxLayout()
        
        self.toggleOne = ToggleSwitch()
        self.toggleOne.setSizePolicy(self.sizePolicy)

        self.autoUpdateLabelOneLayout.addWidget(self.autoUpdateLabelOne)
        self.autoUpdateLabelOneLayout.addWidget(self.toggleOne)

        #------------------

        self.autoUpdateLabelTwo = QLabel("Cover Image and Description")
        self.autoUpdateLabelTwo.setSizePolicy(self.sizePolicy)

        self.autoUpdateLabelTwoFont = QFont()
        self.autoUpdateLabelTwoFont.setPointSize(self.fontSize3)
        self.autoUpdateLabelTwo.setFont(self.autoUpdateLabelTwoFont)

        self.autoUpdateLabelTwoLayout = QHBoxLayout()

        self.toggleTwo = ToggleSwitch()
        self.toggleTwo.setSizePolicy(self.sizePolicy)

        self.autoUpdateLabelTwoLayout.addWidget(self.autoUpdateLabelTwo)
        self.autoUpdateLabelTwoLayout.addWidget(self.toggleTwo)

        self.autoUpdateLabelOneLayout.setContentsMargins(25, 0, 0, 0)
        self.autoUpdateLabelTwoLayout.setContentsMargins(25, 0, 0, 0)
        #------------------

        self.autoUpdateLayout = QVBoxLayout()
        self.autoUpdateLayoutInner = QVBoxLayout()

        self.autoUpdateLayoutInner.addLayout(self.autoUpdateLabelOneLayout)
        self.autoUpdateLayoutInner.addLayout(self.autoUpdateLabelTwoLayout)

        self.autoUpdateLayout.addLayout(self.autoUpdateLabelLayout)
        self.autoUpdateLayout.addLayout(self.autoUpdateLayoutInner)

        self.autoUpdateLayout.setStretch(0, 1)
        self.autoUpdateLayout.setStretch(1, 1)
        self.autoUpdateLayout.setSpacing(0)

        self.libraryLayout = QVBoxLayout()
        self.libraryLayout.addLayout(self.libraryLabelLayout)
        self.libraryLayout.addLayout(self.autoUpdateLayout)


        #---------------------------------------------------
        self.readerLabel = QLabel("Reader")
        self.readerLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.readerLabel.setSizePolicy(self.sizePolicy)

        self.readerLabelFont = QFont()
        self.readerLabelFont.setBold(True)
        self.readerLabelFont.setPointSize(self.fontSize1)

        self.readerLabel.setFont(self.readerLabelFont)

        
        self.readerLabelLayout = QVBoxLayout()
        self.readerLabelLayout.addWidget(self.readerLabel)

        #------------------------
        self.readingModeLabel = QLabel("Default Reading Mode")
        self.readingModeLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.readingModeLabel.setSizePolicy(self.sizePolicy)
        self.readingModeLabelFont = QFont()
        self.readingModeLabelFont.setPointSize(self.fontSize2)
        self.readingModeLabel.setFont(self.readingModeLabelFont)

        self.readingModeLabelLayout = QVBoxLayout()
        self.readingModeLabelLayout.addWidget(self.readingModeLabel)

        #------------------------

        self.radioButtonOne = QRadioButton("Left-to-Right")
        self.radioButtonOne.setSizePolicy(self.sizePolicy)

        self.radioButtonTwo = QRadioButton("Webtoon/Vertical")
        self.radioButtonTwo.setSizePolicy(self.sizePolicy)
        
        self.radioButtonThree = QRadioButton("Right-to-Left")
        self.radioButtonThree.setSizePolicy(self.sizePolicy)

        self.radioButtonOne.setStyleSheet("QRadioButton {font-size: 12pt;} QRadioButton::indicator { width: 30px; height: 30px;}")
        self.radioButtonOne.adjustSize()
        self.radioButtonTwo.setStyleSheet("QRadioButton {font-size: 12pt;} QRadioButton::indicator { width: 30px; height: 30px;}")
        self.radioButtonTwo.adjustSize()
        self.radioButtonThree.setStyleSheet("QRadioButton {font-size: 12pt;} QRadioButton::indicator { width: 30px; height: 30px;}")
        self.radioButtonThree.adjustSize()

        self.radioButtonLayout = QVBoxLayout()

        
        self.radioButtonLayout.addWidget(self.radioButtonOne)
        self.radioButtonLayout.addWidget(self.radioButtonTwo)
        self.radioButtonLayout.addWidget(self.radioButtonThree)
        #------------------

        self.radioButtonLayout.setStretch(0, 1)
        self.radioButtonLayout.setStretch(1, 1)
        self.radioButtonLayout.setStretch(2, 1)
        self.radioButtonLayout.setSpacing(0)

        self.radioButtonLayout.setContentsMargins(45, 0, 0, 0)


        self.readerChoiceInnerLayout = QVBoxLayout()

        self.readerChoiceInnerLayout.addLayout(self.readingModeLabelLayout)
        self.readerChoiceInnerLayout.addLayout(self.radioButtonLayout)

        self.readerChoiceInnerLayout.setStretch(0, 1)
        self.readerChoiceInnerLayout.setStretch(1, 1)


        self.readerLayout = QVBoxLayout()
        self.readerLayout.addLayout(self.readerLabelLayout)
        self.readerLayout.addLayout(self.readerChoiceInnerLayout)

        #----------------------------------------------

        self.readerNavLabel = QLabel("Show/Hide Page Navigation")
        self.readerNavLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.readerNavLabel.setSizePolicy(self.sizePolicy)
        self.readerNavLabelFont = QFont()
        self.readerNavLabelFont.setPointSize(self.fontSize2)
        self.readerNavLabel.setFont(self.readerNavLabelFont)

        self.readerNavtoggle = ToggleSwitch()
        self.readerNavtoggle.setSizePolicy(self.sizePolicy)

        self.readerNavLayout = QHBoxLayout()

        self.readerNavLayout.addWidget(self.readerNavLabel)
        self.readerNavLayout.addWidget(self.readerNavtoggle)


        #----------------------------------------------

        self.readerFSLabel = QLabel("Open reader in fullscreen")
        self.readerFSLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.readerFSLabel.setSizePolicy(self.sizePolicy)
        self.readerFSLabelFont = QFont()
        self.readerFSLabelFont.setPointSize(self.fontSize2)
        self.readerFSLabel.setFont(self.readerFSLabelFont)

        self.readerFStoggle = ToggleSwitch()
        self.readerFStoggle.setSizePolicy(self.sizePolicy)

        self.readerFSLayout = QHBoxLayout()

        self.readerFSLayout.addWidget(self.readerFSLabel)
        self.readerFSLayout.addWidget(self.readerFStoggle)

        #----------------------------------------------
    
        self.spaceEaterForSettings = QWidget()
        self.spaceEaterForSettings.setSizePolicy(self.sizePolicy)
        # self.spaceEaterForLayout = QVBoxLayout()
        # self.spaceEaterForLayout.addWidget(self.spaceEaterForSettings)
    
        self.settingsLayout = QVBoxLayout()
        
        self.settingsLayout.addLayout(self.libraryLayout)
        self.settingsLayout.addLayout(self.readerLayout)
        self.settingsLayout.addLayout(self.readerNavLayout)
        self.settingsLayout.addLayout(self.readerFSLayout)
        self.settingsLayout.addWidget(self.spaceEaterForSettings)

        self.settingsLayout.setStretch(0, 1)
        self.settingsLayout.setStretch(1, 1)
        self.settingsLayout.setStretch(2, 1)
        self.settingsLayout.setStretch(3, 1)
        self.settingsLayout.setStretch(4, 7)
        self.settingsLayout.setSpacing(0)

        

    def downloadWidgetObj(self):
        self.dowBut = QLabel("Downloads")
        self.downloadsLayout.addWidget(self.dowBut)
        pass

    def themesWidgetObj(self):
        self.theBut = QLabel("Themes")
        self.themesLayout.addWidget(self.theBut)
        pass



