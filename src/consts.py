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


VERSION = "v.1.0.2"
APP_NAME = f"Manhua Reader"
APP_DOMAIN = "els.ng"
ORG_NAME = "El's"

MIN_SCREEN_WIDTH = 1092
MIN_SCREEN_HEIGHT = 614
LIB_DIMENSION = 728
C_W_HEIGHT = 30
MAX_BTN_SIZE = 36
MIN_BTN_SIZE = 16
ICON_SIZE = 20
TOOLTIP_DURATION = 3000
EMPTY = 0
IMG_EXT_LIST = ['.jpeg', '.jpg', '.png']


# enums
E_WINDOW_STACK_MW = 0
E_WINDOW_STACK_READER = 1
E_WINDOW_STACK_PREF = 2

E_MW_GRID_VIEW = 0
E_MW_GRID_TEXT = "Grid View"

E_MW_LIST_VIEW = 1
E_MW_LIST_TEXT = "List View"

E_THEME_LIGHT_MODE = 0
E_THEME_DARK_MODE = 1

E_TAB_HOME_INDEX = 0
E_TAB_HOME_INNER_MAIN = 0
E_TAB_HOME_NO_INTERNET = 1
E_TAB_HOME_NO_RESULT = 2
E_TAB_HOME_RESULT_PAGE = 3

E_TAB_LIBRARY_INDEX = 1
E_TAB_LIBRARY_NO_ITEM = 0
E_TAB_LIBRARY_SHELF = 1
E_TAB_LIBRARY_DESCRIPTION_PAGE = 2

E_ACTIVE_STACK_SETTINGS = 0
E_ACTIVE_STACK_DOWNLOAD = 1
E_ACTIVE_STACK_THEME = 2

E_RADIO_SELECTED_LTR = 0
E_RADIO_SELECTED_WEBTOON = 1
E_RADIO_SELECTED_RTL = 2

E_TOGGLE_AUTO_UPDATE = 0
E_TOGGLE_AUTO_UPDATE_OTHER = 1
E_TOGGLE_HIDE_NAV = 2
E_TOGGLE_FULLSCREEN = 3

E_STATUS_OFFLINE = "Offline"
E_STATUS_ONLINE = "Online"
E_STATUS_ARCHIVE = "Archive"

E_STATUS_OFFLINE_TEXT = "Local Manhua Bundle"
E_STATUS_ONLINE_TEXT = "Online Manhua Bundle"
E_STATUS_ARCHIVE_TEXT = "Archive Manhua Bundle"

E_MW_TEXT_DUMMY_DESCRIPTION = "No Description... This file is a locally imported file, metadata consist of no description..."



E_DIALOG_EMPTY = "empty"
E_DIALOG_STRUCTURE = "structure"
E_DIALOG_BADFILE = "badFile"
E_DIALOG_NONE = "none"
E_DIALOG_DUPLICATE = "duplicate"
E_DIALOG_PERMISSION = "permission"
E_DIALOG_DELETED_MANHUA = "deletedM"
E_DIALOG_DELETED_CHAPTER = "deletedC"
E_DIALOG_DELETED_IMAGE = "deletedI"
E_DIALOG_REGEX = "regex"
E_DIALOG_FILE_NOT_FOUND = "file_not_found"


# object names
OBJ_APP = "objApp"
OBJ_WINDOW = "objWindow"
OBJ_MW_NAME = "objMainWindow"
OBJ_READER_NAME = "objReader"
OBJ_PREF_NAME = "objPref"
OBJ_LIB_NAME = "objLib"

OBJ_MW_MENU_BTN = "menuButton"
OBJ_MW_SEARCH_BTN = "searchButton"
OBJ_MW_REFRESH_BTN = "refreshButton"
OBJ_MW_LINE_EDIT = "lineEdit"
OBJ_MW_LOCAL_SEARCH_BTN = "localSearchButton"
OBJ_MW_LOCAL_SEARCH_ARCHIVE_BTN = "localSearcButtonSingleFormat"
OBJ_MW_API_BTN_WIDGET = "apiWidget"
OBJ_MW_CLEAR_HISTORY_BTN = "clearHistoryButton"
OBJ_MW_TOGGLE_LIST_BTN = "toggleListView"
OBJ_MW_TOGGLE_GRID_BTN = "toggleGridView"
OBJ_MW_HISTORY_LABEL = "historyLabel"
OBJ_MW_HISTORY_LIST = "historyListView"
OBJ_MW_HISTORY_SCROLL_W = "historyScroll"
OBJ_MW_SCROLL = "scroll"
OBJ_MW_LIBRARY = "libraryOrigin"
OBJ_MW_MANHUA_LABEL = "manhuaLabel"
OBJ_MW_MANHUA_NAME_LABEL = "nameLabel"
OBJ_MW_LIBRARY_DESC = "descPage"
OBJ_MW_LIBRARY_DESC_DELETE_MANHUA_BTN = "deleteManhuaButton"

OBJ_PREF_BACK_BTN = "backButton"
OBJ_PREF_HEADER_LABEL = "headerLabel"
OBJ_PREF_STACK = "prefStacked"
OBJ_PREF_STACK_SETTINGS = "settingsWidget"
OBJ_PREF_STACK_DOWNLOAD = "downloadsWidget"
OBJ_PREF_STACK_THEME = "themesWidget"
OBJ_PREF_SETTINGS_BTN = "settingsButton"
OBJ_PREF_DOWNLOAD_BTN = "downloadButton"
OBJ_PREF_THEME_BTN = "themesButton"
OBJ_PREF_COMPRESSED_BTN = "compressButton"

OBJ_READER_BACK_BTN = "backButton"
OBJ_READER_PREVIOUS_BTN = "previousButton"
OBJ_READER_NEXT_BTN = "nextButton"
OBJ_READER_SET_TO_COVER_BTN = "setToCoverButton"
