import sys, os
import numpy as np
import json
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

from . import utilities as utls
from .base import MainBackgroundWidget, MainSideBarWidget, MainPageStackWidget
from .navigation import NavigationPageWidget
from .about import AboutPageWidget
from .category import CategoryPageWidget



class RootWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)

        # find the local path and folder information
        self._findPaths()

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
        MainBackground.layout().addWidget(utls.VLine())
        MainBackground.layout().addWidget(self.MainPageStack)

        # add the navigation and about page
        self.MainPageStack.addWidget(NavigationPage)
        self.MainPageStack.addWidget(AboutPage)

        self.MainPageStack.NavigationPage = NavigationPage
        self.MainPageStack.AboutPage = AboutPage

        # construct and add the category pages
        self.MainPageStack.categoryPageList = []
        for iCategory in self.categoryList:
            iCategoryPage = CategoryPageWidget(iCategory, self)
            self.MainPageStack.addWidget(iCategoryPage)
            self.MainPageStack.categoryPageList.append(iCategoryPage)

        # configure the main window header and size
        self.setWindowTitle('SedEdu')
        self.setWindowIcon(QtGui.QIcon(os.path.join(self.privatePath, 
                           'sededuicon.png')))
        self.setGeometry(10, 10, 300, 500)


    def _findPaths(self):
        # create paths used to locate files throughout
        fileDir = os.path.dirname(__file__)
        self.thisPath = os.path.join(fileDir,'')
        self.rootPath = os.path.join(fileDir, os.pardir,'')
        self.privatePath = os.path.join(self.thisPath, 'private')
        self.categoryList = ['Rivers and deltas', 'Landscapes', 'Deserts', 'Coasts', 
                             'Stratigraphy'] # read these from file?


    def _setMainPageStackIndex(self, idx):
        # change the index of the stack to idx
        self.MainPageStack.setCurrentIndex(idx)


    def navToMain(self, idx=0):
        # public alias to _setMainPageStackIndex, Main as default
        self._setMainPageStackIndex(idx=idx)
        self.MainSideBar.SideBarButtons.setAuxButtonToAbout()


    def navToAbout(self, idx=1):
        # public alias to _setMainPageStackIndex, About as default
        self._setMainPageStackIndex(idx=idx)
        self.MainSideBar.SideBarButtons.setAuxButtonToMain()


    def navToCategory(self, idx):
        # public alias to _setMainPageStackIndex, no default
        self._setMainPageStackIndex(idx=idx)
        self.MainSideBar.SideBarButtons.setAuxButtonToMain()



class Runner(object):
    def __init__(self):

        app = QApplication(sys.argv)
        root = RootWindow()
        root.show()
        sys.exit(app.exec_())




if __name__ == '__main__':
    runner = Runner()
