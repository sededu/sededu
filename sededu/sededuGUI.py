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

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.root = QWidget()
        self.stack = QStackedWidget()
        rootLayout = QVBoxLayout()
        rootLayout.addWidget(self.stack)
        self.root.setLayout(rootLayout)
        self.setCentralWidget(self.root)

        self.initializeGUI()

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
        # self.setLayout(mainLayout)
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
        privatePath = os.path.join(self.parent().thisPath, "sededu", "private")
         
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

        ## need to stick this into a subclass and make it on the Category/AboutMenu too?
        etcBox = QGroupBox() # etc box, group title here
        etcLayout = QVBoxLayout()
        etcLogo = QLabel() 
        etcLogo.setPixmap(QtGui.QPixmap(os.path.join(privatePath, "sededu.png")))
        etcButtons = QGroupBox()
        etcButtonsLayout = QHBoxLayout()
        etcQuit = gui.etcButton("Quit")
        etcQuit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        etcAbout = gui.etcButton("About")
        etcAbout.clicked.connect(self.parent().drawAbout)
        etcButtonsLayout.addWidget(etcQuit)
        etcButtonsLayout.addWidget(etcAbout)
        etcButtons.setLayout(etcButtonsLayout)
        etcLayout.addWidget(etcLogo, QtCore.Qt.AlignTop)
        etcLayout.addStretch(100)
        etcLayout.addWidget(etcButtons)
        etcBox.setLayout(etcLayout)

        layout = QGridLayout() #
        layout.addWidget(navBox, 0, 2, 0, 4)
        layout.addWidget(etcBox, 0, 0)
        layout.addWidget(gui.VLine(self), 0, 1)
        self.setLayout(layout)


class CategoryMenu(QWidget):
    # class for navigation menu
    def __init__(self, category, parent):
        QWidget.__init__(self, parent)
        
        bodyModuleList = gui.CategoryList(category, self)
        bodyInfo = bodyModuleList.bodyInfo
        # bodyDocList = bodyModuleList.bodyDocList
        bodyDocList = QListWidget()
        bodyDocList.addItem(QListWidgetItem("doc1"))

        categoryLabelText = QLabel(category + " modules:")
        backBtn = gui.etcButton("Back")
        backBtn.clicked.connect(self.parent().drawMain)
        
        bodyLayout = QGridLayout()
        bodyLayout.addWidget(categoryLabelText, 0, 0)
        bodyLayout.addWidget(bodyModuleList, 1, 0)
        bodyLayout.addWidget(bodyDocList, 2, 0)
        bodyLayout.addWidget(bodyInfo, 0, 1, 3, 1)
        bodyLayout.addWidget(backBtn, 3, 0)
        self.setLayout(bodyLayout)


class AboutPage(QWidget):
    # class for about page
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        headBox = QGroupBox()
        headLayout = QVBoxLayout()
        # categoryLabelText = QLabel(category + " modules:")
        categoryLabelText = QLabel("About the SedEdu project:")
        headLayout.addWidget(categoryLabelText)
        backBtn = gui.etcButton("Back")
        backBtn.clicked.connect(self.parent().drawMain)
        headLayout.addWidget(backBtn)
        headBox.setLayout(headLayout)
        
        bodyBox = QGroupBox()
        bodyLayout = QGridLayout()
        descText = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod \
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, \
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo \
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse \
            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non \
            proident, sunt in culpa qui officia deserunt mollit anim id est laborum." 
        descLabel = QLabel(descText)
        descLabel.setWordWrap(True);
        bodyLayout.addWidget(descLabel)
        bodyBox.setLayout(bodyLayout)
        
        layout = QVBoxLayout()
        layout.addWidget(headBox)
        layout.addWidget(bodyBox)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = RootInit()
    root.setWindowTitle("SedEdu")
    root.show()
    sys.exit(app.exec_())