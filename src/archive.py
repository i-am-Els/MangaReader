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


import zipfile, os, utilities, consts
from pathlib import Path
from datetime import datetime
from PyQt6.QtWidgets import QWidget


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
                    if utilities.correctDirStructure(outPath):
                        pass
                    else:
                        newFolder = os.path.join(outPath, "chapter 0")
                        os.makedirs(newFolder, exist_ok=True)
                        for x in os.listdir(outPath):
                            xPath = os.path.join(outPath, x)
                            if Path(xPath).suffix in ['.jpeg', '.jpg', '.png']:
                                os.rename(xPath, os.path.join(newFolder, x))

                except zipfile.BadZipFile:
                    utilities.popDialog(consts.E_DIALOG_BADFILE)

                except FileNotFoundError:
                    utilities.popDialog(consts.E_DIALOG_FILE_NOT_FOUND)

            return outPath

        else:
            utilities.popDialog(consts.E_DIALOG_NONE)
            return 0

    def writeNewCbz(self):
        with zipfile.ZipFile("hello.zip", mode="w") as archive:
            archive.write("hello.txt")

    def writeToCbz(self):
        with zipfile.ZipFile("hello.zip", mode="a") as archive:
            archive.write("hello.txt")
            # mode='a' is append, this will not truncate the files you have in the zip file before.

    def readAllContent(self):
        ...
