import sys, os, subprocess, platform, re
import numpy as np
import json
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from sededu.utilities import guiUtils as gui


class CategoryPageWidget(QWidget):
    # class for a single category page
    def __init__(self, category, parent):
        QWidget.__init__(self, parent)
        self.setLayout(QGridLayout())

        self.categoryPath = os.path.join(self.parent().thisPath, 
                                          "sededu", "modules", 
                                          gui.category2path(category))
        modulePathList = gui.subDirPath(self.categoryPath)

        self.ModuleList = self._ModuleListWidget(self)
        self.ModulePageStack = self._ModulePageStackWidget(self)
        self.ModuleDocStack = QStackedWidget()
        
        moduleNum = 0
        for iModuleDirectory in modulePathList:
            iModuleAbout = json.load(open(os.path.join(iModuleDirectory, "about.json")))
            
            # construct and add the item to the module list
            iModuleListItem = self._ModuleListItemWidget(moduleNum, iModuleAbout)
            self.ModuleList.addItem(iModuleListItem)
            self.ModuleList.setCurrentRow(0)

            # construct and add the info page to the stack
            iModuleInfoPage = self._ModuleInfoPage(iModuleDirectory, iModuleAbout)
            self.ModulePageStack.addWidget(iModuleInfoPage)

            # construct and add the doc page to the stack
            iModuleDocPath = os.path.join(iModuleDirectory, *iModuleAbout["docloc"])
            iModuleDocNames = iModuleAbout["doclist"]
            iModuleDocLaunchList = [os.path.join(iModuleDocPath, f) for 
                                    f in list(iModuleDocNames.keys())]
            
            docNum = 0
            iModuleDocPage = QWidget()
            iModuleDocList = QListWidget()
            iModuleDocPage.setLayout(QVBoxLayout())
            iModuleDocPage.layout().setContentsMargins(0, 0, 0, 0)
            iModuleDocPage.layout().addWidget(QLabel("Activities/worksheets available:"))
            iModuleDocPage.layout().addWidget(iModuleDocList)
            
            self.ModuleDocStack.addWidget(iModuleDocPage)

            iModuleDocLaunchButton = QPushButton("Open activity")
            iModuleDocLaunchButton.clicked.connect(lambda: self.docLaunch(iModuleDocLaunchList))
            if len(iModuleDocLaunchList) > 0:
                iModuleInfoPage.launchLayout.addWidget(iModuleDocLaunchButton, 0, 0)
            for iDoc in iModuleDocNames:
                iDocInfo = iModuleAbout["doclist"]
                iDocTitle = list(iDocInfo.values())[docNum]
                iDocFile = list(iDocInfo.keys())[docNum]
                iDocListItem = QListWidgetItem(iDocTitle)
                iDocListItem.setSizeHint(QtCore.QSize(100,30))
                iModuleDocList.addItem(iDocListItem)
                docNum += 1
            iModuleDocList.setCurrentRow(0)
            moduleNum += 1

            # add the widgets to the 



        categoryLabelText = gui.InfoLabel(gui.cutTitle(category + " modules:"),
                                          gui.titleFont())
        # backBtn = QPushButton("Back to Main Menu")
        # backBtn.clicked.connect(self.parent().drawMain)
        # backBtn.setFixedSize(QtCore.QSize(200,40))
        # backBtn.setFont(gui.subtitleFont())
        
        
        self.layout().addWidget(categoryLabelText, 0, 0)
        self.layout().addWidget(self.ModuleList, 1, 0)
        self.layout().addWidget(self.ModuleDocStack, 2, 0)
        self.layout().addWidget(self.ModulePageStack, 0, 1, 4, 1)
        self.layout().setContentsMargins(15, 15, 15, 15)


    def setModulePage(self, item):
        self.ModulePageStack.setCurrentIndex(item.idx)
        self.ModuleDocStack.setCurrentIndex(item.idx)


    def docLaunch(self, launchList):
        launchIdx = self.iModuleDocList.currentRow()
        filename = launchList[launchIdx]
        gui.open_file(filename)


    class _ModuleListWidget(QListWidget):
        def __init__(self, parent=None):
            QListWidget.__init__(self, parent)
            self.itemClicked.connect(self.parent().setModulePage)


    class _ModulePageStackWidget(QStackedWidget):
        def __init__(self, parent=None):
            QStackedWidget.__init__(self, parent)
            self.setSizePolicy(QSizePolicy(
                               QSizePolicy.MinimumExpanding,
                               QSizePolicy.Preferred))


    class _ModuleListItemWidget(QListWidgetItem):
        def __init__(self, idx, data):
            QListWidgetItem.__init__(self)
            self.setText(data["title"])
            self.idx = idx
            self.setSizeHint(QtCore.QSize(100,30))
            self.setFont(gui.subtitleFont())




    class _ModuleInfoPage(QWidget):
        def __init__(self, modDirPath, data, parent=None):
            QWidget.__init__(self, parent)
            infoLayout = QVBoxLayout()
            infoLayout.setContentsMargins(10, 0, 0, 0)
            optGroup = QGroupBox()
            optLayout = QGridLayout()
            optGroup.setLayout(optLayout)
            optGroup.setFlat(True)
            optLayout.setContentsMargins(2, 0, 2, 0)
            optLayout.setVerticalSpacing(10)
            # optLayout.setRowMinumumHeight(8)
            optLayout.setHorizontalSpacing(15)
            optLayoutInc = 0 # layout incrementer
            
            # check and add data if needed
            data = self.validateData(data, modDirPath)
            
            # handle required module fields
            titleLabel = gui.InfoLabel(gui.cutTitle(data["title"]), gui.titleFont())
            infoLayout.addWidget(titleLabel)
            versionLabel = gui.InfoLabel("version " + data["version"], gui.versionFont())
            infoLayout.addWidget(versionLabel)

            previewLabel = QLabel()
            previewHeight = 250
            if 'preview' in data:
                previewPath = os.path.join(modDirPath, *data["preview"])
                if os.path.isfile(previewPath): # check that pixmap exists
                    previewLabel.setPixmap(QtGui.QPixmap(previewPath).scaledToHeight(
                                           previewHeight).copy(QtCore.QRect(
                                           0,0,previewHeight*(4/3),previewHeight)))
                else: # preview path supplied, but no image found
                    previewLabel = gui.NoImageFiller("**Image not found**", previewHeight)
            else: # no preview path supplied
                previewLabel = gui.NoImageFiller("**Preview not provided**", previewHeight)
            previewLabel.setAlignment(QtCore.Qt.AlignCenter)
            infoLayout.addWidget(previewLabel)

            # handle optional module fields (replace with for loop with dict of keys?)
            optLayout.addWidget(QLabel("Author(s):"), optLayoutInc, 0, QtCore.Qt.AlignTop)
            optLayout.addWidget(gui.InfoLabel(data["author"]), optLayoutInc, 1)
            optLayoutInc = optLayoutInc + 1

            optLayout.addWidget(QLabel("Description:"), optLayoutInc, 0, QtCore.Qt.AlignTop)
            optLayout.addWidget(gui.InfoLabel(data["shortdesc"]), optLayoutInc, 1)
            optLayoutInc = optLayoutInc + 1

            # optLayoutInc = optLayoutInc + 1
            if 'projurl' in data:
                optLayout.addWidget(QLabel("Proj. website:"), optLayoutInc, 0, QtCore.Qt.AlignTop)
                projurlLabel = gui.InfoLabel(data["projurl"])
                optLayout.addWidget(projurlLabel, optLayoutInc, 1)
                optLayoutInc = optLayoutInc + 1

            if 'projreadme' in data:
                optLayout.addWidget(QLabel("Proj. README:"), optLayoutInc, 0, QtCore.Qt.AlignTop)
                readmeButton = QPushButton("open README")
                readmeButton.setFixedSize(QtCore.QSize(200,25))
                readmeButton.clicked.connect(lambda: open_file(os.path.join(modDirPath, *data["projreadme"])))
                optLayout.addWidget(readmeButton, optLayoutInc, 1, QtCore.Qt.AlignTop)

            infoLayout.addWidget(optGroup)

            launchGroup = QGroupBox()
            self.launchLayout = QGridLayout()
            launchGroup.setLayout(self.launchLayout)
            launchGroup.setFlat(True)
            self.launchLayout.setContentsMargins(20, 0, 20, 10)
            execButton = QPushButton("Run module")
            execPath = os.path.join(modDirPath, *data["exec"])
            execButton.clicked.connect(lambda: self.execModule(execPath))
            self.launchLayout.addWidget(QLabel(), 0, 0)
            self.launchLayout.addWidget(execButton, 0, 1)

            infoLayout.addStretch(1)
            infoLayout.addWidget(launchGroup)
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

