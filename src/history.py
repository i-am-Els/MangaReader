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


from PyQt6.QtWidgets import QPushButton, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from datetime import datetime
import consts
from linker import Link
from settings import Settings
from pathlib import Path

class History(QPushButton):
    imageExit = 0
    def __init__(self, updateTime: bool = True) -> None:
        super().__init__()
        self.v_updateTime = updateTime
        self.data = {
            "manhuaTitle" : "",
            "chapter" : "",
            "mPath" : "",
            "path" : "",
            "index" : 0,
            "page" : 0,
            "time" : ""
        }

        self.updateTime()
        self.createPolicy()
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.clicked.connect(lambda: self.launchReader())

    def bindData(self) -> None:
        self.fm = self.fontMetrics()
        self.elided = self.fm.elidedText(self.data['manhuaTitle'], Qt.TextElideMode.ElideMiddle, 200)
        txt = f"{self.elided} \n{self.data['chapter']} - pg {self.data['page']}\n{self.data['time']}"
        self.setText(txt)
        
    def createPolicy(self) -> None:
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMaximumHeight(50)

    def initData(self, mTitle: str, cTitle: str, path: str, index: int, page: int, time: str = "") -> None:
        self.data["manhuaTitle"] = mTitle
        self.data["chapter"] = cTitle
        self.data["path"] = path
        self.data["mPath"] = str(Path(path).parent)
        self.data["index"] = index
        self.data["page"] = page
        if not self.v_updateTime:
            self.data["time"] = time
        self.bindData()

    def updateData(self) -> None:
        self.data["page"] = Settings.historyData[0]["page"]
        self.data["chapter"] = Settings.historyData[0]["chapter"]
        self.data["path"] = Settings.historyData[0]["path"]
        self.data["index"] = Settings.historyData[0]["index"]
        self.updateTime()

    def getData(self):
        return self.data
    
    def setTimeUpdatable(self, updatable: bool) -> None:
        self.v_updateTime = updatable

    def updateTime(self):
        if self.v_updateTime:
            self.data["time"] = datetime.now().strftime("%d/%m/%Y - %H:%M")

    def launchReader(self):
        metadata = self.data["manhuaTitle"]
        metadataPath = Settings.libraryMetadata[metadata]["ManhuaPath"]
        Link.callBackDeep(consts.OBJ_MW_NAME, "library", "openDescription", metadata, metadataPath, self.data["index"])
        Link.callBack(consts.OBJ_LIB_NAME, "launchReader", self.data["manhuaTitle"], self.data["chapter"], self.data["index"], self.data["path"], self.data["page"])
