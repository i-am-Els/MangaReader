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
import os

class Settings(object):
    def __init__(self, obj):
        super().__init__()
        self.obj = obj
        self.objM = self.obj.objMainWindow
        self.objP = self.obj.objPref
        self.objR = self.obj.objReader

        self.picklePath = str(os.path.join(Path.home(), "Manhua Reader"))

        if not os.path.exists(self.picklePath):
            os.makedirs(self.picklePath)

        
        self.libraryInitPath = "C:\\"
        self.libraryNewPath = self.libraryInitPath
        self.localManhuaTitleDict = dict()



        self.updateChapter = True
        self.updateOther = True
        self.hideNav = True
        self.fsState = True
        self.readerDisplayIndex = 1

        self.compressionState = True
        
        self.themeIndex = 0
        self.themeButtonState = False

        self.downloadInitPath = str(os.path.join(Path.home(), "Documents\\Manhua Reader"))

        if not os.path.exists(self.downloadInitPath):
            os.makedirs(self.downloadInitPath)

        self.downloadNewPath = self.downloadInitPath

        self.apiName = ['Asura Scan', 'Manhuabat', 'HolyManhua']
        self.apiIndex = 1
        
    def setMainWindowVariables(self):
        self.objM.initPath = self.libraryInitPath

        self.objM.newPath = self.libraryNewPath

        self.objM.apiName = self.apiName
        self.objM.apiIndex = self.apiIndex
        self.objM.localManhuaTitleDict = self.localManhuaTitleDict

    def setPrefVariables(self):
        self.objP.compressionState = self.compressionState

        self.objP.updateChapter = self.updateChapter

        self.objP.updateOther = self.updateOther

        self.objP.themeButtonState = self.themeButtonState

        self.objP.hideNav = self.hideNav

        self.objP.fsState = self.fsState

        self.objP.readerDisplayIndex = self.readerDisplayIndex

        self.objP.initPath = self.downloadInitPath

        self.objP.newPath = self.downloadNewPath

    def setObjMState(self):
        self.apiIndex = self.objM.apiIndex
        self.objM.apiButton.setText(self.apiName[self.apiIndex])

    def setStates(self):
        self.setMainWindowVariables()
        self.setPrefVariables()

        self.objM.apiCombo.addItems(self.apiName)

        self.objM.apiIndex = self.apiIndex
        self.setObjMState()

        self.objM.apiCombo.setCurrentIndex(self.objM.apiIndex)
        if self.apiIndex == 0:
            self.objM.setApiIndex(self.apiIndex)
        
        self.objP.downloadDirPathDisplay.setText(str(self.downloadNewPath))

        self.objP.compressArchiveToggleBtn.setChecked(self.objP.compressionState)

        self.objP.toggleOne.setChecked(self.objP.updateChapter)

        self.objP.toggleTwo.setChecked(self.objP.updateOther)

        self.objP.readerNavtoggle.setChecked(self.objP.hideNav)

        self.objP.readerFStoggle.setChecked(self.objP.fsState)

        self.objP.readerDisplayList[self.objP.readerDisplayIndex].setChecked(True)

        self.objP.themesBtn.setChecked(self.objP.themeButtonState)
        
    