import sys, os
import numpy as np
import json
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from sededu.utilities import guiUtils as gui



class MainBackgroundWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setLayout(QHBoxLayout())



class MainSideBarWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QVBoxLayout())
        self.setSizePolicy(QSizePolicy(
                   QSizePolicy.Maximum,
                   QSizePolicy.Preferred))

        self.SideBarHeader = self._SideBarHeaderWidget(self)
        self.SideBarButtons = self._SideBarButtonsWidget(self)

        self.layout().addWidget(self.SideBarHeader)
        self.layout().addStretch(100)
        self.layout().addWidget(self.SideBarButtons)


    class _SideBarHeaderWidget(QGroupBox):
        def __init__(self, parent=None):
            QGroupBox.__init__(self, parent)
            self.setLayout(QVBoxLayout())

            Logo = self.make_Logo()
            Desc = self.make_Desc()
            
            self.layout().addWidget(Logo)
            self.layout().addWidget(Desc)
            self.setAlignment(QtCore.Qt.AlignLeft)


        def make_Logo(self):
            Logo = QLabel() 
            Logo.setPixmap(QtGui.QPixmap(os.path.join(\
                self.parent().parent().privatePath, "sededu.png")))
            return Logo


        def make_Desc(self):
            Desc = gui.InfoLabel("a sediment-related educational activity suite", 
                                 gui.titleFont())
            return Desc


    class _SideBarButtonsWidget(QGroupBox):
        def __init__(self, parent=None):
            QGroupBox.__init__(self, parent)
            self.setLayout(QHBoxLayout())

            self.Quit = QPushButton("Quit")
            self.Quit.clicked.connect(QtCore.QCoreApplication.instance().quit)
            self.layout().addWidget(self.Quit)

            self.AuxButton = QPushButton("About")
            self.setAuxButtonToAbout()
            self.layout().addWidget(self.AuxButton)
            

        def setAuxButtonToAbout(self):
            self.AuxButton.setText("About")
            self.AuxButton.clicked.connect(lambda: self.parent().parent().parent().navToAbout(idx=1))


        def setAuxButtonToMain(self):
            self.AuxButton.setText("Back")
            self.AuxButton.clicked.connect(lambda: self.parent().parent().parent().navToMain())



class MainPageStackWidget(QStackedWidget):
    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent)

        # self.setSizePolicy(QSizePolicy(
        #                    QSizePolicy.MinimumExpanding,
        #                    QSizePolicy.Preferred))
