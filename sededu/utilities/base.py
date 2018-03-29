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



class MainSideBarWidget(QGroupBox):
    def __init__(self, parent=None):
        QGroupBox.__init__(self, parent)
        # etcBox = QGroupBox() # etc box, group title here
        etcLayout = QVBoxLayout()
        etcLogo = QLabel() 
        etcLogo.setPixmap(QtGui.QPixmap(os.path.join(\
            self.parent().privatePath, "sededu.png")))
        etcDesc = gui.InfoLabel("a sediment-related educational activity suite", gui.titleFont())
        etcButtons = QGroupBox()
        etcButtonsLayout = QHBoxLayout()
        etcQuit = QPushButton("Quit")
        etcQuit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        # if aux_key in {"main"}:
        #     etcAuxButton = QPushButton("About")
        #     etcAuxButton.clicked.connect(self.parent().parent().drawAbout)
        # elif aux_key in {"about"}:
        #     etcAuxButton = QPushButton("Back")
        #     etcAuxButton.clicked.connect(self.parent().parent().drawMain)
        etcAuxButton = QPushButton("About")
        etcAuxButton.clicked.connect(self.parent().drawAbout)
        # elif aux_key in {"about"}:
        #     etcAuxButton = QPushButton("Back")
        #     etcAuxButton.clicked.connect(self.parent().parent().drawMain)
        etcButtonsLayout.addWidget(etcQuit)
        etcButtonsLayout.addWidget(etcAuxButton)
        etcButtons.setLayout(etcButtonsLayout)
        etcLayout.addWidget(etcLogo)
        etcLayout.addWidget(etcDesc)
        etcLayout.addStretch(100)
        etcLayout.addWidget(etcButtons)
        self.setLayout(etcLayout)