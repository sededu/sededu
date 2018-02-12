# [Create a root window]

import sys, os
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from sededu import guiUtils as gui
# from sededu import src

class rootInit(QWidget):
    # determine path to private
    thisDir = os.path.dirname(__file__)
    thisPath = os.path.join(thisDir,'')

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.initializeGUI()

    def initializeGUI(self):
        self.main = mainMenu(self) # build mainMenu
        self.drawMain(self.main.layout) # set to mainMenu
        self.setGeometry(400, 400, 100, 300)
        # navTest = categoryMenu()
    
    def drawMain(self, mainLayout):
        self.setLayout(mainLayout)

    def drawNav(self, navLayout):
        sender = self.sender()
        print(navLayout)
        print(sender.text)
        self.setLayout(navLayout)


    def genNav(self, navFolder):
        # generate nav menu from folder information
        a = 1



def mainMenu(self):
    # class for main menu
    # def __init__(self, parent=None):
        # QWidget.__init__(self, parent)
        # super().__init__()
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
    # navTest = categoryMenu(self)
    etcAbout.clicked.connect(self.drawNav)

    etcLayout.addWidget(etcQuit, 0, 0)
    etcLayout.addWidget(etcAbout, 0, 1)
    etcBox.setLayout(etcLayout)

    self.layout = QGridLayout() #
    self.layout.addWidget(navBox, 0, 0, 1, 2)
    self.layout.addWidget(etcBox, 2, 0)
    return self



# class mainMenu(QWidget):
#     # class for main menu
#     def __init__(self, parent=None):
#         QWidget.__init__(self, parent)
#         # super().__init__()
#         mainList = ["Rivers", "Deltas", "Deserts", "Coasts", 
#             "Stratigraphy", "Behind the \nModules"] # read these from file?
#         mainN = range(len(mainList))
#         mainLayout = QGridLayout() # layout for entire main menu
        
#         navBox = QGroupBox() # category navigation box, group title here
#         navLayout = gui.stdObjs.mainLayout(mainList, thisPath)
#         navBox.setLayout(navLayout)

#         etcBox = QGroupBox() # etc box, group title here
#         etcLayout = QGridLayout()
#         etcQuit = gui.stdObjs.etcButton("Quit")
#         etcQuit.clicked.connect(QtCore.QCoreApplication.instance().quit)
#         etcAbout = gui.stdObjs.etcButton("About")
#         etcAbout.clicked.connect(self.drawNav(navTest.layout))

#         etcLayout.addWidget(etcQuit, 0, 0)
#         etcLayout.addWidget(etcAbout, 0, 1)
#         etcBox.setLayout(etcLayout)

#         self.layout = QGridLayout() #
#         self.layout.addWidget(navBox, 0, 0, 1, 2)
#         self.layout.addWidget(etcBox, 2, 0)

def categoryMenu(self):
    # class for navigation menu
    # def __init__(self, parent=None):
        # QWidget.__init__(self, parent)
    label = QLabel("test label")
    self.layout = QGridLayout() #
    self.layout.addWidget(label, 0, 0)
    return self



# class categoryMenu(QWidget):
#     # class for navigation menu
#     def __init__(self, parent=None):
#         QWidget.__init__(self, parent)
#         label = QLabel("test label")
#         self.layout = QGridLayout() #
#         self.layout.addWidget(label, 0, 0)






if __name__ == '__main__':
    # print("ismain")
    app = QApplication(sys.argv)
    root = rootInit()
    root.setWindowTitle("SedEdu")
    root.show()
    sys.exit(app.exec_())