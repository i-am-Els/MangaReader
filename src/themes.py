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


# from pathlib import Path

from PyQt6.QtCore import QPoint, QPointF, Qt, QRect, QSize

from PyQt6.QtGui import QIcon, QPainter, QColor, QPen, QPixmap, QBrush, QCursor, QGuiApplication, QPalette

from PyQt6.QtWidgets import QPushButton, QHBoxLayout, QLabel, QWidget, QSizePolicy, QVBoxLayout

import consts, resources, color
from linker import Link
from settings import Settings

class Themes:
    objM = object()
    objP = object()
    objR = object()
    prevObjButton = object()
    prefSelectedButtonIndex = 0
    prefButtonList = list()
    style = str()

    # self.Themes.objP.spaceE.setPixmap(self.Themes.objP.pixPixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio))
    scrollbarStyleLight = f"QScrollArea {{ background-color: {color.LIGHT_COLOR_3}; border: 1px solid {color.LIGHT_COLOR_3}; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;}} QScrollBar:vertical {{ width: 7px; background: white; border: none; margin: 0px 0px 0px 0px; border-radius: 3px;}} QScrollBar::handle:vertical {{ background: {color.LIGHT_COLOR_7}; min-height:0px; border-radius: 3px;}} QScrollBar::add-line:vertical {{ background: qlineargradient(x1:0; y1:0, x2:1, y2:0, stop: 0 {color.LIGHT_COLOR_8}, stop: 0.5 {color.LIGHT_COLOR_8}, stop: 1 {color.LIGHT_COLOR_8}); height: 0px; subcontrol-position: bottom; subcontrol-origin: margin; }} QScrollBar::sub-line:vertical {{  background: qlineargradient(x1:0; y1:0, x2:1, y2:0, stop: 0 {color.LIGHT_COLOR_8}, stop: 0.5 {color.LIGHT_COLOR_8}, stop: 1 {color.LIGHT_COLOR_8}); height: 0px; subcontrol-position: top; subcontrol-origin: margin; }}"

    def themeInit() -> None:
        Themes.objM = Link.typeTest(consts.OBJ_MW_NAME)
        Themes.objR = Link.typeTest(consts.OBJ_READER_NAME)
        Themes.objP = Link.typeTest(consts.OBJ_PREF_NAME)
        Themes.prefButtonList = [Themes.objP.settingsButton, Themes.objP.downloadButton, Themes.objP.themesButton]

    def prefButtonActiveLight(obj, indexB: int) -> None:
        if type(Themes.prevObjButton) == QPushButton:
            Themes.prevObjButton.setStyleSheet(f"QPushButton {{ color: Black; border-radius: 15px;background-color: {color.LIGHT_COLOR_1};}} QPushButton:hover {{ color:white; background-color: {color.LIGHT_COLOR_3};}} #backButton:hover{{ background-color:{color.LIGHT_COLOR_4}; border-radius: 18px}}")
        else:
            pass

        obj.setStyleSheet(f"QPushButton {{ color: Black; border-radius: 15px;}} .QPushButton:hover{{ color:white;background-color:{color.LIGHT_COLOR_3};}}#backButton:hover{{ background-color:{color.LIGHT_COLOR_4}; border-radius: 18px}}")

        Themes.prefButtonList[indexB].setStyleSheet(f"QPushButton {{ color:white;background-color:{color.LIGHT_COLOR_4}; }} #backButton:hover{{ background-color:{color.LIGHT_COLOR_4}; border-radius: 18px}}")

        for x in Themes.prefButtonList:
            if x != Themes.prefButtonList[indexB]:
                x.setStyleSheet(f"QPushButton {{ color: black; border-radius: 15px;}} .QPushButton:hover{{ color:white;background-color:{color.LIGHT_COLOR_3};}} #backButton:hover{{ background-color:{color.LIGHT_COLOR_4}; border-radius: 18px}}")

        Themes.objP.downloadDirPathBtn.setStyleSheet(f"QPushButton {{ color:white;background-color:{color.LIGHT_COLOR_4}; }} #backButton:hover{{ background-color:{color.LIGHT_COLOR_4}; border-radius: 18px}}")

        Themes.prevObjButton = Themes.prefButtonList[indexB]

    def prefButtonActiveDark(obj, indexB: int) -> None:
        if type(Themes.prevObjButton) == QPushButton:
            Themes.prevObjButton.setStyleSheet(f"QPushButton {{ color: white; border-radius: 15px;background-color: {color.DARK_COLOR_9};}} QPushButton:hover {{ color:gray; background-color: {color.DARK_COLOR_3};}} #backButton:hover{{ background-color:{color.DARK_COLOR_4}; border-radius: 18px}}")
        else:
            pass

        obj.setStyleSheet(f"QPushButton {{ color: gray; border-radius: 15px;}} .QPushButton:hover{{ color:gray;background-color:{color.DARK_COLOR_3};}} #backButton:hover{{ background-color:{color.DARK_COLOR_4}; border-radius: 18px}}")

        Themes.prefButtonList[indexB].setStyleSheet(f"QPushButton {{ color:white;background-color:{color.DARK_COLOR_4}; }} #backButton:hover{{ background-color:{color.DARK_COLOR_4}; border-radius: 18px}}")

        for x in Themes.prefButtonList:
            if x != Themes.prefButtonList[indexB]:
                x.setStyleSheet(f"QPushButton {{ color: gray; border-radius: 15px;}} .QPushButton:hover{{ color:gray;background-color:{color.DARK_COLOR_3};}} #backButton:hover{{ background-color:{color.DARK_COLOR_4}; border-radius: 18px}}")

        Themes.objP.downloadDirPathBtn.setStyleSheet(f"QPushButton {{ color:white;background-color:{color.DARK_COLOR_4}; }} #backButton:hover{{ background-color:{color.DARK_COLOR_4}; border-radius: 18px}}")

        Themes.prevObjButton = Themes.prefButtonList[indexB]

    def lightMode(obj) -> None:
        Themes.style = f"""
        *{{
            color: Black;
            background-color: {color.LIGHT_COLOR_1};
        }}
        QPushButton{{
            background-color: {color.LIGHT_COLOR_1};
            border-radius: 18px;
        }}
        QPushButton:hover {{
            background-color: {color.LIGHT_COLOR_4};
        }}
        QLineEdit{{
            border: 1px solid {color.LIGHT_COLOR_6};
            border-radius: 18px;
            padding-left: 15px;
            font: 13px;
        }}
        QLabel{{
            padding: 10px;
            border-radius: 10px;
        }}
        
        #toggleGridView:hover, #toggleListView:hover{{
            background-color: {color.LIGHT_COLOR_4};
            border-radius: 5px;
        }}
        
        #historyLabel{{
            color: white;
            background-color: {color.LIGHT_COLOR_5}; 
            font: 15px;
        }}
        #historyListView{{
            background-color: {color.LIGHT_COLOR_3};
        }}
        #historyScroll, scroll{{
            background-color: {color.LIGHT_COLOR_3};
            padding: 0px;
            margin: 0px;
        }}
        QToolTip{{
            background-color: {color.LIGHT_COLOR_4};
            color: {color.LIGHT_COLOR_2};
        }}
        """

        obj.setStyleSheet(Themes.style)
        
        Themes.objM.tabWidget.tabBar().setStyleSheet(f"QTabBar::tab {{ background-color: {color.LIGHT_COLOR_1}; width: 200px; padding: 0px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px; }}  QTabBar::tab:bottom{{ background: {color.LIGHT_COLOR_9};}}  QTabBar::tab:bottom:selected {{ background-color: {color.LIGHT_COLOR_5}; color: {color.LIGHT_COLOR_1};}}")

        Themes.objM.tabWidget.setStyleSheet(f"QTabWidget::pane {{ background: {color.LIGHT_COLOR_3}; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;}} ")

        Themes.objM.homeTabStack.setStyleSheet(f"background-color: {color.LIGHT_COLOR_3}; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;")

        Themes.objM.library.setStyleSheet(f" background: {color.LIGHT_COLOR_3}; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;")
        
        Themes.objM.library.noItems.setStyleSheet(f" QWidget{{ background: transparent; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;}} QLabel {{ border: none; }}")
        
        Themes.objM.library.descriptionPage.setStyleSheet(f"QWidget#descPage {{ background: transparent; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px; }} QPushButton:hover {{ background-color: {color.LIGHT_COLOR_4};}}")

        Themes.objM.library.libraryShelf.setStyleSheet(" background: transparent; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px; ")

        Themes.objM.library.libraryScrollArea.setStyleSheet(f"QScrollArea {{ background-color: transparent; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;}} QScrollBar:vertical {{ width: 7px; background: white; border: none; margin: 0px 0px 0px 0px; border-radius: 3px;}} QScrollBar::handle:vertical {{ background: {color.LIGHT_COLOR_7}; min-height:0px; border-radius: 3px;}} QScrollBar::add-line:vertical {{ background: qlineargradient(x1:0; y1:0, x2:1, y2:0, stop: 0 {color.LIGHT_COLOR_8}, stop: 0.5 {color.LIGHT_COLOR_8}, stop: 1 {color.LIGHT_COLOR_8}); height: 0px; subcontrol-position: bottom; subcontrol-origin: margin; }} QScrollBar::sub-line:vertical {{  background: qlineargradient(x1:0; y1:0, x2:1, y2:0, stop: 0 {color.LIGHT_COLOR_8}, stop: 0.5 {color.LIGHT_COLOR_8}, stop: 1 {color.LIGHT_COLOR_8}); height: 0px; subcontrol-position: top; subcontrol-origin: margin; }}")

        Themes.objM.library.descriptionPage.scrollArea.setStyleSheet(f"QScrollArea {{ background-color: transparent; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;}} QScrollBar:vertical {{ width: 7px; background: white; border: none; margin: 0px 0px 0px 0px; border-radius: 3px;}} QScrollBar::handle:vertical {{ background: {color.LIGHT_COLOR_7}; min-height:0px; border-radius: 3px;}} QScrollBar::add-line:vertical {{ background: qlineargradient(x1:0; y1:0, x2:1, y2:0, stop: 0 {color.LIGHT_COLOR_8}, stop: 0.5 {color.LIGHT_COLOR_8}, stop: 1 {color.LIGHT_COLOR_8}); height: 0px; subcontrol-position: bottom; subcontrol-origin: margin; }} QScrollBar::sub-line:vertical {{  background: qlineargradient(x1:0; y1:0, x2:1, y2:0, stop: 0 {color.LIGHT_COLOR_8}, stop: 0.5 {color.LIGHT_COLOR_8}, stop: 1 {color.LIGHT_COLOR_8}); height: 0px; subcontrol-position: top; subcontrol-origin: margin; }}  QPushButton:hover{{ background-color: {color.LIGHT_COLOR_4};}}")

        Themes.objM.scroll.setStyleSheet(f"QScrollArea {{ background-color: {color.LIGHT_COLOR_4}; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;}} QScrollBar:vertical {{ width: 7px; background: white; border: none; margin: 0px 0px 0px 0px; border-radius: 3px;}} QScrollBar::handle:vertical {{ background: {color.LIGHT_COLOR_7}; min-height:0px; border-radius: 3px;}} QScrollBar::add-line:vertical {{ background: qlineargradient(x1:0; y1:0, x2:1, y2:0, stop: 0 {color.LIGHT_COLOR_8}, stop: 0.5 {color.LIGHT_COLOR_8}, stop: 1 {color.LIGHT_COLOR_8}); height: 0px; subcontrol-position: bottom; subcontrol-origin: margin; }} QScrollBar::sub-line:vertical {{  background: qlineargradient(x1:0; y1:0, x2:1, y2:0, stop: 0 {color.LIGHT_COLOR_8}, stop: 0.5 {color.LIGHT_COLOR_8}, stop: 1 {color.LIGHT_COLOR_8}); height: 0px; subcontrol-position: top; subcontrol-origin: margin; }} QPushButton:hover{{ background-color: {color.DARK_COLOR_3};}}")

        Themes.objM.library.libraryScrollAreaWidget.setStyleSheet(f"background-color: transparent; border: 1px solid transparent; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px; ")

        Themes.objM.scrollW.setStyleSheet(f" QObject{{ background-color: transparent; color: white; border: 1px solid transparent; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;}} QPushButton{{background-color: {color.LIGHT_COLOR_6}; color: white; border-radius: 15px;}} QPushButton:hover{{background-color: {color.LIGHT_COLOR_5}; color: white; border-radius: 15px;}}")

        Themes.objM.historyListView.setStyleSheet(f"background-color: transparent; border: 1px solid transparent; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;")


        Themes.objM.library.descriptionPage.selectionWidget.setStyleSheet(f"QWidget {{ background-color: transparent;}} QToolTip{{ background-color: {color.DARK_COLOR_4}; color: {color.DARK_COLOR_2} }}")

        Themes.objM.apiButton.setStyleSheet("QPushButton{ border-radius: 18px;}")
        
        Themes.objM.menuIcon.addPixmap(QPixmap(resources.menu_icon), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objM.menuButton.setIcon(Themes.objM.menuIcon)

        Themes.objM.searchIcon.addPixmap(QPixmap(resources.search_icon), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objM.searchButton.setIcon(Themes.objM.searchIcon)

        Themes.objM.localSearchIcon.addPixmap(QPixmap(resources.local_search_icon), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objM.localSearchButton.setIcon(Themes.objM.localSearchIcon)

        Themes.objM.localSearchIconSingleFormat.addPixmap(QPixmap(resources.local_search_single_icon), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objM.localSearchButtonSingleFormat.setIcon(Themes.objM.localSearchIconSingleFormat)

        Themes.objM.library.descriptionPage.exitButtonIcon.addPixmap(QPixmap(resources.exit_button), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objM.library.descriptionPage.exitButton.setIcon(Themes.objM.library.descriptionPage.exitButtonIcon)
        
        Themes.objM.library.descriptionPage.exitButton.setStyleSheet(f"QPushButton:hover{{ background-color: {color.LIGHT_COLOR_4}; border-radius: 18px;}}")

        Themes.objM.library.descriptionPage.deleteButtonIcon.addPixmap(QPixmap(resources.delete_manhua), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objM.library.descriptionPage.deleteButton.setIcon(Themes.objM.library.descriptionPage.deleteButtonIcon)
        
        Themes.objM.library.descriptionPage.deleteButton.setStyleSheet(f"QPushButton:hover{{ background-color: {color.LIGHT_COLOR_4}; border-radius: 18px;}}")
        
        Themes.objM.refreshIcon.addPixmap(QPixmap(resources.refresh_icon), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objM.refreshButton.setIcon(Themes.objM.refreshIcon)

        Themes.objM.clearHistoryIcon.addPixmap(QPixmap(resources.clear_history_icon), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objM.clearHistoryButton.setIcon(Themes.objM.clearHistoryIcon)

        Themes.objM.apiButtonWidget.setStyleSheet(f"#apiWidget {{ background-color: {color.LIGHT_COLOR_3}; border: 2px solid {color.LIGHT_COLOR_5}; border-radius: 18px;}} QPushButton{{ background-color: {color.LIGHT_COLOR_3}; margin: 5px;}} QPushButton:hover{{ background-color: {color.LIGHT_COLOR_3};}}")

        Themes.objM.apiCombo.setStyleSheet(f" QComboBox{{  border: 0px; background-color: {color.LIGHT_COLOR_3};}} QComboBox::drop-down{{ border: 0px; width: 70px;}} QComboBox:selected{{ background-color: {color.LIGHT_COLOR_4};}}")

        Themes.objP.style = f"""   
            #settingsButton, #downloadButton, #themesButton{{
                border-radius: 15px;
                background-color: {color.LIGHT_COLOR_1};
            }}
            #settingsButton:hover, #downloadButton:hover, #themesButton:hover {{
                color:white;
                background-color: {color.LIGHT_COLOR_3};
            }}
        """
        Themes.objP.setStyleSheet(Themes.objP.style)

        Themes.objP.headerLabel.setMaximumHeight(48)
        
        Themes.objP.stackedWidget.setStyleSheet(f"background-color: {color.LIGHT_COLOR_3}; border-radius: 10px;")
        
        Themes.objP.headerBackgroundWidget.setMaximumHeight(60)
        Themes.objP.headerBackgroundWidget.setStyleSheet(f"background-color: {color.LIGHT_COLOR_4}; border-radius: 25px; color: white; padding-top: 0px;")
        
        Themes.objP.backIcon.addPixmap(QPixmap(resources.back_icon), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objP.backButton.setIcon(Themes.objP.backIcon)
        
        Themes.objP.backButton.setStyleSheet(f"QPushButton:hover{{ background-color: {color.LIGHT_COLOR_3}; border-radius: 18px;}}")

        Themes.objP.radioButtonOne.setStyleSheet("QRadioButton::indicator { width: 20px; height: 20px;}")

        Themes.objP.radioButtonTwo.setStyleSheet("QRadioButton::indicator { width: 20px; height: 20px; }")

        Themes.objP.radioButtonThree.setStyleSheet("QRadioButton::indicator { width: 20px; height: 20px;}")

        Themes.objP.downloadQueue.setStyleSheet("background-color: white;")

        # self.Themes.objP.spaceE.setPixmap(QPixmap("resources/icons/lightModeTheme.png"))

        Themes.objP.downloadDirPathBtn.setStyleSheet(f"background: {color.LIGHT_COLOR_4}; margin-top: 5px; margin-right: 5px; color: white;")
        Themes.objP.downloadDirPathBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        Themes.objP.pixPixmap = QPixmap(resources.light_mode)
        Themes.objP.spaceE.setPixmap(Themes.objP.pixPixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio))

        Themes.prefButtonActiveLight(Themes.objP, Themes.prefSelectedButtonIndex)

        Themes.readerStyle(Settings.readerDisplayIndex)

    def darkMode(obj) -> None:
        Themes.style = f"""
        *{{
            color: gray;
            background-color: {color.DARK_COLOR_9};
        }}
        QPushButton{{
            background-color: {color.DARK_COLOR_9};
            border-radius: 18px;
        }}
        QPushButton:hover {{
            background-color: {color.DARK_COLOR_4};
        }}
        QLineEdit{{
            border: 1px solid {color.DARK_COLOR_6};
            border-radius: 18px;
            padding-left: 15px;
            font: 13px;
        }}
        QLabel{{
            padding: 10px;
            border-radius: 10px;
        }}

        #toggleGridView:hover, #toggleListView:hover{{
            background-color: {color.DARK_COLOR_4};
            border-radius: 5px;
        }}

        #historyLabel{{
            color: {color.DARK_COLOR_10};
            background-color: {color.DARK_COLOR_5}; 
            font: 15px;
        }}
        #historyListView{{
            background-color: {color.DARK_COLOR_3};
            border: none;
        }}
        #historyScroll, scroll{{
            background-color: {color.DARK_COLOR_3};
            padding: 0px;
            margin: 0px;
            border: none;
        }}
        .History QPushButton{{
            color: gray;
            background-color: {color.DARK_COLOR_9};
        }}
        .History QPushButton:hover{{
            background-color: {color.DARK_COLOR_5};
        }}
        QToolTip{{
            background-color: {color.DARK_COLOR_3};
            color: {color.DARK_COLOR_10};
        }}
        """

        obj.setStyleSheet(Themes.style)
        
        Themes.objM.tabWidget.tabBar().setStyleSheet(f"QTabBar::tab {{ background-color: {color.DARK_COLOR_2}; width: 200px; padding: 0px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px; }}  QTabBar::tab:bottom{{ background: {color.DARK_COLOR_2}; color: {color.DARK_COLOR_6};}}  QTabBar::tab:bottom:selected {{ background-color: {color.DARK_COLOR_6}; color: white;}}")

        Themes.objM.tabWidget.setStyleSheet(f"QTabWidget::pane {{ background: {color.DARK_COLOR_3}; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;}} ")

        Themes.objM.homeTabStack.setStyleSheet(f"background-color: {color.DARK_COLOR_3}; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;")

        Themes.objM.library.setStyleSheet(f" background-color: {color.DARK_COLOR_3}; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;")

        Themes.objM.library.noItems.setStyleSheet(f" QWidget{{ background: transparent; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;}} QLabel {{ border: none; }}")
        
        Themes.objM.library.descriptionPage.setStyleSheet(f"QWidget#descPage {{ background:transparent;  border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px; }} QPushButton:hover {{ background-color: {color.DARK_COLOR_4};}}")

        Themes.objM.library.libraryShelf.setStyleSheet(f"background:transparent; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px; ")

        Themes.objM.library.libraryScrollArea.setStyleSheet(f"QScrollArea {{ background-color: transparent; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;}} QScrollBar:vertical {{ width: 7px; background: white; border: none; margin: 0px 0px 0px 0px; border-radius: 3px;}} QScrollBar::handle:vertical {{ background: {color.LIGHT_COLOR_7}; min-height:0px; border-radius: 3px;}} QScrollBar::add-line:vertical {{ background: qlineargradient(x1:0; y1:0, x2:1, y2:0, stop: 0 {color.LIGHT_COLOR_8}, stop: 0.5 {color.LIGHT_COLOR_8}, stop: 1 {color.LIGHT_COLOR_8}); height: 0px; subcontrol-position: bottom; subcontrol-origin: margin; }} QScrollBar::sub-line:vertical {{  background: qlineargradient(x1:0; y1:0, x2:1, y2:0, stop: 0 {color.LIGHT_COLOR_8}, stop: 0.5 {color.LIGHT_COLOR_8}, stop: 1 {color.LIGHT_COLOR_8}); height: 0px; subcontrol-position: top; subcontrol-origin: margin; }}")

        Themes.objM.library.descriptionPage.scrollArea.setStyleSheet(f"QScrollArea {{ background-color: transparent; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;}} QScrollBar:vertical {{ width: 7px; background: white; border: none; margin: 0px 0px 0px 0px; border-radius: 3px;}} QScrollBar::handle:vertical {{ background: {color.LIGHT_COLOR_7}; min-height:0px; border-radius: 3px;}} QScrollBar::add-line:vertical {{ background: qlineargradient(x1:0; y1:0, x2:1, y2:0, stop: 0 {color.LIGHT_COLOR_8}, stop: 0.5 {color.LIGHT_COLOR_8}, stop: 1 {color.LIGHT_COLOR_8}); height: 0px; subcontrol-position: bottom; subcontrol-origin: margin; }} QScrollBar::sub-line:vertical {{  background: qlineargradient(x1:0; y1:0, x2:1, y2:0, stop: 0 {color.LIGHT_COLOR_8}, stop: 0.5 {color.LIGHT_COLOR_8}, stop: 1 {color.LIGHT_COLOR_8}); height: 0px; subcontrol-position: top; subcontrol-origin: margin; }} QPushButton:hover{{ background-color: {color.DARK_COLOR_4};}}")

        Themes.objM.scroll.setStyleSheet(f"QScrollArea {{ background-color: {color.DARK_COLOR_3}; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;}} QScrollBar:vertical {{ width: 7px; background: white; border: none; margin: 0px 0px 0px 0px; border-radius: 3px;}} QScrollBar::handle:vertical {{ background: {color.LIGHT_COLOR_7}; min-height:0px; border-radius: 3px;}} QScrollBar::add-line:vertical {{ background: qlineargradient(x1:0; y1:0, x2:1, y2:0, stop: 0 {color.LIGHT_COLOR_8}, stop: 0.5 {color.LIGHT_COLOR_8}, stop: 1 {color.LIGHT_COLOR_8}); height: 0px; subcontrol-position: bottom; subcontrol-origin: margin; }} QScrollBar::sub-line:vertical {{  background: qlineargradient(x1:0; y1:0, x2:1, y2:0, stop: 0 {color.LIGHT_COLOR_8}, stop: 0.5 {color.LIGHT_COLOR_8}, stop: 1 {color.LIGHT_COLOR_8}); height: 0px; subcontrol-position: top; subcontrol-origin: margin; }} QPushButton:hover{{ background-color: {color.DARK_COLOR_4};}}")

        Themes.objM.library.libraryScrollAreaWidget.setStyleSheet(f"background-color: transparent; border: 1px solid transparent; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px; ")

        Themes.objM.scrollW.setStyleSheet(f" QObject{{ background-color: transparent; color: white; border: 1px solid transparent; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px;}} QPushButton{{background-color: {color.DARK_COLOR_6}; color: {color.DARK_COLOR_4}; border-radius: 15px;}} QPushButton:hover{{background-color: {color.DARK_COLOR_1}; color: {color.DARK_COLOR_4}; border-radius: 15px;}}")

        Themes.objM.historyListView.setStyleSheet(f"background-color: transparent; border: 1px solid transparent; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 0px; border-bottom-right-radius : 10px; ")

        Themes.objM.library.descriptionPage.selectionWidget.setStyleSheet(f"QWidget{{background-color: transparent;}} QToolTip{{background-color: {color.DARK_COLOR_2}; color: {color.DARK_COLOR_10} }}")

        Themes.objM.apiButton.setStyleSheet("QPushButton{ border-radius: 18px;}")
        
        Themes.objM.menuIcon.addPixmap(QPixmap(resources.d_menu_icon), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objM.menuButton.setIcon(Themes.objM.menuIcon)

        Themes.objM.searchIcon.addPixmap(QPixmap(resources.d_search_icon), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objM.searchButton.setIcon(Themes.objM.searchIcon)

        Themes.objM.localSearchIcon.addPixmap(QPixmap(resources.d_local_search_icon), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objM.localSearchButton.setIcon(Themes.objM.localSearchIcon)

        Themes.objM.localSearchIconSingleFormat.addPixmap(QPixmap(resources.d_local_search_single_icon), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objM.localSearchButtonSingleFormat.setIcon(Themes.objM.localSearchIconSingleFormat)

        Themes.objM.library.descriptionPage.exitButtonIcon.addPixmap(QPixmap(resources.d_exit_button), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objM.library.descriptionPage.exitButton.setIcon(Themes.objM.library.descriptionPage.exitButtonIcon)
        
        Themes.objM.library.descriptionPage.exitButton.setStyleSheet(f"QPushButton:hover{{ background-color: {color.DARK_COLOR_4}; border-radius: 18px;}}")

        Themes.objM.library.descriptionPage.deleteButtonIcon.addPixmap(QPixmap(resources.d_delete_manhua), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objM.library.descriptionPage.deleteButton.setIcon(Themes.objM.library.descriptionPage.deleteButtonIcon)
        
        Themes.objM.library.descriptionPage.deleteButton.setStyleSheet(f"QPushButton:hover{{ background-color: {color.DARK_COLOR_4}; border-radius: 18px;}}")
        
        Themes.objM.refreshIcon.addPixmap(QPixmap(resources.d_refresh_icon), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objM.refreshButton.setIcon(Themes.objM.refreshIcon)

        Themes.objM.clearHistoryIcon.addPixmap(QPixmap(resources.d_clear_history_icon), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objM.clearHistoryButton.setIcon(Themes.objM.clearHistoryIcon)

        Themes.objM.apiButtonWidget.setStyleSheet(f"#apiWidget {{ background-color: {color.DARK_COLOR_3}; border: 2px solid {color.DARK_COLOR_5}; border-radius: 18px;}} QPushButton{{ background-color: {color.DARK_COLOR_3}; margin: 5px;}} QPushButton:hover{{ background-color: {color.DARK_COLOR_3};}}")

        Themes.objM.apiCombo.setStyleSheet(f" QComboBox{{  border: 0px; background-color: {color.DARK_COLOR_3};}} QComboBox::drop-down{{ border: 0px; width: 70px;}} QComboBox:selected{{ background-color: white;}}")

        Themes.objP.style = f"""   
            #settingsButton, #downloadButton, #themesButton{{
                border-radius: 15px;
                color: white;
                background-color: {color.DARK_COLOR_3};
            }}
            #settingsButton:hover, #downloadButton:hover, #themesButton:hover {{
                color:white;
                background-color: {color.DARK_COLOR_3};
            }}
        """
        Themes.objP.setStyleSheet(Themes.objP.style)

        Themes.objP.headerLabel.setMaximumHeight(48)
        
        Themes.objP.stackedWidget.setStyleSheet(f"background-color: {color.DARK_COLOR_3}; border-radius: 10px;")
        
        Themes.objP.headerBackgroundWidget.setMaximumHeight(60)
        Themes.objP.headerBackgroundWidget.setStyleSheet(f"background-color: {color.DARK_COLOR_4}; border-radius: 25px; color: white; padding-top: 0px;")
        
        Themes.objP.backIcon.addPixmap(QPixmap(resources.back_icon), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objP.backButton.setIcon(Themes.objP.backIcon)
        
        Themes.objP.backButton.setStyleSheet(f"QPushButton:hover{{ background-color: {color.DARK_COLOR_3}; border-radius: 18px;}}")

        Themes.objP.radioButtonOne.setStyleSheet("QRadioButton::indicator { width: 20px; height: 20px;}")

        Themes.objP.radioButtonTwo.setStyleSheet("QRadioButton::indicator { width: 20px; height: 20px; }")

        Themes.objP.radioButtonThree.setStyleSheet("QRadioButton::indicator { width: 20px; height: 20px;}")

        Themes.objP.downloadQueue.setStyleSheet(f"background-color: {color.DARK_COLOR_9};")

        # self.Themes.objP.spaceE.setPixmap(QPixmap("resources/icons/lightModeTheme.png"))

        Themes.objP.downloadDirPathBtn.setStyleSheet(f"background: {color.LIGHT_COLOR_4}; margin-top: 5px; margin-right: 5px; color: white;")
        Themes.objP.downloadDirPathBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        Themes.objP.pixPixmap = QPixmap(resources.dark_mode)
        Themes.objP.spaceE.setPixmap(Themes.objP.pixPixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio))

        Themes.prefButtonActiveDark(Themes.objP, Themes.prefSelectedButtonIndex)

        Themes.readerStyle(Settings.readerDisplayIndex)


    def readerStyle(index: int) -> None:
        if Settings.themeIndex == consts.E_THEME_LIGHT_MODE:
            Themes.objR.style = """ 
                QPushButton{
                    border-radius: 18px;
                    color: red;
                }
            """
            Themes.objR.setStyleSheet(Themes.objR.style)

            Themes.objR.backIcon.addPixmap(QPixmap(resources.exit_button), QIcon.Mode.Normal, QIcon.State.Off)
            Themes.objR.backButton.setIcon(Themes.objR.backIcon)
            
            Themes.objR.backButton.setStyleSheet(f"QPushButton:hover{{ background-color: {color.LIGHT_COLOR_3}; border-radius: 18px;}}")

            Themes.objR.setToCoverIcon.addPixmap(QPixmap(resources.download_icon), QIcon.Mode.Normal, QIcon.State.Off)
            Themes.objR.setToCoverButton.setIcon(Themes.objR.setToCoverIcon)
            
            Themes.objR.setToCoverButton.setStyleSheet(f"QPushButton:hover{{ background-color: {color.LIGHT_COLOR_3}; border-radius: 18px;}}")

            Themes.objR.manhuaLabel.setStyleSheet(" padding: 0px;")
            
            if Settings.readerDisplayIndex == consts.E_RADIO_SELECTED_WEBTOON:
                Themes.objR.screenScrollArea.setStyleSheet("border: 0px")

            if index != consts.E_RADIO_SELECTED_WEBTOON:
                Themes.objR.nextIcon.addPixmap(QPixmap(resources.next_icon), QIcon.Mode.Normal, QIcon.State.Off)
                Themes.objR.nextButton.setIcon(Themes.objR.nextIcon)
            
                Themes.objR.nextButton.setStyleSheet(f"QPushButton:hover{{ background-color: {color.LIGHT_COLOR_3}; border-radius: 18px;}}")

                Themes.objR.previousIcon.addPixmap(QPixmap(resources.previous_icon), QIcon.Mode.Normal, QIcon.State.Off)
                Themes.objR.previousButton.setIcon(Themes.objR.previousIcon)
            
                Themes.objR.previousButton.setStyleSheet(f"QPushButton:hover{{ background-color: {color.LIGHT_COLOR_3}; border-radius: 18px;}}")

        else:
            Themes.objR.style = """ 
                QPushButton{
                    border-radius: 18px;
                    color: red;
                }
            """
            Themes.objR.setStyleSheet(Themes.objR.style)

            Themes.objR.backIcon.addPixmap(QPixmap(resources.d_exit_button), QIcon.Mode.Normal, QIcon.State.Off)
            Themes.objR.backButton.setIcon(Themes.objR.backIcon)
            
            Themes.objR.backButton.setStyleSheet(f"QPushButton:hover{{ background-color: {color.DARK_COLOR_3}; border-radius: 18px;}}")

            Themes.objR.setToCoverIcon.addPixmap(QPixmap(resources.d_download_icon), QIcon.Mode.Normal, QIcon.State.Off)
            Themes.objR.setToCoverButton.setIcon(Themes.objR.setToCoverIcon)
            
            Themes.objR.setToCoverButton.setStyleSheet(f"QPushButton:hover{{ background-color: {color.DARK_COLOR_3}; border-radius: 18px;}}")

            Themes.objR.manhuaLabel.setStyleSheet(" padding: 0px;")
            
            if Settings.readerDisplayIndex == consts.E_RADIO_SELECTED_WEBTOON:
                Themes.objR.screenScrollArea.setStyleSheet("border: 0px")

            if index != consts.E_RADIO_SELECTED_WEBTOON:
                Themes.objR.nextIcon.addPixmap(QPixmap(resources.d_next_icon), QIcon.Mode.Normal, QIcon.State.Off)
                Themes.objR.nextButton.setIcon(Themes.objR.nextIcon)
            
                Themes.objR.nextButton.setStyleSheet(f"QPushButton:hover{{ background-color: {color.DARK_COLOR_3}; border-radius: 18px;}}")

                Themes.objR.previousIcon.addPixmap(QPixmap(resources.d_previous_icon), QIcon.Mode.Normal, QIcon.State.Off)
                Themes.objR.previousButton.setIcon(Themes.objR.previousIcon)
            
                Themes.objR.previousButton.setStyleSheet(f"QPushButton:hover{{ background-color: {color.DARK_COLOR_3}; border-radius: 18px;}}")
  
    def changeTabBarIconLight(obj) -> None:
        obj.tabIndex = obj.tabWidget.currentIndex()
        if obj.tabIndex == consts.E_TAB_HOME_INDEX:
            obj.homeIcon.addPixmap(QPixmap(resources.home_icon_dark), QIcon.Mode.Normal, QIcon.State.Off)
            obj.tabWidget.setTabIcon(obj.tabIndex, obj.homeIcon)

            obj.libraryIcon.addPixmap(QPixmap(resources.library_icon), QIcon.Mode.Normal, QIcon.State.Off)
            obj.tabWidget.setTabIcon(1, obj.libraryIcon)
        else:
            obj.homeIcon.addPixmap(QPixmap(resources.home_icon), QIcon.Mode.Normal, QIcon.State.Off)
            obj.tabWidget.setTabIcon(0, obj.homeIcon)

            obj.libraryIcon.addPixmap(QPixmap(resources.library_icon_dark), QIcon.Mode.Normal, QIcon.State.Off)
            obj.tabWidget.setTabIcon(obj.tabIndex, obj.libraryIcon)

    def changeTabBarIconDark(obj) -> None:
        obj.tabIndex = obj.tabWidget.currentIndex()
        if obj.tabIndex == consts.E_TAB_HOME_INDEX:
            obj.homeIcon.addPixmap(QPixmap(resources.home_icon_dark), QIcon.Mode.Normal, QIcon.State.Off)
            obj.tabWidget.setTabIcon(obj.tabIndex, obj.homeIcon)

            obj.libraryIcon.addPixmap(QPixmap(resources.library_icon), QIcon.Mode.Normal, QIcon.State.Off)
            obj.tabWidget.setTabIcon(1, obj.libraryIcon)
        else:
            obj.homeIcon.addPixmap(QPixmap(resources.home_icon), QIcon.Mode.Normal, QIcon.State.Off)
            obj.tabWidget.setTabIcon(0, obj.homeIcon)

            obj.libraryIcon.addPixmap(QPixmap(resources.library_icon_dark), QIcon.Mode.Normal, QIcon.State.Off)
            obj.tabWidget.setTabIcon(obj.tabIndex, obj.libraryIcon)

    def prefButtonActive(indexB, themeIndex: int) -> None:
        if themeIndex == consts.E_THEME_LIGHT_MODE:
            Themes.prefButtonActiveLight(Themes.objP, indexB)
        else:
            Themes.prefButtonActiveDark(Themes.objP, indexB)

    def resetHistoryStyle() -> None:
        # if Settings.themeIndex == consts.E_THEME_LIGHT_MODE:    
        #     self.obj.Themes.objMainWindow.scrollW.setStyleSheet("QWidget { background-color: {color.LIGHT_COLOR_3}; padding: 0px; margin: 0px; border: none;} QPushButton:hover { color: white; }")
        ...    

    def declareTheme() -> None:
        if Settings.themeIndex == consts.E_THEME_LIGHT_MODE:
            Settings.themeButtonState = False
        else:
            Settings.themeButtonState = True
        Themes.prefButtonActive(Themes.prefSelectedButtonIndex, Settings.themeIndex)
        Themes.resetManhuaTheme()
        Themes.setViewOptionStyle()

    def setViewOptionStyle() -> None:
        listIcon = ""
        gridIcon = ""
        if Settings.themeIndex == consts.E_THEME_LIGHT_MODE:
            listIcon = resources.list_icon
            gridIcon = resources.grid_icon
        else:
            listIcon = resources.list_icon_disabled
            gridIcon = resources.grid_icon_disabled

        Themes.toggleGridIcon = QIcon()
        Themes.toggleListIcon = QIcon()

        Themes.toggleGridIcon.addPixmap(QPixmap(gridIcon), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objM.toggleGridView.setIcon(Themes.toggleGridIcon)
        
        Themes.toggleListIcon.addPixmap(QPixmap(listIcon), QIcon.Mode.Normal, QIcon.State.Off)
        Themes.objM.toggleListView.setIcon(Themes.toggleListIcon)

        if Settings.viewIsGrid:
            Themes.objM.view.setText(consts.E_MW_GRID_TEXT)
            Themes.objM.toggleGridView.setStyleSheet(f"border-radius: 25px; border: 1px solid {color.DARK_COLOR_5}; background-color: {color.DARK_COLOR_5}")
            Themes.objM.toggleListView.setStyleSheet(f"border: none; background-color: transparent")
        else:
            Themes.objM.view.setText(consts.E_MW_LIST_TEXT)
            Themes.objM.toggleGridView.setStyleSheet(f"border: none; background-color: transparent")
            Themes.objM.toggleListView.setStyleSheet(f"border-radius: 25px; border: 1px solid {color.DARK_COLOR_5}; background-color: {color.DARK_COLOR_5}")

    def resetManhuaTheme() -> None:
        for all in Themes.objM.library.libraryListdata:

            Themes.setManhuaObjStyle(all)

    def setManhuaObjStyle(obj) -> None:
        if Settings.themeIndex == consts.E_THEME_LIGHT_MODE:
            obj.setStyleSheet(f" QLabel#manhuaLabel{{ padding: 7px; border-radius: 5px; background-color: white; border: none;}}  QLabel#nameLabel{{ padding: 1px; border-radius: 5px; color: {color.LIGHT_COLOR_2}; background-color: transparent;}} QPushButton#fav {{ background: {color.LIGHT_COLOR_4};  border: none; border-radius: 5px;}} QPushButton#fav:hover {{ background-color: {color.LIGHT_COLOR_5}}} .Manhua {{ border-radius: 5px; background-color: {color.LIGHT_COLOR_6};}} .Manhua:hover{{ background: {color.LIGHT_COLOR_5};}} QToolTip{{background-color: {color.DARK_COLOR_4};color: {color.DARK_COLOR_2} }}") 

        else:
            obj.setStyleSheet(f" QLabel#manhuaLabel{{ padding: 7px; border-radius: 5px; background-color: white; border: none;}}  QLabel#nameLabel{{ padding: 5px; border: none; color: {color.DARK_COLOR_10}; background-color: transparent;}} QPushButton#fav {{ background: {color.DARK_COLOR_4};  border: none; border-radius: 5px;}} QPushButton#fav:hover {{ background-color: {color.DARK_COLOR_5}}} .Manhua {{ border-radius: 5px; background-color: {color.DARK_COLOR_6};}} .Manhua:hover{{ background: {color.DARK_COLOR_1}}} QToolTip{{background-color: {color.DARK_COLOR_2};color: {color.DARK_COLOR_10} }}") 

class ToggleSwitch(QPushButton):
    def __init__(self) -> None:
        super().__init__()
        self.setCheckable(True)
        self.setMinimumWidth(66)
        self.setMinimumHeight(22)

    def paintEvent(self, event) -> None:
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
    def __init__(self, obj, widgetTitle, widget) -> None:
        super().__init__()
        
        self.obj = obj
        self.widgetTitle = widgetTitle
        self.widget = widget # StsckedWidgetWindow or stWindow
        self.widgetIcon = widget.window_icon
        self.widgetMainW = self.widget.objMainWindow
        self.widgetLibrary = self.widget.objMainWindow.library
        self.widgetReader = self.widget.objReader
        widIcon = 30
        iconsize = 30
        iconsizew = 48

        self.resize_width = 1092
        self.resize_height = 614

        self.size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

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
        self.customWindowTitle.setSizePolicy(self.size_policy)
        self.customWindowTitle.setStyleSheet("padding-left: 8px;")

        self.minimizeIcon = QPushButton()
        self.minimizeIcon.setSizePolicy(self.size_policy)
        self.minimizeIcon.setCheckable(True)

        self.restoreIcon = QPushButton()
        self.restoreIcon.setSizePolicy(self.size_policy)
        self.restoreIcon.setCheckable(True)

        self.closeIcon = QPushButton()
        self.closeIcon.setSizePolicy(self.size_policy)
        self.closeIcon.setCheckable(True)

        self.minimizeIcon.setMaximumSize(iconsizew, iconsize)

        self.minimizeIconIcon = QIcon()
        self.minimizeIconIcon.addPixmap(QPixmap("resources/icons/icons8-minimize-dark-90.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeIcon.setIcon(self.minimizeIconIcon)

        self.minimizeIcon.setStyleSheet("QPushButton{background-color: rgba(72, 75, 106, 0.8); border: none;} QPushButton:hover{ background-color: {color.LIGHT_COLOR_3}; }")


        self.restoreIcon.setMaximumSize(iconsizew, iconsize)

        self.restoreIconIcon = QIcon()
        self.restoreIconIcon.addPixmap(QPixmap("resources/icons/icons8-restore-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.restoreIcon.setIcon(self.restoreIconIcon)

        self.restoreIcon.setStyleSheet("QPushButton{background-color: rgba(72, 75, 106, 0.8); border: none;} QPushButton:hover{ background-color: {color.LIGHT_COLOR_3};}")

        self.closeIcon.setMaximumSize(iconsizew, iconsize)

        self.closeIconIcon = QIcon()
        self.closeIconIcon.addPixmap(QPixmap("resources/icons/icons8-close-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeIcon.setIcon(self.closeIconIcon)

        self.closeIcon.setStyleSheet("QPushButton{background-color: rgba(72, 75, 106, 0.8); border: none;} QPushButton:hover{ background-color: rgba(247, 10, 15, 1);}")

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
        self.closeIcon.clicked.connect(lambda: self.close())

    def close(self):
        Settings.updateSettings()
        return self.obj.close()

    def toggleRestore(self) -> None:
        if self.obj.windowState() == Qt.WindowState.WindowMaximized:
            self.obj.resize(QSize(self.resize_width, self.resize_height))
            self.obj.setWindowState(Qt.WindowState.WindowActive)
            if Settings.viewIsGrid:
                self.widgetLibrary.libraryResized()
            
            self.restoreIconIcon.addPixmap(QPixmap("resources/icons/icons8-maximize-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.restoreIcon.setIcon(self.restoreIconIcon)
        else:
            self.obj.showMaximized()
            self.obj.setWindowState(Qt.WindowState.WindowMaximized)
            if Settings.viewIsGrid:
                self.widgetLibrary.libraryMaximized()

            self.restoreIconIcon.addPixmap(QPixmap("resources/icons/icons8-restore-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.restoreIcon.setIcon(self.restoreIconIcon)
        self.widgetReader.calLabelSize()

class MoveableWindow(QWidget):
    def __init__(self, obj, widget) -> None:
        super().__init__()
        self.refIcon = QPushButton()
        self.refIconIcon = QIcon()
        self.obj = obj #<MainWindow Class>
        # self.obj.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.widget = widget # StsckedWidgetWindow or stWindow
        self.widgetMainW = self.widget.objMainWindow
        self.widgetLibrary = self.widget.objMainWindow.library
        self.prevGeo = self.obj.geometry()
        self.oldPosition = self.geometry()

    def mousePressEvent(self, event) -> None:
        layOut = self.obj.customTitleBar.buttonsLayout
        if not any((layOut.itemAt(i).widget().underMouse() for i in range(layOut.count()))) :
            self.oldPosition = event.scenePosition()

    def mouseDoubleClickEvent(self, event) -> None:
        layOut = self.obj.customTitleBar.buttonsLayout
        if not any((layOut.itemAt(i).widget().underMouse() for i in range(layOut.count())))  :
            if self.obj.windowState() == Qt.WindowState.WindowMaximized or self.obj.windowState() == Qt.WindowState.WindowFullScreen:
                self.obj.setWindowState(Qt.WindowState.WindowNoState)
                # self.obj.resize(QSize(1092, 614))
                self.obj.setGeometry(200, 0, 1092, 614)
                if Settings.viewIsGrid:
                    self.widgetLibrary.libraryResized()

                self.refIconIcon.addPixmap(QPixmap("resources/icons/icons8-maximize-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
                self.refIcon.setIcon(self.refIconIcon)

            elif self.obj.windowState() == Qt.WindowState.WindowNoState or self.obj.windowState() == Qt.WindowState.WindowActive:
                self.obj.showMaximized()
                self.obj.setWindowState(Qt.WindowState.WindowMaximized)
                if Settings.viewIsGrid:
                    self.widgetLibrary.libraryMaximized()

                self.refIconIcon.addPixmap(QPixmap("resources/icons/icons8-restore-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
                self.refIcon.setIcon(self.refIconIcon)
        
    def mouseMoveEvent(self, event) -> None:
        layOut = self.obj.customTitleBar.buttonsLayout
        if not any((layOut.itemAt(i).widget().underMouse() for i in range(layOut.count()))) :
            # self.obj.resize(QSize(1092, 614))
            if self.obj.windowState() == Qt.WindowState.WindowFullScreen or self.obj.windowState() == Qt.WindowState.WindowMaximized:
                self.oldPosition = QPointF(self.prevGeo.width() * .5, 50)
            gr = self.obj.geometry()
            screenPos = event.globalPosition()
            pos = screenPos - self.oldPosition 
            x = int(max(pos.x(), 0))
            y = int(max(pos.y(), 0))
            screen = QGuiApplication.screenAt(QPoint(x, y)).size()
            x = int(min(x, screen.width() - gr.width()))
            y = int(min(y, screen.height() - gr.height()))
            self.obj.move(x, y)

            self.obj.setWindowState(Qt.WindowState.WindowActive)
            if Settings.viewIsGrid:
                self.widgetLibrary.libraryResized()

            self.refIconIcon.addPixmap(QPixmap("resources/icons/icons8-maximize-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.refIcon.setIcon(self.refIconIcon)

    def mouseReleaseEvent(self, event) -> None:
        if event.globalPosition().y() < 10:
            self.prevGeo = self.obj.geometry()
            self.obj.setWindowState(Qt.WindowState.WindowMaximized)
            self.refIconIcon.addPixmap(QPixmap("resources/icons/icons8-restore-dark-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.refIcon.setIcon(self.refIconIcon)

            if Settings.viewIsGrid:
                self.widgetLibrary.libraryMaximized()
            