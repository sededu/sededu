# [Create a root window]

import sys, os
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from sededu.utilities import guiUtils as gui

class rootInit(QMainWindow):
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
        self.main = mainMenu(self) # build mainMenu
        self.about = aboutPage(self) # build aboutPage
        # build all categoryMenus here
        # # #
        # # #
        self.riversMenu = categoryMenu(self)
        self.stack.addWidget(self.main)
        self.stack.addWidget(self.about)
        self.stack.addWidget(self.riversMenu)
    
    def drawMain(self):
        # self.setLayout(mainLayout)
        self.stack.setCurrentIndex(0)

    def drawNav(self, idx):
        self.stack.setCurrentIndex(idx)

    def genNav(self, navFolder):
        # generate nav menu from folder information
        a = 1

    def drawAbout(self):
        self.stack.setCurrentIndex(1)


class mainMenu(QWidget):
    # class for main menu
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        mainList = ["Rivers", "Deltas", "Deserts", "Coasts", 
            "Stratigraphy", "Behind the \nModules"] # read these from file?
         
        navBox = QGroupBox() # category navigation box, group title here
        navLayout = gui.mainLayout(mainList, thisPath)
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


class categoryMenu(QWidget):
    # class for navigation menu
    def __init__(self, parent=None):
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


class aboutPage(QWidget):
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
    # print("ismain")
    app = QApplication(sys.argv)
    root = rootInit()
    root.setWindowTitle("SedEdu")
    root.show()
    sys.exit(app.exec_())