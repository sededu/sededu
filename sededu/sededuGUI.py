import sys, os
import numpy as np
import json
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from sededu.utilities import guiUtils as gui

from sededu.utilities.base import MainBackgroundWidget, MainSideBarWidget, MainPageStackWidget
from sededu.utilities.navigation import NavigationPageWidget
from sededu.utilities.about import AboutPageWidget

class RootWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)

        MainBackground = MainBackgroundWidget()
        self.setCentralWidget(MainBackground)

        self.find_paths()

        MainSideBar = MainSideBarWidget(self)
        MainPageStack = MainPageStackWidget(self)

        MainBackground.layout().addWidget(MainSideBar)
        MainBackground.layout().addWidget(MainPageStack)

        NavigationPage = NavigationPageWidget(self)
        MainPageStack.addWidget(NavigationPage)

        AboutPage = AboutPageWidget(self)
        MainPageStack.addWidget(AboutPage)


        # self.initializeGUI()


        self.setWindowTitle("SedEdu")
        self.setWindowIcon(QtGui.QIcon(os.path.join(self.privatePath, 
                           "sededuicon.png")))
        self.setGeometry(10, 10, 300, 500)


    def find_paths(self):
        self.thisDir = os.path.dirname(__file__)
        self.thisPath = os.path.join(self.thisDir,'')
        self.privatePath = os.path.join(self.thisPath, "sededu", "private")

    def initializeGUI(self):
        a = 1
        # MainMenu = MainMenuWidget(self) # build MainMenuWidget
        # about = AboutMenu(self) # build AboutMenu
        # riversMenu = CategoryMenu("Rivers", self)
        # deltasMenu = CategoryMenu("Deltas", self)
        # desertsMenu = CategoryMenu("Deserts", self)
        # coastsMenu = CategoryMenu("Coasts", self)
        # stratMenu = CategoryMenu("Stratigraphy", self)
        # btmodsMenu = CategoryMenu("Behind the Modules", self)
        # self.stack.addWidget(MainMenu)
        # self.stack.addWidget(about)
        # self.stack.addWidget(riversMenu)
        # self.stack.addWidget(deltasMenu)
        # self.stack.addWidget(desertsMenu)
        # self.stack.addWidget(coastsMenu)
        # self.stack.addWidget(stratMenu)
        # self.stack.addWidget(btmodsMenu)
    

    # def drawMain(self):
    #     self.stack.setCurrentIndex(0)


    def drawAbout(self):
        self.parent().MainPageStack.setCurrentIndex(1)


    # def drawNav(self, idx):
    #     self.stack.setCurrentIndex(idx)



class MainMenuWidget(QWidget):
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







class CategoryMenu(QWidget):
    # class for navigation menu
    def __init__(self, category, parent):
        QWidget.__init__(self, parent)

        # self.categoryPath = os.path.join(self.parent().thisPath, 
        #                                   "sededu", "modules", 
        #                                   gui.category2path(category))
        # self.modulePathList = gui.subDirPath(self.categoryPath)

        # self.ModuleList = self.ModuleListWidget(self)
        # self.ModulePageStack = self.ModulePageStackWidget(self)
        # self.ModuleDocStack = QStackedWidget()
        
        # moduleNum = 0
        # for iModuleDirectory in self.modulePathList:
        #     iModuleAbout = json.load(open(os.path.join(iModuleDirectory, "about.json")))
            # iInfoPage = gui.ModuleInfoPage(iModuleDirectory, iModuleAbout)
            # iListItem = gui.categoryListItem(moduleNum, iModuleAbout)
            # self.moduleList.addItem(iListItem)
            # self.infoPageStack.addWidget(iInfoPage)


        categInfo = gui.CategoryInfo(category, self)
        moduleList = categInfo.moduleList
        infoPageStack = categInfo.infoPageStack
        docPageStack = categInfo.docPageStack

        categoryLabelText = gui.InfoLabel(gui.cutTitle(category + " modules:"),
                                          gui.titleFont())
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

    def loopModules(self):
        # for i in self.iDir:
        a=1

    class ModuleListWidget(QListWidget):
        def __init__(self, parent=None):
            QListWidget.__init__(self, parent)
            self.itemClicked.connect(self.parent().setCategoryItemInfo)

    class ModulePageStackWidget(QStackedWidget):
        def __init__(self, parent=None):
            QStackedWidget.__init__(self, parent)
            self.setSizePolicy(QSizePolicy(
                               QSizePolicy.MinimumExpanding,
                               QSizePolicy.Preferred))

    def setCategoryItemInfo(self, item):
        self.infoPageStack.setCurrentIndex(item.idx)
        self.docPageStack.setCurrentIndex(item.idx)


    def docLaunch(self, launchList):
        launchIdx = self.iDocList.currentRow()
        filename = launchList[launchIdx]
        
        open_file(filename)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = RootWindow()
    root.show()
    sys.exit(app.exec_())