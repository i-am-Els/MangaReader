# Manhua Reader,  An application for reading manhuas and manhuas online and offline
# Copyright (C) 2022  Eniola Emmanuel Olawale

# This program is free software: you can redistribute it and/or modify
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pathlib import Path
import PyQt6

from PyQt6.QtCore import QPointF, Qt, QRect, QSize

from PyQt6.QtGui import QIcon, QPainter, QColor, QPen, QPixmap, QBrush, QCursor

from PyQt6.QtWidgets import QPushButton, QHBoxLayout, QLabel, QWidget, QSizePolicy, QVBoxLayout

class Themes:
    def __init__(self, obj):
        self.obj = obj        
        self.prevObjButton = 0;
        self.prefSelectedButtonIndex = 0
        self.prefButtonList = [self.obj.objPref.settingsButton, self.obj.objPref.downloadButton, self.obj.objPref.themesButton]

        self.defaultCoverImage = "resources/logo/thumbnailCoverless.png"
        self.defaultCoverPixmap = QPixmap(self.defaultCoverImage).scaled(60, 80, Qt.AspectRatioMode.KeepAspectRatio)
        # objP.spaceE.setPixmap(objP.pixPixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio))

    def prefButtonActiveLight(self, obj, indexB):
        if type(self.prevObjButton) == PyQt6.QtWidgets.QPushButton:
            self.prevObjButton.setStyleSheet(
                "QPushButton { color: Black; border-radius: 15px;background-color: rgb(250,250,250);} QPushButton:hover { color:white; background-color:rgb(210,211,219);} #backButton:hover{ background-color:rgb(147,148,165); border-radius: 18px}"
            )
        else:
            pass

        obj.setStyleSheet(
            "QPushButton { color: Black; border-radius: 15px;} QPushButton:hover{ color:white;background-color:rgb(210,211,219);}#backButton:hover{ background-color:rgb(147,148,165); border-radius: 18px}"
        )
        self.prefButtonList[indexB].setStyleSheet(
            "QPushButton { color:white;background-color:rgb(147,148,165); } #backButton:hover{ background-color:rgb(147,148,165); border-radius: 18px}"
        )

        self.prevObjButton = self.prefButtonList[indexB]

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
        
        objM.tabWidget.tabBar().setStyleSheet("QTabBar::tab { background-color: rgb(250, 250, 250); width: 200px; padding: 1px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px; }  QTabBar::tab:bottom{ background: rgb(235, 235, 235);}  QTabBar::tab:bottom:selected { background-color: rgb(72,75,106); color: rgb(250,250,250);}")

        objM.tabWidget.setStyleSheet("QTabWidget::pane { background: rgb(210, 211, 219); border: 1px solid rgb(210, 211, 219); border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;} ")

        objM.homeTabStack.setStyleSheet("background-color: rgb(210, 211, 219); border: 1px solid rgb(210, 211, 219); border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;")

        objM.library.setStyleSheet("#libraryOrigin { background-color: rgb(210, 211, 219); border: 1px solid rgb(210, 211, 219); border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;} ")
        
        objM.library.noItems.setStyleSheet(" QWidget{ background-color: rgb(210, 211, 219); border: 1px solid rgb(210, 211, 219); border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;} QLabel { border: none; }")
        
        objM.library.descriptionPage.setStyleSheet("border: 2px solid rgb(210, 211, 219); border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px; ")

        objM.library.libraryShelf.setStyleSheet("background: rgb(210, 211, 219); border: 1px solid rgb(210, 211, 219); border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px; ")

        self.scrollbarStyleLight = "QScrollArea { background-color: rgb(210, 211, 219); border: 1px solid rgb(210, 211, 219); border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;} QScrollBar:vertical { width: 7px; background: white; border: none; margin: 0px 0px 0px 0px; border-radius: 3px;} QScrollBar::handle:vertical { background: rgb(128, 128, 128); min-height:0px; border-radius: 3px;} QScrollBar::add-line:vertical { background: qlineargradient(x1:0; y1:0, x2:1, y2:0, stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop: 1 rgb(32, 47, 130)); height: 0px; subcontrol-position: bottom; subcontrol-origin: margin; } QScrollBar::sub-line:vertical {  background: qlineargradient(x1:0; y1:0, x2:1, y2:0, stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop: 1 rgb(32, 47, 130)); height: 0px; subcontrol-position: top; subcontrol-origin: margin; }"

        objM.library.libraryScrollArea.setStyleSheet(self.scrollbarStyleLight)

        # objM.library.libraryScrollAreaWidget.setStyleSheet("QSCrollArea{ border: 1px solid rgb(210, 211, 219); border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px; } ")

        objM.apiButton.setStyleSheet("QPushButton{ border-radius: 18px;}")
        
        objM.menuIcon.addPixmap(QPixmap("resources/icons/icons8-menu-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        objM.menuButton.setIcon(objM.menuIcon)

        objM.searchIcon.addPixmap(QPixmap("resources/icons/icons8-search-90.png"), QIcon.Mode.Normal, QIcon.State.Off)
        objM.searchButton.setIcon(objM.searchIcon)

        objM.localSearchIcon.addPixmap(QPixmap("resources/icons/icons8-add-folder-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        objM.localSearchButton.setIcon(objM.localSearchIcon)

        objM.localSearchIconSingleFormat.addPixmap(QPixmap("resources/icons/icons8-cbr-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        objM.localSearchButtonSingleFormat.setIcon(objM.localSearchIconSingleFormat)

        objM.library.descriptionPage.sideAInnerABackBtnIcon.addPixmap(QPixmap("resources/icons/icons8-go-back-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        objM.library.descriptionPage.sideAInnerABackBtn.setIcon(objM.library.descriptionPage.sideAInnerABackBtnIcon)
        
        objM.library.descriptionPage.sideAInnerABackBtn.setStyleSheet("QPushButton:hover{ background-color: rgb(210, 211, 219); border-radius: 18px;}")
        
        objM.refreshIcon.addPixmap(QPixmap("resources/icons/icons8-refresh-90.png"), QIcon.Mode.Normal, QIcon.State.Off)
        objM.refreshButton.setIcon(objM.refreshIcon)

        objM.apiButtonWidget.setStyleSheet("#apiWidget { background-color: rgb(210, 211, 219); border: 2px solid rgb(72,75,106); border-radius: 18px;} QPushButton{ background-color: rgb(210, 211, 219); margin: 5px;} QPushButton:hover{ background-color: rgb(210, 211, 219);}")

        objM.apiCombo.setStyleSheet(" QComboBox{  border: 0px; background-color: rgb(210, 211, 219);} QComboBox::drop-down{ border: 0px; width: 70px;} QComboBox:selected{ background-color: white;}")

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
        
        objP.headerBackgroundWidget.setMaximumHeight(60)
        objP.headerBackgroundWidget.setStyleSheet("background-color: rgb(147, 148, 165); border-radius: 25px; color: white; padding-top: 0px;")
        
        objP.backIcon.addPixmap(QPixmap("resources/icons/icons8-go-back-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        objP.backButton.setIcon(objP.backIcon)
        
        objP.backButton.setStyleSheet("QPushButton:hover{ background-color: rgb(210, 211, 219); border-radius: 18px;}")

        objP.radioButtonOne.setStyleSheet("QRadioButton::indicator { width: 20px; height: 20px;}")

        objP.radioButtonTwo.setStyleSheet("QRadioButton::indicator { width: 20px; height: 20px; }")

        objP.radioButtonThree.setStyleSheet("QRadioButton::indicator { width: 20px; height: 20px;}")

        objP.downloadQueue.setStyleSheet("background-color: white;")


        # objP.spaceE.setPixmap(QPixmap("resources/icons/lightModeTheme.png"))


        objP.downloadDirPathBtn.setStyleSheet("background: rgb(147, 148, 165); margin-top: 5px; margin-right: 5px; color: white;")
        objP.downloadDirPathBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        objP.pixPixmap = QPixmap("resources/icons/lightModeTheme.png")
        objP.spaceE.setPixmap(objP.pixPixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio))

        self.prefButtonActiveLight(objP, self.prefSelectedButtonIndex)
    
    def changeTabBarIconLight(obj):
        obj.tabIndex = obj.tabWidget.currentIndex()
        if obj.tabIndex == 0:
            obj.homeIcon.addPixmap(QPixmap("resources/icons/icons8-home-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            obj.tabWidget.setTabIcon(obj.tabIndex, obj.homeIcon)

            obj.libraryIcon.addPixmap(QPixmap("resources/icons/icons8-library-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            obj.tabWidget.setTabIcon(1, obj.libraryIcon)
        else:
            obj.homeIcon.addPixmap(QPixmap("resources/icons/icons8-home-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            obj.tabWidget.setTabIcon(0, obj.homeIcon)

            obj.libraryIcon.addPixmap(QPixmap("resources/icons/icons8-library-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            obj.tabWidget.setTabIcon(obj.tabIndex, obj.libraryIcon)

    def prefButtonActiveDark(self, obj, indexB):
        pass

    def darkMode(self, obj):
        objM = obj.objMainWindow
        objP = obj.objPref
        objR = obj.objReader

        objP.pixPixmap = QPixmap("resources/icons/darkModeTheme.png")
        objP.spaceE.setPixmap(objP.pixPixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio))

    def changeTabBarIconDark(obj):
        pass

    def prefButtonActive(self, indexB, themeIndex):
        self.prefSelectedButtonIndex = indexB
        if themeIndex == 0:
            self.prefButtonActiveLight(self.obj.objPref, indexB)
        else:
            self.prefButtonActiveDark(self.obj.objPref, indexB)

    def declareTheme(self, obj, themeIndex):
        if themeIndex == 0:
            obj.objMainWindow.themeIndex = themeIndex
            obj.objReader.themeIndex = themeIndex
            obj.objPref.themeIndex = themeIndex
            obj.setting.themeIndex = themeIndex
            obj.setting.themeButtonState = False

        else:
            obj.objMainWindow.themeIndex = themeIndex
            obj.objReader.themeIndex = themeIndex
            obj.objPref.themeIndex = themeIndex
            obj.setting.themeIndex = themeIndex
            obj.setting.themeButtonState = True

        # obj.objMainWindow.themeObj = themeObj
        # obj.objReader.themeObj = themeObj
        # obj.objPref.themeObj = themeObj
        

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
    def __init__(self, obj, widgetTitle, widget):
        super().__init__()
        
        self.obj = obj
        self.widgetTitle = widgetTitle
        self.widget = widget # StsckedWidgetWindow or stWindow
        self.widgetIcon = widget.windowIcon
        self.widgetMainW = self.widget.objMainWindow
        self.widgetLibrary = self.widget.objMainWindow.library
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
        self.minimizeIconIcon.addPixmap(QPixmap("resources/icons/icons8-minimize-dark-90.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeIcon.setIcon(self.minimizeIconIcon)

        self.minimizeIcon.setStyleSheet("QPushButton{background-color: rgba(72, 75, 106, 0.8); border: none;} QPushButton:hover{ background-color: rgb(210, 211, 219); }")


        self.restoreIcon.setMaximumSize(iconsizew, iconsize)

        self.restoreIconIcon = QIcon()
        self.restoreIconIcon.addPixmap(QPixmap("resources/icons/icons8-restore-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.restoreIcon.setIcon(self.restoreIconIcon)

        self.restoreIcon.setStyleSheet("QPushButton{background-color: rgba(72, 75, 106, 0.8); border: none;} QPushButton:hover{ background-color: rgb(210, 211, 219);}")

        self.closeIcon.setMaximumSize(iconsizew, iconsize)

        self.closeIconIcon = QIcon()
        self.closeIconIcon.addPixmap(QPixmap("resources/icons/icons8-close-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
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
            if self.widgetMainW.viewIsGrid:
                self.widgetLibrary.libraryResized()
            
            self.restoreIconIcon.addPixmap(QPixmap("resources/icons/icons8-maximize-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.restoreIcon.setIcon(self.restoreIconIcon)

        else:
            self.obj.showMaximized()
            self.obj.setWindowState(Qt.WindowState.WindowMaximized)
            if self.widgetMainW.viewIsGrid:
                self.widgetLibrary.libraryMaximized()

            self.restoreIconIcon.addPixmap(QPixmap("resources/icons/icons8-restore-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.restoreIcon.setIcon(self.restoreIconIcon)

class MoveableWindow(QWidget):
    def __init__(self, obj, widget):
        super().__init__()
        self.refIcon = QPushButton()
        self.refIconIcon = QIcon()
        self.obj = obj
        self.obj.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.widget = widget # StsckedWidgetWindow or stWindow
        self.widgetMainW = self.widget.objMainWindow
        self.widgetLibrary = self.widget.objMainWindow.library
        
        self.oldPosition = self.pos()

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPosition()

    def mouseDoubleClickEvent(self, event):
        
        self.oldPosition = event.globalPosition()
        if self.obj.windowState() == Qt.WindowState.WindowMaximized or self.obj.windowState() == Qt.WindowState.WindowFullScreen:
            self.obj.setWindowState(Qt.WindowState.WindowNoState)
            # self.obj.resize(QSize(1092, 614))
            self.obj.setGeometry(200, 0, 1092, 614)
            if self.widgetMainW.viewIsGrid:
                self.widgetLibrary.libraryResized()

            self.refIconIcon.addPixmap(QPixmap("resources/icons/icons8-maximize-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.refIcon.setIcon(self.refIconIcon)

        elif self.obj.windowState() == Qt.WindowState.WindowNoState or self.obj.windowState() == Qt.WindowState.WindowActive:
            self.obj.showMaximized()
            self.obj.setWindowState(Qt.WindowState.WindowMaximized)
            if self.widgetMainW.viewIsGrid:
                self.widgetLibrary.libraryMaximized()

            self.refIconIcon.addPixmap(QPixmap("resources/icons/icons8-restore-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.refIcon.setIcon(self.refIconIcon)

    def mouseMoveEvent(self, event):
        delta = QPointF(event.globalPosition() - self.oldPosition)
        self.obj.move(self.obj.x() + delta.x(), self.obj.y() + delta.y())
        

        self.obj.resize(QSize(1092, 614))
        self.obj.setWindowState(Qt.WindowState.WindowActive)
        if self.widgetMainW.viewIsGrid:
            self.widgetLibrary.libraryResized()

        self.refIconIcon.addPixmap(QPixmap("resources/icons/icons8-maximize-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.refIcon.setIcon(self.refIconIcon)

        self.oldPosition = event.globalPosition()
         