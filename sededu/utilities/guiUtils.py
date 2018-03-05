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
        iIcon = QtGui.QIcon()
        iIcon.addPixmap(QtGui.QPixmap(iPath))
        self.setIcon(iIcon)
        self.setIconSize(QtCore.QSize(300, 200))



class CategoryInfo(QWidget):
    def __init__(self, category, parent):
        QWidget.__init__(self, parent)
        categoryPath = os.path.join(self.parent().parent().thisPath, \
            "sededu", "modules", category2path(category))
        self.moduleList = QListWidget()
        self.moduleList.itemClicked.connect(self.setCategoryItemInfo)
        self.infoPageStack = QStackedWidget()
        self.infoPageStack.setSizePolicy(QSizePolicy(
                                         QSizePolicy.MinimumExpanding,
                                         QSizePolicy.Preferred))
        self.docPageStack = QStackedWidget()
        subDirs = subDirPath(categoryPath)
        modIdx = 0
        for iDir in subDirs:
            iData = json.load(open(os.path.join(iDir, "about.json")))
            iInfoPage = ModuleInfoPage(iDir, iData)
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
            iDocPageLayout.setContentsMargins(0, 0, 0, 0)
            iDocPageLayout.addWidget(QLabel("Activities/worksheets available:"))
            iDocPageLayout.addWidget(self.iDocList)
            docLaunch = QPushButton("Open activity")
            docLaunch.clicked.connect(lambda: self.docLaunch(launchList))
            if len(launchList) > 0:
                iInfoPage.infoLayout.insertWidget(6, docLaunch) # THIS IS WHERE THE BUTTON SLIPS IN
                # iInfoPage.infoLayout.goButtonLayout.insertWidget(0, docLaunch) # THIS IS WHERE THE BUTTON SLIPS IN
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
        if os.path.isfile(filename):
            if platType in {"Darwin", "Linux"}:
                subprocess.Popen(["xdg-open", filename])
            elif platType in {"Windows"}:
                subprocess.Popen(["open", filename])
            else:
                print("unknown platform type")
        else:
            msg = NoFileMessageBox(filename)
            msg.exec_()
        


class ModuleInfoPage(QWidget):
    def __init__(self, modDirPath, data, parent=None):
        QWidget.__init__(self, parent)
        infoLayout = QVBoxLayout()
        infoLayout.setContentsMargins(10, 0, 0, 0)
        optGroup = QGroupBox()
        optLayout = QGridLayout()
        optGroup.setLayout(optLayout)
        optGroup.setFlat(True)
        optLayout.setContentsMargins(2, 0, 2, 0)
        optLayoutInc = 0 # layout incrementer
        
        # check and add data if needed
        data = self.validateData(data, modDirPath)
        
        # handle required module fields
        titleLabel = InfoLabel(cutTitle(data["title"]), titleFont())
        infoLayout.addWidget(titleLabel)
        versionLabel = InfoLabel("version " + data["version"], versionFont())
        infoLayout.addWidget(versionLabel)

        previewLabel = QLabel()
        if 'preview' in data:
            previewHeight = 250
            previewPath = os.path.join(modDirPath, *data["preview"])
            if os.path.isfile(previewPath): # check that pixmap exists
                previewLabel.setPixmap(QtGui.QPixmap(previewPath).scaledToHeight(
                                       previewHeight).copy(QtCore.QRect(
                                       0,0,previewHeight*(4/3),previewHeight)))
            else: # preview path supplied, but no image found
                previewLabel = NoImageFiller("**Image not found**", previewHeight)
        else: # no preview path supplied
            previewLabel = NoImageFiller("**Preview not provided**", previewHeight)
        previewLabel.setAlignment(QtCore.Qt.AlignCenter)
        infoLayout.addWidget(previewLabel)

        # handle optional module fields (replace with for loop with dict of keys?)
        optLayout.addWidget(QLabel("Author(s):"), optLayoutInc, 0, QtCore.Qt.AlignTop)
        optLayout.addWidget(InfoLabel(data["author"]), optLayoutInc, 1)
        optLayoutInc = optLayoutInc + 1

        optLayout.addWidget(QLabel("Description:"), optLayoutInc, 0, QtCore.Qt.AlignTop)
        optLayout.addWidget(InfoLabel(data["shortdesc"]), optLayoutInc, 1)
        optLayoutInc = optLayoutInc + 1

        # if 'projurl' in data:

        infoLayout.addWidget(optGroup)

        execButton = QPushButton("Run module")
        execPath = os.path.join(modDirPath, *data["exec"])
        execButton.clicked.connect(lambda: self.execModule(execPath))
        # goButtonLayout.addWidget(execButton)

        infoLayout.addStretch(1)
        infoLayout.addWidget(execButton)
        self.infoLayout = infoLayout
        self.setLayout(self.infoLayout)


    def validateData(self, data, modDirPath):
        # in reqDict, value 'default' indicates to include key in info, otherwise print the value
        reqDict = {'title':'default', 'version':'1.0', 'author':'The SedEdu contributors', 
                   'shortdesc':'default', 'exec':['bad_path_supplied'], 'difficulty':11}
        for k, v in reqDict.items():
            isPresent = k in data.keys()
            if not isPresent:
                print("Module missing necessary information in:")
                print(os.path.join(modDirPath, "about.json"))
                print("Required field:", k, "is missing\n")
                if v == 'default': # if default print:
                    data[k] = "No " + k + " supplied" # set appr filler text
                else:
                    data[k] = v
        return data


    def execModule(self, execPath):
        if os.path.isfile(execPath):
            subprocess.Popen(["python3", execPath])
        else:
            msg = NoFileMessageBox(execPath)
            msg.exec_()



class NoFileMessageBox(QMessageBox):
    # warning nofile mesage box, path is a required arg.
    # custom text can be passed as string mainText
    default = 'There was no file found at the specified path.\n\n'

    def __init__(self, givenPath, mainText=default, 
                 informText=False, parent=None):
        QMessageBox.__init__(self, parent)
        self.setIcon(QMessageBox.Critical)
        self.setText(mainText)
        if informText:
            self.setInformativeText(informText)
        self.setDetailedText(' '.join(['Path given:\n\n', givenPath]))
        self.setWindowTitle("Error")
        self.setStandardButtons(QMessageBox.Ok)



class NoImageFiller(QGroupBox):
    # filler image, takes text for label
    def __init__(self, labelText, previewHeight, parent=None):
        QGroupBox.__init__(self, parent)
        label = QLabel(labelText)
        label.setAlignment(QtCore.Qt.AlignCenter)
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        self.setMinimumHeight(previewHeight)
        self.setSizePolicy(QSizePolicy(
                           QSizePolicy.Preferred,
                           QSizePolicy.Fixed))



class InfoLabel(QLabel):
    # add support to pass a font, and default to basic text if none
    defaultFont = QtGui.QFont()
    def __init__(self, labelText='', theFont=defaultFont, parent=None):
        QLabel.__init__(self, parent)
        self.setText(labelText)
        self.setWordWrap(True)
        self.setSizePolicy(QSizePolicy(
                           QSizePolicy.MinimumExpanding,
                           QSizePolicy.Preferred))
        self.setFont(theFont)



class EtcBox(QGroupBox):
    def __init__(self, aux_key, parent=None):
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
        if aux_key in {"main"}:
            etcAuxButton = etcButton("About")
            etcAuxButton.clicked.connect(self.parent().parent().drawAbout)
        elif aux_key in {"about"}:
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


def cutTitle(text0):
    # Use QFontMetrics to get measurements, 
    # e.g. the pixel length of a string using QFontMetrics.width().
    # cut the titles down to textextext... for the list widgets

    # also removes word module from end of string if two present
    splt_t0 = text0.split()
    spltend_t0 = splt_t0[-2:]
    nospec_t0 = [ [''.join(e for e in x if e.isalnum()).lower()] 
                 for x in spltend_t0 ]
    if nospec_t0[0] == nospec_t0[1]: # if last two words are same (i.e., 'modules')
        text = ' '.join(splt_t0[:-1]) + ":"
    else:
        text = text0
    return text