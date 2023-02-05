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
    def __init__(self) -> None:
        super().__init__()
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
        self.setText(f"{self.data['manhuaTitle']} \n{self.data['chapter']} - pg {self.data['page']}\n{self.data['time']}")
        
    def createPolicy(self) -> None:
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMaximumHeight(50)

    def initData(self, mTitle: str, cTitle: str, path: str, index: int, page: int) -> None:
        self.data["manhuaTitle"] = mTitle
        self.data["chapter"] = cTitle
        self.data["path"] = path
        self.data["mPath"] = str(Path(path).parent)
        self.data["index"] = index
        self.data["page"] = page
        self.bindData()

    def updateData(self) -> None:
        self.data["page"] = Settings.historyData[0]["page"]
        self.data["chapter"] = Settings.historyData[0]["chapter"]
        self.data["path"] = Settings.historyData[0]["path"]
        self.data["index"] = Settings.historyData[0]["index"]
        self.updateTime()

    def getData(self):
        return self.data

    def updateTime(self):
        self.data["time"] = datetime.now().strftime("%d/%m/%Y - %H:%M")

    def launchReader(self):
        metadata = self.data["manhuaTitle"]
        metadataPath = Settings.libraryMetadata[metadata]["ManhuaPath"]
        Link.callBackDeep(consts.OBJ_MW_NAME, "library", "openDescription", metadata, metadataPath, self.data["index"])
        Link.callBack(consts.OBJ_LIB_NAME, "launchReader", self.data["manhuaTitle"], self.data["chapter"], self.data["index"], self.data["path"], self.data["page"])
