import os, consts, re, resources
from linker import Link
from pathlib import Path

from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QIcon, QPixmap



def popDialog(type: str) -> None:
    if type == consts.E_DIALOG_EMPTY:
        txt, t_txt = "Bundle is empty, Please select a filled directory.", "Empty Bundle Error!"
        
    elif type == consts.E_DIALOG_STRUCTURE:
        txt, t_txt = "There are 2 scenarios that raise this error: Bundle Structure Error or No Image Found\nTip 1: Select a Parent folder that has chapters arranged in sub-folders.\nTip 2: The chapter sub-folders MUST contain images.", "Structure or File Error!"
        
    elif type == consts.E_DIALOG_BADFILE:
        txt, t_txt = "The supposed archive file might contain a bad or corrupted file...\nUnable to completely read archive.", "Bad/Corrupted Archive File!"
        
    elif type == consts.E_DIALOG_NONE:
        txt, t_txt = "Selected file is not a valid archive file. Select A readable archive file such as '.cbz', '.zip' files.", "Not an Archive File!"

    elif type == consts.E_DIALOG_DUPLICATE:
        txt, t_txt = "The manhua title already exists in your library, select another title.", "Duplicate Action!"

    elif type == consts.E_DIALOG_PERMISSION:
        txt, t_txt = "The system has denied permission to the selected folder.", "Permission Denied!"

    elif type == consts.E_DIALOG_DELETED_MANHUA:
        txt, t_txt = "The manhua bundle is no longer on drive. The path might be incorrect or the manhua has been deleted. The directory might also be folder-less or has no image in it's structure.", "Manhua not found on Drive!"

    elif type == consts.E_DIALOG_DELETED_CHAPTER:
        txt, t_txt = "The selected Chapter is no longer on drive or Does not contain any image file. It might also be empty. Check the above conditions...", "Unable to read Chapter!"

    elif type == consts.E_DIALOG_DELETED_IMAGE:
        txt, t_txt = "Image not Found, it must have been deleted just now.", "Missing Image!"

    elif type == consts.E_DIALOG_REGEX:
        txt, t_txt = "Directories failed the chapter regex test... \n[FIX] Rename at least one sub-directory of the bundle something like 'chapter 1', 'chap 1' or 'ch 1'", "ReGex Failed!"

    elif type == consts.E_DIALOG_FILE_NOT_FOUND:
        txt, t_txt = "File not Found. Make sure the Selected Path is still present on the drive.", "File Not Found"

    window_icon = QIcon()
    window_icon.addPixmap(QPixmap(resources.app_logo), QIcon.Mode.Normal, QIcon.State.Off)

    messageBox = QMessageBox()
    messageBox.setIcon(QMessageBox.Icon.Information)
    messageBox.setText(txt)
    messageBox.setWindowTitle(t_txt)
    messageBox.setStandardButtons(QMessageBox.StandardButton.Ok)
    messageBox.setWindowIcon(window_icon)
    messageBox.exec()


def correctDirStructure(path: str) -> bool:
    correct: bool = False
    imageExtList = consts.IMG_EXT_LIST

    for x in os.listdir(path):
        xPath = os.path.join(path, x)
        if os.path.isdir(xPath):
            correct = not(any(os.path.isdir(os.path.join(xPath, y)) == True for y in os.listdir(xPath))) and any((Path(os.path.join(xPath, y)).suffix in imageExtList) for y in os.listdir(xPath))
            if correct == True:
                break
    return correct

def addToMetaData(path: str, status: str) -> dict:
        
    imageExtList = consts.IMG_EXT_LIST
    manhuaMetaDict = dict()
    manhuaChapterList = list()

    manhuaMetaDict["ManhuaTitle"] = Path(path).stem
    manhuaMetaDict["ManhuaPath"] = str(path)
    emptyCover = True

    for x in os.listdir(path):
        xPath = os.path.join(path, x)
        if os.path.isdir(xPath) and any(Path(os.path.join(xPath, z)).suffix in imageExtList for z in os.listdir(xPath)):
                    # sChapterName = str(Path(xPath).name)
            sChapterName = Path(xPath).name
            manhuaChapterList.append(sChapterName)
        elif Path(xPath).suffix in ['.jpeg', '.jpg', '.png'] and emptyCover == True:
            manhuaMetaDict["ManhuaCover"] = xPath
            emptyCover = False
    if emptyCover == True:
        manhuaMetaDict["ManhuaCover"] = resources.default_cover_image

    if status == consts.E_STATUS_OFFLINE:
        manhuaMetaDict["Status"] = consts.E_STATUS_OFFLINE_TEXT
    elif status == consts.E_STATUS_ARCHIVE:
        manhuaMetaDict["Status"] = consts.E_STATUS_ARCHIVE_TEXT
        
    sortedManhuaChapterDict = sortChapters(manhuaChapterList)
    if sortedManhuaChapterDict != {}:
        manhuaMetaDict["Chapters"] = sortedManhuaChapterDict
        manhuaMetaDict["Description"] = consts.E_MW_TEXT_DUMMY_DESCRIPTION
        return manhuaMetaDict

def sortChapters(someList: list[str]) -> dict:
    try:
        newSortedDict = dict()
        initIndexHolderList = list()
        indexHolderList = list()
        chapterNameList = list()
        for item in someList:
            dTxt = re.findall(r"((ch+(ap)?(ter)?)+(\W|_)*(\d+(?:\.\d+)?))", str(item).casefold())
            desiredTxt = dTxt[0]
            initIndexHolderList.append(desiredTxt[-1])
            if '.' in desiredTxt[-1]:
                indexHolderList.append(float(desiredTxt[-1]))
            else:
                indexHolderList.append(int(desiredTxt[-1]))
            chapterName = 'Chapter ' + str(desiredTxt[-1])
            chapterNameList.append(chapterName)
        indexHolderList.sort()
        for i in indexHolderList:
            for j in initIndexHolderList:
                if str(i) == j:
                    ind = initIndexHolderList.index(j)
                    newSortedDict.update({chapterNameList[ind] : someList[ind]})
        return newSortedDict
    except IndexError:
        popDialog(consts.E_DIALOG_REGEX)
        return {}
        
def convertToPath(path: str) -> Path:
    path_n = Path(path)
    return path_n

def extractParentFolderPath(path: str) -> str:
    path_n = os.path.dirname(path)
    return path_n

def extractFileName(path: str) -> str:
    file_n = os.path.basename(path)
    return file_n
        