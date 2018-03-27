import sys, os
import numpy as np
import json
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from sededu.utilities import guiUtils as gui

class RootInit(QMainWindow):
    # determine path to private
    thisDir = os.path.dirname(__file__)
    thisPath = os.path.join(thisDir,'')
    privatePath = os.path.join(thisPath, "sededu", "private")

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.initializeGUI()
        self.setWindowTitle("SedEdu")
        self.setWindowIcon(QtGui.QIcon(os.path.join(self.privatePath, 
                           "sededuicon.png")))
        self.setGeometry(10, 10, 300, 500)


    def initializeGUI(self):
        main = MainMenu(self) # build MainMenu
        about = AboutMenu(self) # build AboutMenu
        riversMenu = CategoryMenu("Rivers", self)
        deltasMenu = CategoryMenu("Deltas", self)
        desertsMenu = CategoryMenu("Deserts", self)
        coastsMenu = CategoryMenu("Coasts", self)
        stratMenu = CategoryMenu("Stratigraphy", self)
        btmodsMenu = CategoryMenu("Behind the Modules", self)
        self.stack.addWidget(main)
        self.stack.addWidget(about)
        self.stack.addWidget(riversMenu)
        self.stack.addWidget(deltasMenu)
        self.stack.addWidget(desertsMenu)
        self.stack.addWidget(coastsMenu)
        self.stack.addWidget(stratMenu)
        self.stack.addWidget(btmodsMenu)
    
    def drawMain(self):
        self.stack.setCurrentIndex(0)

    def drawAbout(self):
        self.stack.setCurrentIndex(1)

    def drawNav(self, idx):
        self.stack.setCurrentIndex(idx)


class MainMenu(QWidget):
    # class for main menu
    def __init__(self, parent):
        super().__init__(parent)
        mainList = ["Rivers", "Deltas", "Deserts", "Coasts", 
            "Stratigraphy", "Behind the \nModules"] # read these from file?
         
        navBox = QGroupBox() # category navigation box, group title here
        nList = len(mainList)
        gridSize = [3, 2]
        # xPos = np.tile( range(gridSize[1]), (1, int(np.ceil(nList/gridSize[1]))) )
        cPos = [0, 1, 0, 1, 0, 1]
        rPos = [0, 0, 1, 1, 2, 2] # this needs to be figured out how to make in numpy...
        navLayout = QGridLayout()
        for i in range(nList):
            iButton = gui.NavButton(mainList[i], self.parent().thisPath)
            # iButton.clicked.connect(lambda x, i=i: self.parent().setCurrentIndex(i+2))
            iButton.clicked.connect(lambda x, i=i: self.parent().parent().drawNav(i+2))
            navLayout.addWidget(iButton, rPos[i], cPos[i])
        navBox.setLayout(navLayout)

        etcBox = gui.EtcBox("main", self)

        layout = QHBoxLayout()
        layout.addWidget(etcBox)
        layout.addWidget(gui.VLine(self))
        layout.addWidget(navBox, 100)
        self.setLayout(layout)


class AboutMenu(QWidget):
    # class for about page
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        etcBox = gui.EtcBox("about", self)
        
        readmeText = gui.ParseReadmeInfo(self.parent().thisPath)
        bodyBox = QGroupBox()
        bodyLayout = QVBoxLayout()
        categoryLabelText = gui.InfoLabel("About the SedEdu project:", gui.titleFont())
        descLabel = QLabel(readmeText.summary)
        descLabel.setWordWrap(True)
        bodyLayout.addWidget(categoryLabelText)
        bodyLayout.addWidget(descLabel)
        bodyLayout.addWidget(gui.InfoLabel(readmeText.license))
        bodyLayout.addStretch(1)
        bodyLayout.addWidget(gui.InfoLabel("Contributors:"))
        for c in readmeText.contributors:
            contrib = gui.InfoLabel(c)
            contrib.setContentsMargins(10, 0, 0, 0)
            bodyLayout.addWidget(contrib)

        bodyLayout.addStretch(2)
        bodyLayout.addWidget(gui.InfoLabel('For complete information visit \
            the [SedEdu project page](https://github.com/amoodie/sededu).', gui.titleFont()))
        bodyLayout.addStretch(10)
        bodyLayout.addWidget(gui.InfoLabel("SedEdu is supported by:"))
        bodyLayout.addWidget(gui.SupportedBox(self.parent().privatePath))
        
        bodyBox.setLayout(bodyLayout)
        
        layout = QHBoxLayout()
        layout.addWidget(etcBox)
        layout.addWidget(gui.VLine(self))
        layout.addWidget(bodyBox, 100)
        self.setLayout(layout)


class CategoryMenu(QWidget):
    # class for navigation menu
    def __init__(self, category, parent):
        # super().__init__(parent)
        QWidget.__init__(self, parent)

        categInfo = gui.CategoryInfo(category, self)
        moduleList = categInfo.moduleList
        infoPageStack = categInfo.infoPageStack
        docPageStack = categInfo.docPageStack

        categoryLabelText = gui.InfoLabel(gui.cutTitle(category + " modules:"), gui.titleFont())
        backBtn = QPushButton("Back to Main Menu")
        backBtn.clicked.connect(self.parent().drawMain)
        backBtn.setFixedSize(QtCore.QSize(200,40))
        backBtn.setFont(gui.subtitleFont())
        
        bodyLayout = QGridLayout()
        bodyLayout.addWidget(categoryLabelText, 0, 0)
        bodyLayout.addWidget(moduleList, 1, 0)
        bodyLayout.addWidget(docPageStack, 2, 0)
        bodyLayout.addWidget(infoPageStack, 0, 1, 4, 1)
        bodyLayout.addWidget(backBtn, 3, 0)
        bodyLayout.setContentsMargins(15, 15, 15, 15)
        self.setLayout(bodyLayout)

    def loop_modules():
        for i in self.parent().iDir:
            a=1




if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = RootInit()
    root.show()
    sys.exit(app.exec_())