from PyQt6.QtWidgets import (
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
from PyQt6.QtGui import QCursor, QIcon, QPixmap
from PyQt6.QtCore import QSize, Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.max_button_size = QSize(50, 50)
        self.min_button_size = QSize(16, 16)
        self.icon_size = QSize(35, 35)

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
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
        sizePolicy.setHeightForWidth(self.menuButton.sizePolicy().hasHeightForWidth())
        self.menuButton.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(0, 50))
        self.lineEdit.setMaximumSize(QSize(1366, 50))
        self.lineEdit.setMaxLength(36)
        self.lineEdit.setClearButtonEnabled(True)
     
        # Search Button
        self.searchButton = QPushButton()
        self.searchButton.setCheckable(True)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.localSearchButton.sizePolicy().hasHeightForWidth())
        self.localSearchButton.setSizePolicy(sizePolicy)
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

        self.menuButton.clicked.connect(self.changeStackIndex)

        #-----------------------------------------------

    def changeStackIndex(self):
        stackIndex = 2
        return stackIndex

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
        

    def create_library_widgets(self):
        pass
     
            
    def create_stack_widget_home(self):
        #create_home_widgets()
        pass


    def create_stack_widget_library(self):
        #create_library_widgets()
        pass

    def search(self):
        self.keyword = self.lineEdit.text()
        if self.keyword != "":
            print(self.keyword)
