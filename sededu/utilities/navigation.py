import sys, os
import numpy as np
import json
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from sededu.utilities import guiUtils as gui


class NavigationPageWidget(QWidget):
    # class for navigation button page
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

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
            iButton = CategoryButtonWidget(mainList[i], self.parent().thisPath)
            # iButton.clicked.connect(lambda x, i=i: self.parent().setCurrentIndex(i+2))
            # iButton.clicked.connect(lambda x, i=i: self.parent().drawNav(i+2))
            # iButton.clicked.connect(lambda x, i=i: self.parent().set_MainPageStackIndex(i+2))
            iButton.clicked.connect(lambda x, i=i: self.parent().setCurrentIndex(i+2))
            navLayout.addWidget(iButton, rPos[i], cPos[i])
        navBox.setLayout(navLayout)

        # etcBox = gui.EtcBox("main", self)

        layout = QHBoxLayout()
        # layout.addWidget(etcBox)
        layout.addWidget(gui.VLine(self))
        layout.addWidget(navBox, 100)
        self.setLayout(layout)




class CategoryButtonWidget(QPushButton):
    def __init__(self, category, thisPath, parent=None):
        QPushButton.__init__(self, parent)
        iPath = os.path.join(thisPath, "sededu", "private", \
            gui.category2path(category) + ".png")
        iIcon = QtGui.QIcon()
        iIcon.addPixmap(QtGui.QPixmap(iPath))
        self.setIcon(iIcon)
        self.setIconSize(QtCore.QSize(300, 200))
        self.setSizePolicy(QSizePolicy(
                           QSizePolicy.Maximum,
                           QSizePolicy.Maximum))