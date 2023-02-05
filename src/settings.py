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



from pathlib import Path
import os, consts, json, ctypes

class Settings(object):
    obj = object()
    objM = object()
    objP = object()
    objR = object()

    picklePath = str(os.path.join(Path.home(), "Manhua Reader"))
    pickleFile = os.path.join(picklePath, "metadata.mhr")
    pickleDict = dict()

    def init() -> None: 
        if not os.path.exists(Settings.pickleFile):
            os.makedirs(Settings.picklePath, exist_ok=True)
            
            Settings.saveData(Settings.defaults())
            # print("System call", os.system(f"attrib +h {Settings.pickleFile}"))
        Settings.pickleDict = Settings.loadSettings()
        
        if not os.path.exists(Settings.downloadInitPath):
            os.makedirs(Settings.downloadInitPath)

        if not os.path.exists(Settings.extractionInitPath):
            os.makedirs(Settings.extractionInitPath)

    def initObjs(obj: object) -> None:
        Settings.obj = obj
        Settings.objM = obj.objMainWindow
        Settings.objR = obj.objReader
        Settings.objP = obj.objPref

    def defaults() -> dict:
        return  {
            "libraryMetadata" : {},
            "libraryInitPath" : "",
            "libraryNewPath" : "C:\\",
            "viewIsGrid" : False,
            "downloadInitPath" : str(os.path.join(Path.home(), "Documents\\Manhua Reader\\downloads\\")),
            "downloadNewPath" : str(os.path.join(Path.home(), "Documents\\Manhua Reader\\downloads\\")),
            "extractionInitPath" : str(os.path.join(Path.home(), "Documents\\Manhua Reader\\archives\\")),
            "extractionNewPath" : str(os.path.join(Path.home(), "Documents\\Manhua Reader\\archives\\")),
            "updateChapter" : True,
            "updateOther" : True,
            "hideNav" : True,
            "fsState" : False,
            "readerDisplayIndex" : consts.E_RADIO_SELECTED_WEBTOON,
            "compressionState" : True,
            "apiName" : ['Asura Scan', 'Mangabat', 'HolyManga'],
            "apiIndex" : 1,

            "themeIndex" : consts.E_THEME_LIGHT_MODE,
            "themeButtonState" : False,
            "historyData" : []
        }

    def saveData(data) -> None:
        data = json.dumps(data)

        data = data.encode()

        with open(os.path.expanduser(Settings.pickleFile), "wb") as filehandle:
            filehandle.write(data)

    def loadSettings() -> dict:
        try:
            data = b''
            with open(Settings.pickleFile, 'rb') as filehandle:
                data = filehandle.read()
            data = data.decode()
            data = json.loads(data)

            for key, value in data.items():
                setattr(Settings, key, value)
            return data
        except PermissionError:
            ...
        except FileNotFoundError:
            data = Settings.saveDefaults()
            return Settings.loadSettings()

    def updateSettings():
        data = {key: Settings.__dict__[key] for key in Settings.defaults()}

        Settings.saveData(data)

    def setMainWindowVariables() -> None:
        Settings.objM.apiName = Settings.apiName

    def setObjMState() -> None:
        Settings.objM.apiButton.setText(Settings.apiName[Settings.apiIndex])

    def setStates() -> None:
        Settings.setMainWindowVariables()
        Settings.objR.selfInit()

        Settings.objM.apiCombo.addItems(Settings.apiName)

        Settings.setObjMState()

        Settings.objM.apiCombo.setCurrentIndex(Settings.apiIndex)
        if Settings.apiIndex == 0:
            Settings.objM.setApiIndex(Settings.apiIndex)
        
        Settings.objP.downloadDirPathDisplay.setText(str(Settings.downloadNewPath))

        Settings.objP.compressArchiveToggleBtn.setChecked(Settings.compressionState)

        Settings.objP.toggleOne.setChecked(Settings.updateChapter)

        Settings.objP.toggleTwo.setChecked(Settings.updateOther)

        Settings.objP.readerNavtoggle.setChecked(Settings.hideNav)

        Settings.objP.readerFStoggle.setChecked(Settings.fsState)

        Settings.objP.readerDisplayList[Settings.readerDisplayIndex].setChecked(True)

        Settings.objP.themesBtn.setChecked(Settings.themeButtonState)
        
