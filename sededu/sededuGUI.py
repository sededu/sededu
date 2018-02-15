import sys, os
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from sededu.utilities import guiUtils as gui

class RootInit(QMainWindow):
    # determine path to private
    thisDir = os.path.dirname(__file__)
    thisPath = os.path.join(thisDir,'')

    def __init__(self, parent=None):
        # QWidget.__init__(self, parent)
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
        # build all categoryMenus here
        riversMenu = CategoryMenu(self)
        # # #
        # # #
        self.stack.addWidget(main)
        self.stack.addWidget(about)
        self.stack.addWidget(riversMenu)
    
    def drawMain(self):
        # self.setLayout(mainLayout)
        self.stack.setCurrentIndex(0)

    def drawNav(self, idx):
        print("idx = " + str(idx))
        # self.stack.setCurrentIndex(idx)

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
            iCapture = lambda x, i=i: i+1
            iI = iCapture(i)
            print(str(iI))
            # iButton.clicked.connect(lambda: print(self.__class__.__name__ + str(iI)))
            iButton.clicked.connect(lambda: self.drawNav)
            navLayout.addWidget(iButton, rPos[i], cPos[i])
            # backBtn.clicked.connect(self.parent().drawNav)
            # print(type(self).__name__)

            # lambda: self.AddControl('fooData')

        # navLayout = gui.mainLayout(mainList, thisPath)
        navBox.setLayout(navLayout)

        etcBox = QGroupBox() # etc box, group title here
        etcLayout = QGridLayout()
        etcQuit = gui.etcButton("Quit")
        etcQuit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        etcAbout = gui.etcButton("About")
        etcAbout.clicked.connect(self.parent().drawAbout)

        etcLayout.addWidget(etcQuit, 0, 0)
        etcLayout.addWidget(etcAbout, 0, 1)
        etcBox.setLayout(etcLayout)

        layout = QGridLayout() #
        layout.addWidget(navBox, 0, 2, 0, 4)
        layout.addWidget(etcBox, 0, 0)
        layout.addWidget(gui.VLine(self), 0, 1)
        self.setLayout(layout)


class CategoryMenu(QWidget):
    # class for navigation menu
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        
        headBox = QGroupBox()
        headLayout = QVBoxLayout()
        # categoryLabelText = QLabel(category + " modules:")
        categoryLabelText = QLabel("brokenPipe" + " modules:")
        headLayout.addWidget(categoryLabelText)
        backBtn = gui.etcButton("Back")
        backBtn.clicked.connect(self.parent().drawMain)
        headLayout.addWidget(backBtn)
        headBox.setLayout(headLayout)
        
        bodyBox = QGroupBox()
        bodyLayout = QGridLayout()
        bodyLayout.addWidget(QListWidget(), 0, 0, 2, 0)
        bodyLayout.addWidget(QStackedWidget(), 0, 1, 2, 2)
        bodyBox.setLayout(bodyLayout)
        
        layout = QVBoxLayout()
        layout.addWidget(headBox)
        layout.addWidget(bodyBox)
        self.setLayout(layout)

    def genNav(self, navFolder):
        # generate nav menu from folder information
        a = 1

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
        bodyLayout.addWidget(QLabel("fill this with text"))
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