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


import consts

class Link(object):
    app = object()
    window = object()

    def setAppWindow(obj: any) -> None:
        Link.app = obj

    def setCreatorWindow(obj: any) -> None:
        Link.window = obj 

    def modifyAttribute(parent: str, attr:str, value: any) -> None:
        mObj = Link.typeTest(parent=parent)
        if hasattr(mObj, attr):
            setattr(mObj, attr, value)

    def fetchAttribute(parent: str, attr: str, _isMethod: bool = False) -> any:
        mObj = Link.typeTest(parent=parent)
        if _isMethod:
            value = getattr(mObj, attr)()
        else:
            value = getattr(mObj, attr, consts.EMPTY) 
        return value

    def callBackDeep(parent: str, attr: str, callBack: str, *value) -> None:
        mObj = Link.typeTest(parent=parent)
        if hasattr(mObj, attr):
            u = getattr(mObj, attr)
            x = getattr(u, callBack)
            x(*value)

    def callBack(parent: str, callBack: str, *value) -> None:
        mObj = Link.typeTest(parent=parent)
        u = getattr(mObj, callBack)
        u(*value)

    def typeTest(parent: str) -> any:
        mObj = object()
        if parent == consts.OBJ_MW_NAME:
            mObj = Link.window.objMainWindow
        elif parent == consts.OBJ_READER_NAME:
            mObj = Link.window.objReader
        elif parent == consts.OBJ_PREF_NAME:
            mObj = Link.window.objPref
        elif parent == consts.OBJ_LIB_NAME:
            mObj = Link.window.objMainWindow.library
        elif parent == consts.OBJ_WINDOW:
            mObj = Link.window
        elif parent == consts.OBJ_APP:
            mObj = Link.app
        return mObj
