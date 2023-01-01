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
import os, consts

class Settings(object):
    obj = object()
    objM = object()
    objP = object()
    objR = object()

    picklePath = str(os.path.join(Path.home(), "Manhua Reader"))
            
    libraryInitPath = "C:\\"
    libraryNewPath = libraryInitPath
    localManhuaTitleDict = dict()

    updateChapter = True
    updateOther = True
    hideNav = True
    fsState = False
    readerDisplayIndex = 1

    compressionState = True

    themeIndex = consts.E_THEME_LIGHT_MODE
    themeButtonState = False

    downloadInitPath = str(os.path.join(Path.home(), "Documents\\Manhua Reader\\downloads\\"))

    downloadNewPath = downloadInitPath

    extractionInitPath = str(os.path.join(Path.home(), "Documents\\Manhua Reader\\archives\\"))

    extractionNewPath = extractionInitPath
    apiName = ['Asura Scan', 'Mangabat', 'HolyManga']
    apiIndex = 1

    def init() -> None: 
        if not os.path.exists(Settings.picklePath):
            os.makedirs(Settings.picklePath)
        
        if not os.path.exists(Settings.downloadInitPath):
            os.makedirs(Settings.downloadInitPath)

        if not os.path.exists(Settings.extractionInitPath):
            os.makedirs(Settings.extractionInitPath)

    def initObjs(obj: object) -> None:
        Settings.obj = obj
        Settings.objM = obj.objMainWindow
        Settings.objR = obj.objReader
        Settings.objP = obj.objPref


    def setMainWindowVariables() -> None:
        Settings.objM.initPath = Settings.libraryInitPath

        Settings.objM.newPath = Settings.libraryNewPath

        Settings.objM.apiName = Settings.apiName
        Settings.objM.apiIndex = Settings.apiIndex
        Settings.objM.localManhuaTitleDict = Settings.localManhuaTitleDict

    def setPrefVariables() -> None:
        Settings.objP.compressionState = Settings.compressionState

        Settings.objP.updateChapter = Settings.updateChapter

        Settings.objP.updateOther = Settings.updateOther

        Settings.objP.themeButtonState = Settings.themeButtonState

        Settings.objP.hideNav = Settings.hideNav

        Settings.objP.fsState = Settings.fsState

        Settings.objP.readerDisplayIndex = Settings.readerDisplayIndex

        Settings.objP.initPath = Settings.downloadInitPath

        Settings.objP.newPath = Settings.downloadNewPath

        Settings.objP.initReaderState = [Settings.readerDisplayIndex, Settings.hideNav, Settings.fsState]

    def setReaderInits() -> None:
        Settings.objR.hideNav = Settings.hideNav

        Settings.objR.fsState = Settings.fsState

        Settings.objR.readerDisplayIndex = Settings.readerDisplayIndex
        Settings.objR.initReaderState = [Settings.readerDisplayIndex, Settings.hideNav, Settings.fsState]

    def setObjMState() -> None:
        Settings.apiIndex = Settings.objM.apiIndex
        Settings.objM.apiButton.setText(Settings.apiName[Settings.apiIndex])

    def setStates() -> None:
        Settings.setMainWindowVariables()
        Settings.setPrefVariables()
        Settings.setReaderInits()
        Settings.objR.selfInit()

        Settings.objM.apiCombo.addItems(Settings.apiName)

        Settings.objM.apiIndex = Settings.apiIndex
        Settings.setObjMState()

        Settings.objM.apiCombo.setCurrentIndex(Settings.objM.apiIndex)
        if Settings.apiIndex == 0:
            Settings.objM.setApiIndex(Settings.apiIndex)
        
        Settings.objP.downloadDirPathDisplay.setText(str(Settings.downloadNewPath))

        Settings.objP.compressArchiveToggleBtn.setChecked(Settings.objP.compressionState)

        Settings.objP.toggleOne.setChecked(Settings.objP.updateChapter)

        Settings.objP.toggleTwo.setChecked(Settings.objP.updateOther)

        Settings.objP.readerNavtoggle.setChecked(Settings.objP.hideNav)

        Settings.objP.readerFStoggle.setChecked(Settings.objP.fsState)

        Settings.objP.readerDisplayList[Settings.objP.readerDisplayIndex].setChecked(True)

        Settings.objP.themesBtn.setChecked(Settings.objP.themeButtonState)
        
