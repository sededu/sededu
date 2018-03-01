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
        self.setIconSize(QtCore.QSize(300, 200))
        # self.setScaledContents(True)


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
                iDocListItem = QListWidgetItem(iDocTitle)
                iDocListItem.setSizeHint(QtCore.QSize(100,30))
                self.iDocList.addItem(iDocListItem)
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
        optGroup = QGroupBox()
        optLayout = QGridLayout()
        optGroup.setLayout(optLayout)
        # optLayout.setContentsMargins(0, 0, 0, 0)
        optLayoutInc = 0 # layout incrementer
        
        # check and add data if needed
        data = self.validateData(data)
        
        # handle required module fields
        titleLabel = InfoLabel(data["title"])
        titleLabel.setFont(titleFont())
        infoLayout.addWidget(titleLabel)
        versionLabel = QLabel("version " + data["version"])
        versionLabel.setFont(versionFont())
        infoLayout.addWidget(versionLabel)

        authorLabel = InfoLabel("Author(s): " + data["author"])
        descLabel = InfoLabel("Description: " + data["shortdesc"])
        optLayout.addWidget(authorLabel)
        optLayout.addWidget(descLabel)

        # add fields (widgets) if data is present
        previewLabel = QLabel()
        if 'preview' in data:
            previewPath = os.path.join(modDirPath, *data["preview"])
            if os.path.isfile(previewPath): # check that pixmap exists
                previewLabel.setPixmap(QtGui.QPixmap(previewPath).scaled( \
                    350, 350, QtCore.Qt.KeepAspectRatio))
            else: # preview path supplied, but no image found
                previewLabel.setText("**Image not found**")
        else: # no preview path supplied
            previewLabel.setText("**Preview not provided**")
        previewLabel.setAlignment(QtCore.Qt.AlignCenter)
        infoLayout.addWidget(previewLabel)

        infoLayout.addWidget(optGroup)

        execButton = QPushButton("Run module")
        execPath = os.path.join(modDirPath, *data["exec"])
        execButton.clicked.connect(lambda: self.execModule(execPath))
        
        
        
        

        infoLayout.addStretch(1)
        infoLayout.addWidget(execButton)
        self.infoLayout = infoLayout
        self.setLayout(self.infoLayout)

    def validateData(self, data):
        requiredList = ['title', 'version', 'author', 'shortdesc', 'exec']
        for k in requiredList:
            isPresent = k in data.keys()
            if not isPresent:
                print("Module missing necessary information in about.json\n")
                print("Required field: ", k, " is missing")
                print("Substituting filler text")        
                if not k == 'exec':
                    data[k] = "No " + k + " supplied" # set appr filler text
                else:
                    data[k] = False # set 'exec' to false
        if not 'difficulty' in data.keys():
            data['difficulty'] = 11 # default to end of list
        return data

    def execModule(self, path):
        if path:
            subprocess.Popen(["python3", path])
        else: # path is flase, no exec provided
            print('No exec supplied, nothing to execute...')

class InfoLabel(QLabel):
    def __init__(self, parent=None):
        # add support to pass a font, and default to basic text if none
        QLabel.__init__(self, parent)
        self.setWordWrap(True)
        # self.setFont(font)

class EtcBox(QGroupBox):
    def __init__(self, auxKey, parent=None):
        QGroupBox.__init__(self, parent)
        # etcBox = QGroupBox() # etc box, group title here
        etcLayout = QVBoxLayout()
        etcLogo = QLabel() 
        etcLogo.setPixmap(QtGui.QPixmap(os.path.join(\
            self.parent().parent().privatePath, "sededu.png")))
        etcDesc = InfoLabel("sediment-related educational activity suite")
        etcButtons = QGroupBox()
        etcButtonsLayout = QHBoxLayout()
        etcQuit = etcButton("Quit")
        etcQuit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        if auxKey in {"main"}:
            etcAuxButton = etcButton("About")
            etcAuxButton.clicked.connect(self.parent().parent().drawAbout)
        elif auxKey in {"about"}:
            etcAuxButton = etcButton("Back")
            etcAuxButton.clicked.connect(self.parent().parent().drawMain)
        etcButtonsLayout.addWidget(etcQuit)
        etcButtonsLayout.addWidget(etcAuxButton)
        etcButtons.setLayout(etcButtonsLayout)
        etcLayout.addWidget(etcLogo)
        etcLayout.addWidget(etcDesc)
        etcLayout.addStretch(100)
        etcLayout.addWidget(etcButtons)
        self.setLayout(etcLayout)


def etcButton(btnStr):
    etcBtn = QPushButton(btnStr)
    return etcBtn

def categoryListItem(idx, data):
    item = QListWidgetItem(data["title"])
    item.idx = idx
    item.setSizeHint(QtCore.QSize(100,30))
    return item

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


class SupportedBox(QWidget):
    def __init__(self, privatePath, parent=None):
        QWidget.__init__(self, parent)
        supportLayout = QHBoxLayout()
        nsfLogo = self.logoPixmap(os.path.join(privatePath, "nsf.gif"))
        riceLogo = self.logoPixmap(os.path.join(privatePath, "rice.png"))
        supportLayout.addWidget(nsfLogo)
        supportLayout.addWidget(riceLogo)
        supportLayout.addStretch(100)
        self.setLayout(supportLayout)

    def logoPixmap(self, path):
        logo = QLabel()
        logo.setPixmap(QtGui.QPixmap(path).scaledToHeight(100))
        return logo


## one off utils
def parseReadme(path):
    self = type('readmeData', (object,), {})()
    self.readmePath = os.path.join(path, "README.md")
    self.raw = open(self.readmePath, 'rt')
    self.lines = [l.replace("\n","").replace("*","") for l in self.raw]
    self.summaryIdx = self.lines.index("# SedEdu") + 2
    self.summary = self.lines[self.summaryIdx]
    self.licenseIdx = self.lines.index("## License") + 2
    licenseUrl = "<a href=\"https://github.com/amoodie/sededu/blob/master/LICENSE.md\">\
        full license</a>"
    self.license = self.lines[self.licenseIdx].replace("[LICENSE.md](LICENSE.md)", licenseUrl)
    self.contributorsIdx = self.lines.index("## Authors") + 2
    contributorsRaw = self.lines[self.contributorsIdx:self.licenseIdx-4]
    self.contributors = "\n".join(contributorsRaw)
    # print(self.license)
    # close(self.readmePath)
    return(self)

## path definitions / file finders
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

## font definitions / text modifiers
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
    # cut the titles down to textextext... for the list widgets
    a=1