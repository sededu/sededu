# [Create a root window]

import sys, os
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from sededu import guiUtils as gui
# from sededu import src

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
        # build all categoryMenus here
        # # #
        # # #
        self.riversMenu = categoryMenu("rivers")
        self.stack.addWidget(self.main)
        self.stack.addWidget(self.riversMenu)
    
    def drawMain(self):
        # self.setLayout(mainLayout)
        self.stack.setCurrentIndex(0)

    def drawNav(self):
        # sender = self.sender()
        # print(navLayout)
        # print(sender.text)
        # self.setLayout(navLayout)
        self.stack.setCurrentIndex(1)

    def genNav(self, navFolder):
        # generate nav menu from folder information
        a = 1


class mainMenu(QWidget):
    # class for main menu
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        super().__init__()
        print(dir(self))
        mainList = ["Rivers", "Deltas", "Deserts", "Coasts", 
            "Stratigraphy", "Behind the \nModules"] # read these from file?
        mainN = range(len(mainList))
        mainLayout = QGridLayout() # layout for entire main menu
        
        navBox = QGroupBox() # category navigation box, group title here
        navLayout = gui.stdObjs.mainLayout(mainList, thisPath)
        navBox.setLayout(navLayout)

        etcBox = QGroupBox() # etc box, group title here
        etcLayout = QGridLayout()
        etcQuit = gui.stdObjs.etcButton("Quit")
        etcQuit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        etcAbout = gui.stdObjs.etcButton("About")
        etcAbout.clicked.connect(self.drawNav())

        etcLayout.addWidget(etcQuit, 0, 0)
        etcLayout.addWidget(etcAbout, 0, 1)
        etcBox.setLayout(etcLayout)

        layout = QGridLayout() #
        layout.addWidget(navBox, 0, 0, 1, 2)
        layout.addWidget(etcBox, 2, 0)
        self.setLayout(layout)

    def drawNav(self):
        # sender = self.sender()
        # print(navLayout)
        # print(sender.text)
        # self.setLayout(navLayout)
        self.stack.setCurrentIndex(1)

# def categoryMenu(self):
#     # class for navigation menu
#     # def __init__(self, parent=None):
#         # QWidget.__init__(self, parent)
#     label = QLabel("test label")
#     self.layout = QGridLayout() #
#     self.layout.addWidget(label, 0, 0)
#     return self



class categoryMenu(QWidget):
    # class for navigation menu
    def __init__(self, category, parent=None):
        QWidget.__init__(self, parent)
        label = QLabel("test label" + category)
        layout = QGridLayout() #
        layout.addWidget(label, 0, 0)
        self.setLayout(layout)






if __name__ == '__main__':
    # print("ismain")
    app = QApplication(sys.argv)
    root = rootInit()
    root.setWindowTitle("SedEdu")
    root.show()
    sys.exit(app.exec_())