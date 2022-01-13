import sys
from PyQt6.QtWidgets import (
    QApplication,
    QStackedWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QTabWidget,
    QWidget,
    QLineEdit,
    QLabel,
    QSizePolicy,
    QListView,
    QPushButton,
)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QCursor, QIcon, QPixmap, QFont

"""
from mainWindow import MainWindow 
from pref import Preference
from reader import Reader
"""

class Link(object):

    def talkToStackWidgetIndex(w_index, obj):
        print("talk")
        obj.changeStackIndex(obj, w_index)


class MainWindow(QWidget, Link):
    def __init__(self):
        super().__init__()

        self.max_button_size = QSize(50, 50)
        self.min_button_size = QSize(16, 16)
        self.icon_size = QSize(35, 35)

        self.sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.create_widgets()

    def create_widgets(self):
        #------------------------------------------------
        self.gridLayout = QGridLayout()

        #------------------------------------------------
        # Create a centralLayout to hold all other layouts
        self.centralLayout = QVBoxLayout()
        self.centralLayout.setSpacing(9)

        #------------------------------------------------
        # Create an horizontal layout to hold all search functions
        self.searchLayout = QHBoxLayout()
        self.searchLayout.setContentsMargins(-1, 10, -1, 10)
        # Create search function widgets

        # Menu/Option button 
        self.menuButton = QPushButton()
        self.menuButton.setCheckable(True)
        
        self.menuButton.setSizePolicy(self.sizePolicy)
        self.menuButton.setMinimumSize(self.min_button_size)
        self.menuButton.setMaximumSize(self.max_button_size)
        self.menuButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        menuIcon = QIcon()
        menuIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-menu-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuButton.setIcon(menuIcon)
        self.menuButton.setIconSize(self.icon_size)

        # TextBox
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("Enter Search keyword here...")
        
        self.lineEdit.setSizePolicy(self.sizePolicy)
        self.lineEdit.setMinimumSize(QSize(0, 50))
        self.lineEdit.setMaximumSize(QSize(1366, 50))
        self.lineEdit.setMaxLength(36)
        self.lineEdit.setClearButtonEnabled(True)
     
        # Search Button
        self.searchButton = QPushButton()
        self.searchButton.setCheckable(True)
        
        self.searchButton.setSizePolicy(self.sizePolicy)
        self.searchButton.setMinimumSize(self.min_button_size)
        self.searchButton.setMaximumSize(self.max_button_size)
        self.searchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        searchIcon = QIcon()
        searchIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-search-90.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchButton.setIcon(searchIcon)
        self.searchButton.setIconSize(self.icon_size)

        # Local Search
        self.localSearchButton = QPushButton()
        self.localSearchButton.setCheckable(True)
        
        self.localSearchButton.setSizePolicy(self.sizePolicy)
        self.localSearchButton.setMinimumSize(self.min_button_size)
        self.localSearchButton.setMaximumSize(self.max_button_size)
        self.localSearchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        localSearchIcon = QIcon()
        localSearchIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-plus-math-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.localSearchButton.setIcon(localSearchIcon)
        self.localSearchButton.setIconSize(self.icon_size)

        # Add Widgets to searchLayout
        self.searchLayout.addWidget(self.menuButton)
        self.searchLayout.addWidget(self.lineEdit)
        self.searchLayout.addWidget(self.searchButton)
        self.searchLayout.addWidget(self.localSearchButton)
        self.searchLayout.setStretch(0, 1)
        self.searchLayout.setStretch(1, 7)
        self.searchLayout.setStretch(2, 1)
        self.searchLayout.setStretch(3, 1)

        #------------------------------------------------
        # Create another horizontal layout to hold objects of focus
        self.containerLayout = QHBoxLayout()
        # Create a Vetical layout to hold the tabwidget
        self.homeLayout = QVBoxLayout()
        self.create_home_widgets()

        # Create a vertical layout to hold the list of previously read manhuas
        self.historyLayout = QVBoxLayout()
        # Create widgets for the historyLayout
        self.historyLabel = QLabel()
        self.historyLabel.setText("Recent Manhua")
        self.historyLabel.setStyleSheet("background-color: rgb(145, 145, 145); font: 15px;")
        self.historyLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.historyListView = QListView()
        # Add widgets to the historyLayout

        self.historyLayout.addWidget(self.historyLabel)    
        self.historyLayout.addWidget(self.historyListView)    
        self.historyLayout.setSpacing(5)

        #------------------------------------------------
        # Add homeLayout and historyLayout to containerLayout
        self.containerLayout.addLayout(self.homeLayout)
        self.containerLayout.addLayout(self.historyLayout)

        # Set Layout Stretch policy
        self.containerLayout.setStretch(0, 7)
        self.containerLayout.setStretch(1, 3)
        #------------------------------------------------
        #Add searchLayout and containerLayout to centralLayout
        self.centralLayout.addLayout(self.searchLayout)
        self.centralLayout.addLayout(self.containerLayout)
        self.centralLayout.setStretch(0, 2)
        self.centralLayout.setStretch(1, 12)
        #------------------------------------------------
        self.gridLayout.addLayout(self.centralLayout, 0, 0, 1, 1)

        self.setLayout(self.gridLayout)

        #------------------------------------------------
    
        self.style = """
                QTabWidget{
                    border: 1px solid rgba(0,0,0,40);
                }
                QPushButton{
                    border-radius:25px;
                }
                QPushButton:hover {
                    background-color: rgba(0,0,0,40);
                    color: white;
                }
                QLineEdit{
                    border: 1px solid rgba(0,0,0,40);
                    border-radius: 25px;
                    padding-left: 25px;
                    font: 13px;
                }
                QStatusBar{
                    background-color: rgba(0,0,0,40);
                }
                QLabel{
                    padding: 10px;
                    border-radius: 10px;
                }
            """
        self.setStyleSheet(self.style)
        #-----------------------------------------------
        self.searchButton.clicked.connect(self.search)
        self.lineEdit.returnPressed.connect(self.searchButton.click)
        
        self.menuButton.clicked.connect(self.menuAction)

        #-----------------------------------------------


    def create_home_widgets(self):
        self.tabWidget = QTabWidget()
        
        self.home = QWidget()

        homeIcon = QIcon()
        homeIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-home-96.png"), QIcon.Mode.Normal, QIcon.State.Off)

        self.library = QWidget()
        libraryIcon = QIcon()
        libraryIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-library-96.png"), QIcon.Mode.Normal, QIcon.State.Off)        
        
        self.tabWidget.addTab(self.home, homeIcon, "Home")
        self.tabWidget.addTab(self.library, libraryIcon, "Library")

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        #self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setIconSize(QSize(64, 24))

        self.homeLayout.addWidget(self.tabWidget)


    def search(self):
        self.keyword = self.lineEdit.text()
        if self.keyword != "":
            print(self.keyword)

    def menuAction(self):
        Link.talkToStackWidgetIndex(2, Window)

    def changeStackIndex(self, w_index):
        window.setCurrentIndex(w_index)


class Preference(QWidget, Link):
    def __init__(self):
        super().__init__()

        self.max_button_size = QSize(50, 50)
        self.min_button_size = QSize(16, 16)
        self.icon_size = QSize(35, 35)

        self.sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

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

        self.backButton.setSizePolicy(self.sizePolicy)
        self.backButton.setMinimumSize(self.min_button_size)
        self.backButton.setMaximumSize(self.max_button_size)
        self.backButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Set backIcon to backButton
        backIcon = QIcon()
        backIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-go-back-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.backButton.setIcon(backIcon)
        self.backButton.setIconSize(self.icon_size)
        self.backButton.setCheckable(True)
        self.backButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) 

        #-----------------------------------------------
        self.headerLabel = QLabel()
        self.headerLabel.setSizePolicy(self.sizePolicy)
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
        self.settingsButton.setSizePolicy(self.sizePolicy)

        self.downloadButton = QPushButton("Downloads")
        self.downloadButton.setSizePolicy(self.sizePolicy)

        self.themesButton = QPushButton("Themes")
        self.themesButton.setSizePolicy(self.sizePolicy)

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


        self.setLayout(self.baseLayout)

        self.backButton.clicked.connect(self.backAction)

    def backAction(self):
        Link.talkToStackWidgetIndex(0, Window)

    def changeStackIndex(self, w_index):
        self.setCurrentIndex(w_index)


class Reader(QWidget, Link):
    def __init__(self):
        super().__init__()


class Window(QStackedWidget):
    def __init__(self):
        super().__init__()
        #self.screen_width = 1366
        #self.screen_height = 768
        self.min_screen_width = 915
        self.min_screen_height = 515
        self.resize_width = 1092
        self.resize_height = 614
        self.appWindowTitle = "Manhua Reader"
        self.resize(QSize(self.resize_width, self.resize_height))
        self.setMinimumSize(QSize(self.min_screen_width, self.min_screen_height))
        self.setWindowTitle(self.appWindowTitle)
        
        self.objMainWindow = MainWindow()
        self.objReader = Reader()
        self.objPref = Preference()

        self.addWidget(self.objMainWindow)
        self.addWidget(self.objReader)
        self.addWidget(self.objPref)
        print(self.count())

    def changeStackIndex(self, w_index):
        window.setCurrentIndex(w_index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.showMaximized()
    sys.exit(app.exec())