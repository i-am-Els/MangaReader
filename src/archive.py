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


import zipfile, os
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
        if not os.path.exists(outPath):
            os.makedirs(outPath)
        rfileList = list()
        if zipfile.is_zipfile(self.path):
            with zipfile.ZipFile(self.path, mode='r') as archive:
                try:
                    # Edit the files name by slicing with / character
                    for x in archive.namelist():
                        if Path(x).suffix in ['.jpeg', '.jpg', '.png']:
                            archive.extract(x, outPath)
                except zipfile.BadZipFile:
                    caller.popDialog('badFile')
                except FileNotFoundError:
                    print("Something unexpected happened... ")

        else:
            caller.popDialog('none')
            return 0 

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

    def readAllContent(self):
        ...
