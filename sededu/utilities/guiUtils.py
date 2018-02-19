import os, subprocess, platform
import numpy as np
import json
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore


class NavButton(QPushButton):
    def __init__(self, category, thisPath, parent=None):
        QPushButton.__init__(self, parent)
        iPath = os.path.join(thisPath, "sededu", "private", \
        	category2path(category) + ".png")
        # print(category + " path: " + iPath)
        iIcon = QtGui.QIcon()
        iIcon.addPixmap(QtGui.QPixmap(iPath))
        self.setIcon(iIcon)
        # self.setIconSize(QtCore.QSize(300,200))
        self.setIconSize(QtCore.QSize(225, 150))


class CategoryList(QListWidget):
    def __init__(self, category, parent):
        QListWidget.__init__(self, parent)
        categoryPath = os.path.join(self.parent().parent().thisPath, \
            "sededu", "modules", category2path(category))
        self.itemClicked.connect(self.setCategoryItemInfo)
        self.bodyInfo = QStackedWidget()
        subDirs = subDirPath(categoryPath)
        idx = 0
        for iDir in subDirs:
            iData = json.load(open(os.path.join(iDir, "about.json")))
            # iStack = genInfo(iDir, iData)
            iStack = ModuleInfo(iDir, iData)
            iListItem = categoryListItem(idx, iData)
            self.addItem(iListItem)
            self.bodyInfo.addWidget(iStack)
            idx += 1

    def setCategoryItemInfo(self, item):
        self.bodyInfo.setCurrentIndex(item.idx)


### DEVELOPING BELOW, AS REPLACEMENT FOR CATEGORY LIST CLASS,
### THIS CLASS SHOULD BUILD ALL COMPONENETS FOR PAGE (WORKING ON DOCLIST NOW)
### THEN THE CATEGORYMENU CLASS CAN INDEX THEM BACK TO SELF.
class CategoryInfo(QWidget):
    def __init__(self, category, parent):
        QWidget.__init__(self, parent)
        categoryPath = os.path.join(self.parent().parent().thisPath, \
            "sededu", "modules", category2path(category))
        self.moduleList = QListWidget()
        self.moduleList.itemClicked.connect(self.setCategoryItemInfo)
        self.infoPageStack = QStackedWidget()
        self.docPageStack = QStackedWidget()
        subDirs = subDirPath(categoryPath)
        modIdx = 0
        for iDir in subDirs:
            iData = json.load(open(os.path.join(iDir, "about.json")))
            iInfoPage = ModuleInfo(iDir, iData)
            iListItem = categoryListItem(modIdx, iData)
            self.moduleList.addItem(iListItem)
            self.infoPageStack.addWidget(iInfoPage)

            docPath = os.path.join(iDir, *iData["docloc"])
            docList = iData["doclist"]
            launchList = [os.path.join(docPath, f) for f in list(docList.keys())]
            docIdx = 0
            iDocPage = QWidget()
            self.iDocList = QListWidget()
            iDocPageLayout = QVBoxLayout()
            iDocPageLayout.setContentsMargins(0, 0, 0,0)
            iDocPageLayout.addWidget(QLabel("Activities/worksheets available:"))
            iDocPageLayout.addWidget(self.iDocList)
            docLaunch = QPushButton("Open activity")
            docLaunch.clicked.connect(lambda: self.docLaunch(launchList))
            iInfoPage.infoLayout.insertWidget(6, docLaunch)
            for iDoc in docList:
                iDocInfo = iData["doclist"]
                iDocTitle = list(iDocInfo.values())[docIdx]
                iDocFile = list(iDocInfo.keys())[docIdx]
                self.iDocList.addItem(iDocTitle)
                docIdx += 1

            self.moduleList.setCurrentRow(0)
            self.iDocList.setCurrentRow(0)
            iDocPage.setLayout(iDocPageLayout)
            self.docPageStack.addWidget(iDocPage)
            modIdx += 1

    def setCategoryItemInfo(self, item):
        self.infoPageStack.setCurrentIndex(item.idx)
        self.docPageStack.setCurrentIndex(item.idx)

    def docLaunch(self, launchList):
        launchIdx = self.iDocList.currentRow()
        filename = launchList[launchIdx]
        platType = platform.system()
        if platType in {"Darwin", "Linux"}:
            subprocess.Popen(["xdg-open", filename])
        elif platType in {"Windows"}:
            subprocess.Popen(["open", filename])
        else:
            print("unknown platform type")


class ModuleInfo(QWidget):
    def __init__(self, modDirPath, data, parent=None):
        QWidget.__init__(self, parent)
        infoLayout = QVBoxLayout()
        infoLayout.setContentsMargins(10, 0, 0, 0)
        titleLabel = infoLabel(data["title"])
        titleLabel.setFont(titleFont())
        versionLabel = QLabel("version " + data["version"])
        versionLabel.setFont(versionFont())
        previewLabel = QLabel()
        previewPath = os.path.join(modDirPath, *data["preview"])
        previewLabel.setPixmap(QtGui.QPixmap(previewPath).scaled( \
        	350, 350, QtCore.Qt.KeepAspectRatio))
        previewLabel.setAlignment(QtCore.Qt.AlignCenter)
        authorLabel = infoLabel("Author(s): " + data["author"])
        descLabel = infoLabel("Description: " + data["shortdesc"])
        execButton = QPushButton("Run module")
        execPath = os.path.join(modDirPath, *data["exec"])
        execButton.clicked.connect(lambda: self.execModule(execPath))
        infoLayout.addWidget(titleLabel)
        infoLayout.addWidget(versionLabel)
        infoLayout.addWidget(previewLabel)
        infoLayout.addWidget(authorLabel)
        infoLayout.addWidget(descLabel)
        infoLayout.addStretch(1)
        infoLayout.addWidget(execButton)
        self.infoLayout = infoLayout
        self.setLayout(self.infoLayout)

    def execModule(self, path):
        subprocess.Popen(["python3", path])


class infoLabel(QLabel):
    def __init__(self, parent=None):
        # add support to pass a font, and default to basic text if none
        QLabel.__init__(self, parent)
        self.setWordWrap(True)
        # self.setFont(font)


def etcButton(btnStr):
    etcBtn = QPushButton(btnStr)
    return etcBtn

def categoryListItem(idx, data):
    item = QListWidgetItem(data["title"])
    item.idx = idx
    return item

def categoryItemSelected(self, item):
    item.setStackIdx()

def HLine(self):
    toto = QFrame()
    toto.setFrameShape(QFrame.HLine)
    toto.setFrameShadow(QFrame.Sunken)
    return toto

def VLine(self):
    toto = QFrame()
    toto.setFrameShape(QFrame.VLine)
    toto.setFrameShadow(QFrame.Sunken)
    return toto

## path definitions 
def subDirPath(d):
    # list of direct subdirectories
    return filter(os.path.isdir, [os.path.join(d,f) for f in os.listdir(d)])

def category2path(c):
    # convert category name to folder name
    # this is very specific now -- any way to generalize the folders to
    # case insensitive?
    return c.lower().replace(" ","").replace("\n","")

def filesList(d):
    # list files in directory
    return [f for f in os.listdir(d) if os.path.isfile(os.path.join(d, f))]

## font definitions
def versionFont():
    font = QtGui.QFont()
    font.setBold(False)
    font.setItalic(True)
    font.setPointSize(9)
    return font

def titleFont():
    font = QtGui.QFont()
    font.setBold(True)
    font.setItalic(False)
    font.setPointSize(14)
    return font

def cutTitle():
    # Use QFontMetrics to get measurements, 
    # e.g. the pixel length of a string using QFontMetrics.width().
    a=1