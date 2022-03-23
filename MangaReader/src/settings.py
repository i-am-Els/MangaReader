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

        self.apiName = ['Asura Scan', 'Mangabat']
        self.apiIndex = 1
        

    def setMainWindowVariables(self):
        self.objM.initPath = self.libraryInitPath

        self.objM.newPath = self.libraryNewPath

        self.objM.apiName = self.apiName
        self.objM.apiIndex = self.apiIndex


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

        # print('donee')

    def setObjMState(self):
        self.apiIndex = self.objM.apiIndex
        self.objM.apiButton.setText(self.apiName[self.apiIndex])

    def setStates(self):
        self.setMainWindowVariables()
        self.setPrefVariables()
        
        self.objM.apiCombo.addItems(self.apiName)

        self.objM.apiIndex = self.apiIndex
        self.objM.apiCombo.setCurrentIndex(self.objM.apiIndex)

        self.setObjMState()
        
        self.objP.downloadDirPathDisplay.setText(str(self.downloadNewPath))

        self.objP.compressArchiveToggleBtn.setChecked(self.objP.compressionState)

        self.objP.toggleOne.setChecked(self.objP.updateChapter)

        self.objP.toggleTwo.setChecked(self.objP.updateOther)

        self.objP.readerNavtoggle.setChecked(self.objP.hideNav)

        self.objP.readerFStoggle.setChecked(self.objP.fsState)

        self.objP.readerDisplayList[self.objP.readerDisplayIndex].setChecked(True)

        self.objP.themesBtn.setChecked(self.objP.themeButtonState)
        

    