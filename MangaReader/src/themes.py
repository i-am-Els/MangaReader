# from PyQt6.QtCore import QSize, Qt
import PyQt6

from PyQt6.QtCore import QPointF, Qt, QRect, QSize

from PyQt6.QtGui import QIcon, QPainter, QColor, QPen, QPixmap, QBrush

from PyQt6.QtWidgets import QPushButton, QHBoxLayout, QLabel, QWidget, QSizePolicy, QVBoxLayout


class Themes:
    def __init__(self, obj):
        self.obj = obj        
        self.prevObjButton = 0;

    def prefButtonActiveLight(self, obj, objButton):
        if type(self.prevObjButton) == PyQt6.QtWidgets.QPushButton:
            self.prevObjButton.setStyleSheet(
                "QPushButton { color: Black; border-radius: 15px;background-color: rgb(250,250,250);} QPushButton:hover { color:white; background-color:rgb(210,211,219);} #backButton:hover{ background-color:rgb(147,148,165); border-radius: 18px}"
            )
        else:
            pass

        obj.setStyleSheet(
            "QPushButton { color: Black; border-radius: 15px;} QPushButton:hover{ color:white;background-color:rgb(210,211,219);}#backButton:hover{ background-color:rgb(147,148,165); border-radius: 18px}"
        )
        objButton.setStyleSheet(
            "QPushButton { color:white;background-color:rgb(147,148,165); } #backButton:hover{ background-color:rgb(147,148,165); border-radius: 18px}"
        )

        self.prevObjButton = objButton


    def lightMode(self, obj):
        style ="""
        *{
            color: Black;
            background-color: rgb(250,250,250);
        }
        QPushButton{
            border-radius: 18px;
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
        QListView{
            background-color: rgb(210, 211, 219);
            border: 1px solid rgb(210, 211, 219);
            border-radius: 10px;
        }
        """

        obj.setStyleSheet(style)

        objM = obj.objMainWindow
        objP = obj.objPref
        objR = obj.objReader
        
        objM.tabBar.setStyleSheet("QTabBar::tab  { background: rgb(250,250,250); width: 200px; border-radius: 3px; padding: 3px;} QTabBar::tab:bottom:selected  {       background-color: rgb(72,75,106); color: rgb(250,250,250); } ")

        objM.tabWidget.setStyleSheet("background-color: rgb(210, 211, 219); border: 1px solid rgb(210, 211, 219); border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;")

        
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

        objP.style = """   
            #settingsButton, #downloadButton, #themesButton{
                border-radius: 15px;
            }
            #settingsButton:hover, #downloadButton:hover, #themesButton:hover{
                color:white;
                background-color:rgb(210,211,219);
            }
            
        """
        objP.setStyleSheet(objP.style)

        objP.headerLabel.setMaximumHeight(48)
        
        objP.stackedWidget.setStyleSheet("background-color: rgb(210,211,219); border-radius: 10px;")
        
        objP.headerBackgroundWidget.setMaximumHeight(65)
        objP.headerBackgroundWidget.setStyleSheet("background-color: rgb(147, 148, 165); border-radius: 25px; color: white; padding-top: 0px;")
        
        objP.backIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-go-back-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        objP.backButton.setIcon(objP.backIcon)
        
        objP.backButton.setStyleSheet("QPushButton:hover{ background-color: rgb(210, 211, 219); border-radius: 18px;}")

        objP.radioButtonOne.setStyleSheet("QRadioButton::indicator { width: 30px; height: 30px;}")

        objP.radioButtonTwo.setStyleSheet("QRadioButton::indicator { width: 30px; height: 30px; }")

        objP.radioButtonThree.setStyleSheet("QRadioButton::indicator { width: 30px; height: 30px;}")

        objP.downloadQueue.setStyleSheet("background-color: white;")


        # objP.spaceE.setPixmap(QPixmap("MangaReader/resources/icons/lightModeTheme.png"))


        objP.compressArchiveBtn.setStyleSheet("background: rgb(147, 148, 165); margin-top: 5px; margin-right: 5px;")

        self.prefButtonActiveLight(objP, objP.settingsButton)
    
    def changeTabBarIconLight(obj):
        obj.tabIndex = obj.tabBar.currentIndex()
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



#-------------------------------------------------------

    def prefButtonActiveDark(obj, objButton):
        pass

    def darkMode():
        pass

    def changeTabBarIconDark(obj):
        pass


    def declareTheme(self, obj, themeIndex, themeObj):
        if themeIndex == 0:
            obj.objMainWindow.themeIndex = themeIndex
            obj.objReader.themeIndex = themeIndex
            obj.objPref.themeIndex = themeIndex

        else:
            obj.objMainWindow.themeIndex = themeIndex
            obj.objReader.themeIndex = themeIndex
            obj.objPref.themeIndex = themeIndex

        obj.objMainWindow.themeObj = themeObj
        obj.objReader.themeObj = themeObj
        obj.objPref.themeObj = themeObj
        

class ToggleSwitch(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setCheckable(True)
        self.setMinimumWidth(66)
        self.setMinimumHeight(22)

    def paintEvent(self, event):
        label = "on" if self.isChecked() else "off"
        bg_color = QColor(72, 75, 106) if self.isChecked() else QColor(147, 148, 165)

        radius = 10
        width = 24
        center = self.rect().center()

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.translate(center)
        painter.setBrush(QColor(250, 250, 250))

        pen = QPen(Qt.GlobalColor.white)
        pen.setWidth(2)
        painter.setPen(pen)

        painter.drawRoundedRect(QRect(-width, -radius, 2*width, 2*radius), radius, radius)
        painter.setBrush(QBrush(bg_color))
        sw_rect = QRect(-radius, -radius, width + radius, 2*radius)
        if not self.isChecked():
            sw_rect.moveLeft(-width)
        painter.drawRoundedRect(sw_rect, radius, radius)
        painter.drawText(sw_rect, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop, label)



class WindowTitleBar(QHBoxLayout):
    def __init__(self, obj, widgetTitle, widgetIcon):
        super().__init__()
        
        self.obj = obj
        self.widgetTitle = widgetTitle
        self.widgetIcon = widgetIcon
        widIcon = 30
        iconsize = 30
        iconsizew = 48

        self.resize_width = 1092
        self.resize_height = 614

        self.sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # self.majorLayout = QHBoxLayout()
        self.logoLayout = QHBoxLayout()
        self.buttonsLayout = QHBoxLayout()
        self.sE = QWidget()
        self.sE.setMaximumHeight(30)
        self.sEL = QVBoxLayout()
        self.sEL.addWidget(self.sE)

        self.customWindowIcon = QPushButton()
        self.customWindowIcon.setIcon(self.widgetIcon)
        self.customWindowIcon.setIconSize(QSize(iconsize, iconsize))
        self.customWindowIcon.setCheckable(False)
        self.customWindowIcon.setMaximumSize(widIcon, widIcon)
        self.customWindowIcon.setStyleSheet("QPushButton { padding-left: 2px; border: none;}")

        self.customWindowTitle = QLabel(widgetTitle)
        self.customWindowTitle.setFixedHeight(30)
        self.customWindowTitle.setSizePolicy(self.sizePolicy)
        self.customWindowTitle.setStyleSheet("padding-left: 8px;")

        self.minimizeIcon = QPushButton()
        self.minimizeIcon.setSizePolicy(self.sizePolicy)
        self.minimizeIcon.setCheckable(True)

        self.restoreIcon = QPushButton()
        self.restoreIcon.setSizePolicy(self.sizePolicy)
        self.restoreIcon.setCheckable(True)

        self.closeIcon = QPushButton()
        self.closeIcon.setSizePolicy(self.sizePolicy)
        self.closeIcon.setCheckable(True)

        self.minimizeIcon.setMaximumSize(iconsizew, iconsize)

        self.minimizeIconIcon = QIcon()
        self.minimizeIconIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-minimize-dark-90.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeIcon.setIcon(self.minimizeIconIcon)

        self.minimizeIcon.setStyleSheet("QPushButton{background-color: rgba(72, 75, 106, 0.8); border: none;} QPushButton:hover{ background-color: rgb(210, 211, 219); }")


        self.restoreIcon.setMaximumSize(iconsizew, iconsize)

        self.restoreIconIcon = QIcon()
        self.restoreIconIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-restore-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.restoreIcon.setIcon(self.restoreIconIcon)

        self.restoreIcon.setStyleSheet("QPushButton{background-color: rgba(72, 75, 106, 0.8); border: none;} QPushButton:hover{ background-color: rgb(210, 211, 219);}")

        self.closeIcon.setMaximumSize(iconsizew, iconsize)

        self.closeIconIcon = QIcon()
        self.closeIconIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-close-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeIcon.setIcon(self.closeIconIcon)

        self.closeIcon.setStyleSheet("QPushButton{background-color: rgba(72, 75, 106, 0.8); border: none;} QPushButton:hover{ background-color: rgba(247,10,15,1);}")

        self.logoLayout.addWidget(self.customWindowIcon)
        self.logoLayout.addWidget(self.customWindowTitle)
        self.logoLayout.setSpacing(0)
        self.logoLayout.setContentsMargins(0,0,0,0)

        self.buttonsLayout.addWidget(self.minimizeIcon)
        self.buttonsLayout.addWidget(self.restoreIcon)
        self.buttonsLayout.addWidget(self.closeIcon)
        self.buttonsLayout.setSpacing(0)

        self.addLayout(self.logoLayout)
        self.addLayout(self.sEL)
        self.addLayout(self.buttonsLayout)
        self.setStretch(0, 1)
        self.setStretch(1, 7)
        self.setStretch(2, 1)
        self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)

        self.minimizeIcon.clicked.connect(lambda: self.obj.showMinimized())
        self.restoreIcon.clicked.connect(lambda: self.toggleRestore())
        self.closeIcon.clicked.connect(self.obj.close)

    def toggleRestore(self):
        if self.obj.windowState() == Qt.WindowState.WindowMaximized:
            self.obj.resize(QSize(self.resize_width, self.resize_height))
            self.obj.setWindowState(Qt.WindowState.WindowActive)
            
            self.restoreIconIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-maximize-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.restoreIcon.setIcon(self.restoreIconIcon)

        else:
            self.obj.showMaximized()
            self.obj.setWindowState(Qt.WindowState.WindowMaximized)

            self.restoreIconIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-restore-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.restoreIcon.setIcon(self.restoreIconIcon)

class MoveableWindow(QWidget):
    def __init__(self, obj):
        super().__init__()
        self.refIcon = QPushButton()
        self.refIconIcon = QIcon()
        self.obj = obj
        self.obj.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        
        self.obj.oldPosition = self.obj.pos()


    def mousePressEvent(self, event):
        self.obj.oldPosition = event.globalPosition()

    def mouseDoubleClickEvent(self, event):
        self.obj.oldPosition = event.globalPosition()
        if self.obj.windowState() == Qt.WindowState.WindowMaximized or self.obj.windowState() == Qt.WindowState.WindowFullScreen:
            self.obj.setWindowState(Qt.WindowState.WindowNoState)
            self.obj.resize(QSize(1092, 614))
            self.refIconIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-maximize-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.refIcon.setIcon(self.refIconIcon)

        elif self.obj.windowState() == Qt.WindowState.WindowNoState or self.obj.windowState() == Qt.WindowState.WindowActive:
            self.obj.showMaximized()
            self.obj.setWindowState(Qt.WindowState.WindowMaximized)

            self.refIconIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-restore-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.refIcon.setIcon(self.refIconIcon)

    def mouseMoveEvent(self, event):
        delta = QPointF(event.globalPosition() - self.obj.oldPosition)
        self.obj.move(self.obj.x() + delta.x(), self.obj.y() + delta.y())
        self.obj.oldPosition = event.globalPosition()

        self.obj.resize(QSize(1092, 614))
        self.obj.setWindowState(Qt.WindowState.WindowActive)

        self.refIconIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-maximize-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.refIcon.setIcon(self.refIconIcon)
        
  