# Manhua Reader,  An application for reading mangas and manhuas online and offline
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



from PyQt6.QtWidgets import QWidget, QStackedWidget

from themes import Themes
from settings import Settings

class Reader(QWidget):
    def __init__(self, obj, win_dow):
        super().__init__()

        self.obj = obj
        self.win_dow = win_dow

        
        self.themeObj = object()
        self.setting = object()

        self.themeIndex = object()

