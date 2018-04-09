import sys, os, subprocess, platform, re
import numpy as np
import json
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

import sededu.utilities as utls


class CategoryPageWidget(QWidget):
    # class for a single category page
    def __init__(self, category, parent):
        QWidget.__init__(self, parent)
        self.setLayout(QGridLayout())

        self.categoryPath = os.path.join(self.parent().thisPath, 
                                          "sededu", "modules", 
                                          utls.category2path(category))
        modulePathList = utls.subDirPath(self.categoryPath)

        self.ModuleList = self._ModuleListWidget(self)
        self.ModulePageStack = self._ModulePageStackWidget(self)
        self.ModuleDocStack = QStackedWidget()
        self.categoryLabelText = utls.OneLineInfoLabel(utls.cutTitle(category + " modules:"),
                                               utls.titleFont())

        self.layout().addWidget(self.categoryLabelText, 0, 0)
        self.layout().addWidget(self.ModuleList, 1, 0)
        self.layout().addWidget(self.ModuleDocStack, 2, 0)
        self.layout().addWidget(self.ModulePageStack, 0, 1, 4, 1)
        self.layout().setContentsMargins(15, 15, 15, 15)
        
        # loop through all the modules
        moduleNum = 0
        for iModuleDirectory in modulePathList:
            # check out and prepare the about.json file
            moduleAboutPath = os.path.join(iModuleDirectory, "about.json")
            if os.path.isfile(moduleAboutPath):
                # read the raw file
                moduleAboutRawText = open(moduleAboutPath)

                # get module metadata from the about.json file
                iModuleAbout = json.load(moduleAboutRawText)
    
                # check and add defaults to moduleAbout if needed
                iModuleAbout = self.validateModuleAbout(iModuleAbout, iModuleDirectory)
            
            # construct and add the item to the module list
            iModuleListItem = self._ModuleListItemWidget(moduleNum, iModuleAbout)
            self.ModuleList.addItem(iModuleListItem)
            self.ModuleList.setCurrentRow(0)

            # construct and add the info page to the stack
            iModuleInfoPage = self._ModuleInformationPage(iModuleDirectory, iModuleAbout)
            self.ModulePageStack.addWidget(iModuleInfoPage)

            # construct and add the doc page to the stack
            iModuleDocPath = os.path.join(iModuleDirectory, *iModuleAbout["docloc"])
            iModuleDocNames = iModuleAbout["doclist"]
            iModuleDocLaunchList = [os.path.join(iModuleDocPath, f) for 
                                    f in list(iModuleDocNames.keys())]
            iModuleDocPage = self._ModuleDocumentPage()
            self.ModuleDocStack.addWidget(iModuleDocPage)

            # construct and add the document list to the doc page
            iModuleDocList = self._DocumentListWidget(iModuleDocLaunchList)
            iModuleDocPage.layout().addWidget(iModuleDocList)

            # loop through the docs and add to the list 
            docNum = 0
            for iDoc in iModuleDocNames:
                iDocInfo = iModuleAbout["doclist"]
                iDocTitle = list(iDocInfo.values())[docNum]
                iDocFile = list(iDocInfo.keys())[docNum]
                iDocListItem = QListWidgetItem(iDocTitle)
                iDocListItem.setSizeHint(QtCore.QSize(100,30))
                iModuleDocList.addItem(iDocListItem)
                docNum += 1
            iModuleDocList.setCurrentRow(0)
            
            # create a document launcher button if docs
            if len(iModuleDocLaunchList) > 0:
                iModuleDocLaunchButton = QPushButton("Open activity")
                iModuleDocLaunchButton.clicked.connect(lambda x, lL=iModuleDocLaunchList: iModuleDocList.docLaunch(lL))
                # iModuleInfoPage.launchLayout.addWidget(iModuleDocLaunchButton, 0, 0)
                iModuleInfoPage.launchButtons.layout().addWidget(iModuleDocLaunchButton, 0, 0)

            # increment to next module
            moduleNum += 1


    def setModulePage(self, item):
        self.ModulePageStack.setCurrentIndex(item.idx)
        self.ModuleDocStack.setCurrentIndex(item.idx)

    def validateModuleAbout(self, moduleAbout, moduleDirectory):

        # delete any empty fields from the dictionary
        moduleAbout = {k: v for k, v in moduleAbout.items() if v}

        # in reqDict, value 'default' indicates to include key in info, otherwise print the value
        reqDict = {'title':'**Title not defined**', 'author':'The SedEdu contributors', 
                   'version':'1.0', 'shortdesc':'default', 'license': 'None',
                   'difficulty':11, 'exec':['bad_path_supplied']}
        for k, v in reqDict.items():
            isPresent = k in moduleAbout.keys()
            if not isPresent:
                print("Module missing necessary information in:")
                print(os.path.join(moduleDirectory, "about.json"))
                print("Required field:", k, "is missing\n")
                if v == 'default': # if default print:
                    moduleAbout[k] = "No " + k + " supplied" # set appr filler text
                else:
                    moduleAbout[k] = v
        return moduleAbout

    class _ModuleListWidget(QListWidget):
        def __init__(self, parent=None):
            QListWidget.__init__(self, parent)

            self.itemClicked.connect(self.parent().setModulePage)


    class _DocumentListWidget(QListWidget):
        def __init__(self, launchList, parent=None):
            QListWidget.__init__(self, parent)


        def docLaunch(self, launchList):
            launchIdx = self.currentRow()
            filename = launchList[launchIdx]
            utls.open_file(filename)


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
            self.setFont(utls.subtitleFont())


    class _ModuleDocumentPage(QWidget):
        def __init__(self, parent=None):
            QWidget.__init__(self, parent)

            self.setLayout(QVBoxLayout())
            self.layout().setContentsMargins(0, 0, 0, 0)
            self.layout().addWidget(QLabel("Activities/worksheets available:"))


    class _ModuleInformationPage(QWidget):
        def __init__(self, moduleDirectory, moduleAbout, parent=None):
            QWidget.__init__(self, parent)
            
            self.setLayout(QVBoxLayout())
            self.layout().setContentsMargins(10, 0, 0, 0)
            
            # handle required module fields
            titleLabel = self.ModuleTitleLabel(title=utls.cutTitle(moduleAbout["title"]))
            self.layout().addWidget(titleLabel)

            versionLabel = utls.OneLineInfoLabel("version " + moduleAbout["version"], utls.versionFont())
            self.layout().addWidget(versionLabel)

            previewLabel = self.ModulePreviewWidget(moduleDirectory=moduleDirectory, moduleAbout=moduleAbout)
            self.layout().addWidget(previewLabel)
            self.layout().addSpacing(10)

            authorLabel = self.GenericOptionalLabel('Author(s):', moduleAbout['author'])
            self.layout().addWidget(authorLabel)

            shortDescLabel = self.GenericOptionalLabel('Description:', moduleAbout['shortdesc'])
            self.layout().addWidget(shortDescLabel)

            licenseLabel = self.GenericOptionalLabel('License:', moduleAbout['license'])
            self.layout().addWidget(licenseLabel)


            # handle optional fields
            if 'longdesc' in moduleAbout:
                placeholder = 1

            if 'projurl' in moduleAbout:
                projurlLabel = self.GenericOptionalLabel('Proj. website:', moduleAbout['projurl'])
                self.layout().addWidget(projurlLabel)

            if 'projreadme' in moduleAbout:
                readmeLabel = self.GenericOptionalLabel('Proj. README:', os.path.join(moduleDirectory, *moduleAbout['projreadme']))
                self.layout().addWidget(readmeLabel)

            self.layout().addStretch(10)

            self.launchButtons = self.ModuleLaunchButtonsWidget(moduleDirectory=moduleDirectory, moduleAbout=moduleAbout, 
                                                           parent=self)
            self.layout().addWidget(self.launchButtons)





        def execModule(self, execPath):
            if os.path.isfile(execPath):
                subprocess.Popen(["python3", execPath])
            else:
                msg = NoFileMessageBox(execPath)
                msg.exec_()


        class ModuleTitleLabel(utls.ShortInfoLabel):
            # title widget
            titleFont = utls.titleFont()
            def __init__(self, title='', theFont=titleFont, parent=None):
                utls.ShortInfoLabel.__init__(self, title, theFont, parent)


        class GenericOptionalLabel(QGroupBox):
            def __init__(self, fieldLabel='', aboutText='', parent=None):
                QGroupBox.__init__(self, parent)
                self.setLayout(QHBoxLayout())
                self.setContentsMargins(0, 0, 0, 2)
                self.layout().setContentsMargins(0, 0, 0, 0)

                self.FieldLabel = utls.ShortInfoLabel(fieldLabel)
                self.FieldLabel.setMinimumWidth(115)
                self.FieldLabel.setSizePolicy(QSizePolicy(
                           QSizePolicy.Fixed,
                           QSizePolicy.Preferred))
                self.layout().addWidget(self.FieldLabel)

                self.AboutData = utls.ShortInfoLabel(aboutText)
                self.layout().addWidget(self.AboutData)


            def setFieldLabel(self, fieldLabel):
                self.FieldLabel.setText(fieldLabel)


            def setAboutText(self, aboutText):
                self.AboutText.setText(aboutText)


        class ModuleLaunchButtonsWidget(QGroupBox):
            def __init__(self, moduleDirectory, moduleAbout, parent=None):
                QGroupBox.__init__(self, parent)
                self.setLayout(QGridLayout())
                self.setFlat(True)
                self.layout().setContentsMargins(20, 0, 20, 10)
                
                execButton = QPushButton("Run module")
                execPath = os.path.join(moduleDirectory, *moduleAbout["exec"])
                execButton.clicked.connect(lambda: self.parent().execModule(execPath))
                self.layout().addWidget(QLabel(), 0, 0)
                self.layout().addWidget(execButton, 0, 1)

        class ModulePreviewWidget(QGroupBox):
            # preview widget, fills with blank if not given
            previewHeight = 250

            def __init__(self, moduleDirectory, moduleAbout, 
                         previewHeight=previewHeight, parent=None):
                QGroupBox.__init__(self, parent)
                self.setLayout(QVBoxLayout())
                self.layout().setContentsMargins(0, 0, 0, 0)
                self.setContentsMargins(0, 0, 0, 0)
                self.setMinimumHeight(previewHeight)
                self.setSizePolicy(QSizePolicy(
                           QSizePolicy.Preferred,
                           QSizePolicy.Fixed))

                previewLabel = QLabel()
                previewLabel.setContentsMargins(0, 0, 0, 0)
                self.layout().addWidget(previewLabel)

                if 'preview' in moduleAbout:
                    previewPath = os.path.join(moduleDirectory, *moduleAbout["preview"])
                    if os.path.isfile(previewPath): # check that pixmap exists
                        previewLabel.setPixmap(QtGui.QPixmap(previewPath).scaledToHeight(
                                               previewHeight).copy(QtCore.QRect(
                                               0,0,previewHeight*(4/3),previewHeight)))
                    else: # preview path supplied, but no image found
                        previewLabel.setText('** Image not found **')
                else: # no preview path supplied
                    previewLabel.setText('** Preview not provided **')
                previewLabel.setAlignment(QtCore.Qt.AlignCenter)

