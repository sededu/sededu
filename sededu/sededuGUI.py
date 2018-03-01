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
        self.setWindowIcon(QtGui.QIcon(os.path.join(self.privatePath, "sededuicon.png")))
        self.setGeometry(10, 10, 900, 500)


    def initializeGUI(self):
        main = MainMenu(self) # build MainMenu
        about = AboutPage(self) # build AboutPage
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

    def drawNav(self, idx):
        print("idx = " + str(idx))
        self.stack.setCurrentIndex(idx)

    def drawAbout(self):
        self.stack.setCurrentIndex(1)


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
            iButton.clicked.connect(lambda x, i=i: self.parent().setCurrentIndex(i+2))
            navLayout.addWidget(iButton, rPos[i], cPos[i])
        navBox.setLayout(navLayout)

        etcBox = gui.EtcBox("main", self)

        layout = QHBoxLayout()
        layout.addWidget(etcBox)
        layout.addWidget(gui.VLine(self))
        layout.addWidget(navBox, 100)
        self.setLayout(layout)


class CategoryMenu(QWidget):
    # class for navigation menu
    def __init__(self, category, parent):
        QWidget.__init__(self, parent)
        
        categInfo = gui.CategoryInfo(category, self)
        moduleList = categInfo.moduleList
        infoPageStack = categInfo.infoPageStack
        docPageStack = categInfo.docPageStack

        categoryLabelText = gui.InfoLabel(category + " modules:")
        categoryLabelText.setFont(gui.titleFont())
        backBtn = gui.etcButton("Back to Main Menu")
        backBtn.clicked.connect(self.parent().drawMain)
        
        bodyLayout = QGridLayout()
        bodyLayout.addWidget(categoryLabelText, 0, 0)
        bodyLayout.addWidget(moduleList, 1, 0)
        bodyLayout.addWidget(docPageStack, 2, 0)
        bodyLayout.addWidget(infoPageStack, 0, 1, 4, 1)
        bodyLayout.addWidget(backBtn, 3, 0)
        self.setLayout(bodyLayout)


class AboutPage(QWidget):
    # class for about page
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        etcBox = gui.EtcBox("about", self)
        
        readmeText = gui.parseReadme(self.parent().thisPath)
        bodyBox = QGroupBox()
        # bodyBox.minimumSizeHint(400)
        # bodyBox.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        bodyLayout = QVBoxLayout()
        categoryLabelText = gui.InfoLabel("About the SedEdu project:")
        categoryLabelText.setFont(gui.titleFont())
        # descText = readmeText.summary
        descLabel = QLabel(readmeText.summary)
        descLabel.setWordWrap(True)
        # descLabel.setFixedWidth(400)
        bodyLayout.addWidget(categoryLabelText)
        bodyLayout.addWidget(descLabel)
        bodyLayout.addWidget(gui.InfoLabel(readmeText.license))
        bodyLayout.addWidget(gui.InfoLabel("Contributors:"))
        bodyLayout.addWidget(gui.InfoLabel(readmeText.contributors))
        bodyLayout.addStretch(10)
        bodyLayout.addWidget(gui.InfoLabel("Supported by:"))
        bodyLayout.addWidget(gui.SupportedBox(self.parent().privatePath))
        
        bodyBox.setLayout(bodyLayout)
        
        layout = QHBoxLayout()
        layout.addWidget(etcBox)
        layout.addWidget(gui.VLine(self))
        layout.addWidget(bodyBox, 100)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = RootInit()
    root.show()
    sys.exit(app.exec_())