# from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import  QIcon, QPixmap, QFont

class Themes(object):
    def __init__(self) -> None:
        pass
    def lightMode(obj):
        style ="""
        *{
            color: Black;
            background-color: rgb(250,250,250);
        }
        QPushButton{
            border-radius:18px;
        }
        QPushButton:hover {
            background-color: rgb(147,148,165);
        }
        QLineEdit{
            border: 1px solid rgba(0,0,0,40);
            border-radius: 18px;
            padding-left: 15px;
            font: 13px;
        }
        QStatusBar{
            background-color: rgba(0,0,0,40);
        }
        QLabel{
            padding: 10px;
            border-radius: 10px;
        }

        #toggleGridView:hover, #toggleListView:hover{
            background-color: rgb(147,148,165);;
            border-radius: 5px;
        }

        QTabWidget::pane{
            border: 0px;
        }

        #historyLabel{
            color: white;
            background-color: rgb(72,75,106); 
            font: 15px;
        }
        """

        obj.setStyleSheet(style)

        objM = obj.objMainWindow
        objM.tabBar.setStyleSheet("QTabBar::tab  { background: rgb(250,250,250); width: 200px; border-radius: 3px; padding: 3px;} QTabBar::tab:bottom:selected  {       background-color: rgb(72,75,106); color: rgb(250,250,250); } ")

        
        objM.menuIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-menu-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        objM.menuButton.setIcon(objM.menuIcon)

        objM.searchIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-search-90.png"), QIcon.Mode.Normal, QIcon.State.Off)
        objM.searchButton.setIcon(objM.searchIcon)

        objM.localSearchIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-add-folder-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        objM.localSearchButton.setIcon(objM.localSearchIcon)

        objM.localSearchIconSingleFormat.addPixmap(QPixmap("MangaReader/resources/icons/icons8-cbr-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        objM.localSearchButtonSingleFormat.setIcon(objM.localSearchIconSingleFormat)
        
        objM.refreshIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-refresh-90.png"), QIcon.Mode.Normal, QIcon.State.Off)
        objM.refreshButton.setIcon(objM.refreshIcon)

        
    
    def changeTabBarIconLight(obj):
        obj.tabIndex = obj.tabBar.currentIndex()
        print("Current Tab:", obj.tabIndex)
        print("Current Theme:", obj.themeIndex)
        if obj.tabIndex == 0:
            obj.homeIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-home-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            obj.tabBar.setTabIcon(obj.tabIndex, obj.homeIcon)

            obj.libraryIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-library-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            obj.tabBar.setTabIcon(1, obj.libraryIcon)
        else:
            obj.homeIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-home-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            obj.tabBar.setTabIcon(0, obj.homeIcon)

            obj.libraryIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-library-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            obj.tabBar.setTabIcon(obj.tabIndex, obj.libraryIcon)


    def darkMode():
        pass

    def changeTabBarIconDark(obj):
        pass


    def declareTheme(obj, themeIndex):
        if themeIndex == 0:
            obj.objMainWindow.themeIndex = themeIndex
            obj.objReader.themeIndex = themeIndex
            obj.objPref.themeIndex = themeIndex

        else:
            obj.objMainWindow.themeIndex = themeIndex
            obj.objReader.themeIndex = themeIndex
            obj.objPref.themeIndex = themeIndex