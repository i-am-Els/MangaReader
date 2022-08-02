import zipfile
from pathlib import Path
from datetime import datetime
from PyQt6.QtWidgets import QWidget

path = Path(r"C:\Users\User\Documents\Eniola Olawale\Manga\avatar\Avatar - The Last Airbender - North and South - Part 1 (2016) (Digital) (Raven).cbz")

path_2 = Path(r"C:\Users\User\Documents\Eniola Olawale\Manga\avatar\Avatar - The Last Airbender - Smoke and Shadow Part 1 (2015) (digital) (Son of Ultron-Empire).cbz")


class Archiver:
    def __init__(self) -> None:
        self.info = dict()
        self.path = ''

    def compressFile(self, path, outPath):
        ...

    def extractCbz(self, path, outPath, caller:QWidget) -> zipfile.ZipFile:
        self.path = path
        fileLists = list()
        if zipfile.is_zipfile(self.path):
            with zipfile.ZipFile(self.path, mode='r') as archive:
                archive.extractall(outPath)  
        else:
            caller.popDialog('none')
            return 0      
#           File "C:\Users\User\AppData\Local\Programs\Python\Python39\lib\zipfile. py", line 942, in _update_crc
#     raise BadZipFile("Bad CRC-32 for file %r" % self.name)
# zipfile.BadZipFile: Bad CRC-32 for file 'Classroom of the Elite - c003 (v01) - p089 [Seven Seas Entertainment] [Digital] [1r0n] {HQ}.jpg'

    def writeNewCbz(self):
        with zipfile.ZipFile("hello.zip", mode="w") as archive:
            archive.write("hello.txt")
        print("Pop dialog Success!")

    def writeToCbz(self):
        with zipfile.ZipFile("hello.zip", mode="a") as archive:
            archive.write("hello.txt")
            # mode='a' is append, this will not truncate the files you have in the zip file before.

    def getfileList(self, path):
        # You are expected to pass in the variable to the path of the zip
        with zipfile.ZipFile(path, mode="r") as archive:
            fileList = archive.namelist()
            count=0
            for x in fileList:
                if Path(x).suffix in ['.jpeg', '.jpg', '.png']:
                    count+=1
                    print(x,"\n")
            print(count)

    def readAllContent(self):
        ...
