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


import zipfile, os, utilities
from pathlib import Path
from datetime import datetime
from PyQt6.QtWidgets import QWidget

path = Path(r"C:\Users\Eniola Olawale\Documents\Els\Study Room\Literatti\Graphics Novel\avatar\cbz\Avatar - The Last Airbender - The Promise Part 1 (2012) (digital) (Son of Ultron II-Empire).cbz")

path_2 = Path(r"C:\Users\Eniola Olawale\Documents\Els\Study Room\Literatti\Graphics Novel\avatar\cbz\Avatar - The Last Airbender - The Rift Part 1 (2014) (digital) (Son of Ultron II-Empire).cbz")


class Archiver:
    def __init__(self) -> None:
        pass

    def extractCbz(self, path: str | Path, outPath: str | Path, caller:QWidget) -> str | Path:
        if not os.path.exists(outPath):
            os.makedirs(outPath)
        
        if zipfile.is_zipfile(path):
            with zipfile.ZipFile(path, mode='r') as archive:
                try:
                    archive.extractall(outPath)
                    
                    for x in os.listdir(outPath):
                        ...
                        # if Path(x).suffix in ['.jpeg', '.jpg', '.png']:
                        #     print(x)
                    print(archive.printdir())
                except zipfile.BadZipFile:
                    #utilities.popDialog('badFile')
                    ...
                except FileNotFoundError:
                    print("Something unexpected happened...")
            return outPath

        else:
            #utilities.popDialog('none')
            return 0

    def writeNewCbz(self):
        with zipfile.ZipFile("hello.zip", mode="w") as archive:
            archive.write("hello.txt")
        print("Pop dialog Success!")

    def writeToCbz(self):
        with zipfile.ZipFile("hello.zip", mode="a") as archive:
            archive.write("hello.txt")
            # mode='a' is append, this will not truncate the files you have in the zip file before.

    def readAllContent(self):
        ...

# a = Archiver()
# a.extractCbz(path, r"C:\Users\Eniola Olawale\Documents\Manhua Reader\archives", None)
# a.extractCbz(path_2, r"C:\Users\Eniola Olawale\Documents\Manhua Reader\archives", None)