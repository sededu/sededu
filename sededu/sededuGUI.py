import sys, os
import numpy as np
import json
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from sededu.utilities import guiUtils as gui

from sededu.utilities.base import MainBackgroundWidget, MainSideBarWidget, MainPageStackWidget
from sededu.utilities.navigation import NavigationPageWidget
from sededu.utilities.about import AboutPageWidget
from sededu.utilities.category import CategoryPageWidget



class RootWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)

        # find the local path and folder information
        self.findPaths()

        # construct the central widget of the gui
        MainBackground = MainBackgroundWidget(self)
        self.setCentralWidget(MainBackground)

        # construct the sidebar and page stack
        self.MainPageStack = MainPageStackWidget(MainBackground)
        self.MainSideBar = MainSideBarWidget(self)

        # construct the navigation page and about page
        NavigationPage = NavigationPageWidget(self)
        AboutPage = AboutPageWidget(self)

        # add the side bar and page stack to the central widget
        MainBackground.layout().addWidget(self.MainSideBar)
        MainBackground.layout().addWidget(gui.VLine(self))
        MainBackground.layout().addWidget(self.MainPageStack)

        # add the navigation and about page
        self.MainPageStack.addWidget(NavigationPage)
        self.MainPageStack.addWidget(AboutPage)

        # construct and add the category pages
        for i in self.categoryList:
            iCategoryPage = CategoryPageWidget(i, self)
            self.MainPageStack.addWidget(iCategoryPage)

        # configure the main window header and size
        self.setWindowTitle("SedEdu")
        self.setWindowIcon(QtGui.QIcon(os.path.join(self.privatePath, 
                           "sededuicon.png")))
        self.setGeometry(10, 10, 300, 500)


    def findPaths(self):
        thisDir = os.path.dirname(__file__)
        self.thisPath = os.path.join(thisDir,'')
        self.privatePath = os.path.join(self.thisPath, "sededu", "private")
        self.categoryList = ["Rivers", "Deltas", "Deserts", "Coasts", 
            "Stratigraphy", "Behind the \nModules"] # read these from file?


    def _setMainPageStackIndex(self, idx):
        self.MainPageStack.setCurrentIndex(idx)


    def navToMain(self, idx=0):
        self._setMainPageStackIndex(idx=idx)
        self.MainSideBar.SideBarButtons.setAuxButtonToAbout()


    def navToAbout(self, idx=1):
        self._setMainPageStackIndex(idx=idx)
        self.MainSideBar.SideBarButtons.setAuxButtonToMain()


    def navToCategory(self, idx):
        self._setMainPageStackIndex(idx=idx)
        self.MainSideBar.SideBarButtons.setAuxButtonToMain()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = RootWindow()
    root.show()
    sys.exit(app.exec_())