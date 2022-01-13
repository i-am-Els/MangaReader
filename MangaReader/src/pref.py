from PyQt6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QLabel,
    QSizePolicy,
    QStackedWidget,
    QPushButton,
)
from PyQt6.QtGui import QCursor, QIcon, QPixmap, QFont
from PyQt6.QtCore import QSize, Qt


class Preference(QWidget):
    def __init__(self):
        super().__init__()

        self.max_button_size = QSize(50, 50)
        self.min_button_size = QSize(16, 16)
        self.icon_size = QSize(35, 35)

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        #-----------------------------------------------
        # Create baseLayout
        self.baseLayout = QVBoxLayout()        

        #-----------------------------------------------
        # Create an horizontal headerLayout
        self.headerLayout = QHBoxLayout()
        self.bodyLayout = QHBoxLayout()

        #-----------------------------------------------
        # Create a backButton
        self.backButton = QPushButton()

        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setMaximumSize(self.max_button_size)

        # Set backIcon to backButton
        backIcon = QIcon()
        backIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-go-back-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.backButton.setIcon(backIcon)
        self.backButton.setIconSize(self.icon_size)
        self.backButton.setCheckable(True)
        self.backButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        

        #-----------------------------------------------
        self.headerLabel = QLabel()
        self.headerLabel.setSizePolicy(sizePolicy)
        headerLabelFont = QFont()
        headerLabelFont.setPointSize(24)
        headerLabelFont.setBold(True)
        self.headerLabel.setFont(headerLabelFont)
        self.headerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #-----------------------------------------------
        self.headerLayout.addWidget(self.backButton)
        self.headerLayout.addWidget(self.headerLabel)

        self.headerLayout.setStretch(1, 12)
        #-----------------------------------------------
        self.buttonsLayout = QVBoxLayout()
        self.buttonsLayout.setSpacing(3)

        self.settingsButton = QPushButton("Settings")
        self.settingsButton.setSizePolicy(sizePolicy)

        self.downloadButton = QPushButton("Downloads")
        self.downloadButton.setSizePolicy(sizePolicy)

        self.themesButton = QPushButton("Themes")
        self.themesButton.setSizePolicy(sizePolicy)

        self.buttonsLayout.addWidget(self.settingsButton)
        self.buttonsLayout.addWidget(self.downloadButton)
        self.buttonsLayout.addWidget(self.themesButton)

        #-----------------------------------------------
        self.stackLayout = QVBoxLayout()
        self.stackedWidget = QStackedWidget()

        self.settingsWidget = QWidget()
        self.downloadsWidget = QWidget()
        self.themesWidget = QWidget()

        self.stackedWidget.addWidget(self.settingsWidget)
        self.stackedWidget.addWidget(self.downloadsWidget)
        self.stackedWidget.addWidget(self.themesWidget)

        self.stackedWidget.setCurrentIndex(0)

        #---------------------------------------------------
        self.stackLayout.addWidget(self.stackedWidget)

        #-----------------------------------------------
        self.bodyLayout.addLayout(self.buttonsLayout)
        self.bodyLayout.addLayout(self.stackLayout)
        self.bodyLayout.setStretch(0, 1)
        self.bodyLayout.setStretch(1, 4)
        #-----------------------------------------------
        self.baseLayout.addLayout(self.headerLayout)
        self.baseLayout.addLayout(self.bodyLayout)

        self.baseLayout.setStretch(0, 1)
        self.baseLayout.setStretch(1, 10)
        #-----------------------------------------------

        self.backButton.clicked.connect(self.changeStackIndex)

        self.setLayout(self.baseLayout)

    def changeStackIndex(self):
        stackIndex = 0
        return stackIndex

        