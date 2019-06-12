import sys, os
import numpy as np
import json
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

from . import utilities as utls



class MainBackgroundWidget(QWidget):
    # the central blank widget that everything sits on
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setLayout(QHBoxLayout())



class MainSideBarWidget(QWidget):
    # main sidebar
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
        # the sidebar header (logo and subtitle)
        def __init__(self, parent=None):
            QGroupBox.__init__(self, parent)
            self.setLayout(QVBoxLayout())

            self.Logo = self.makeLogo()
            self.Desc = self.makeDesc()
            self.Vers = self.makeVers()
            
            self.layout().addWidget(self.Logo)
            self.layout().addWidget(self.Desc)
            self.layout().addWidget(self.Vers)
            self.setAlignment(QtCore.Qt.AlignLeft)


        def makeLogo(self):
            Logo = QLabel()
            try:
                LogoPath = os.path.join(self.parent().parent().privatePath, 
                                        'sededu.png')
                Logo.setPixmap(QtGui.QPixmap(LogoPath))
            except:
                Logo.setText('**logo not found**')
            return Logo


        def makeDesc(self):
            Desc = utls.ShortInfoLabel('a sediment-related\neducational activity suite', 
                                 utls.titleFont())
            return Desc


        def makeVers(self):
            try:
                from ._version import __version__
            except ImportError:
                __version__ = "unknown"
            Vers = utls.ShortInfoLabel("version " + __version__, utls.versionFont())
            return Vers


    class _SideBarButtonsWidget(QGroupBox):
        # buttons at the bottom of the sidebar
        def __init__(self, parent=None):
            QGroupBox.__init__(self, parent)
            self.setLayout(QHBoxLayout())

            self.Quit = utls.GenericLargePushButton(text='Quit')
            self.Quit.clicked.connect(QtCore.QCoreApplication.instance().quit)
            self.layout().addWidget(self.Quit)

            self.AuxButton = utls.GenericLargePushButton(text='About')
            self.setAuxButtonToAbout()
            self.layout().addWidget(self.AuxButton)
            

        def setAuxButtonToAbout(self):
            # switch the button to direct to about page
            self.AuxButton.setText('About')
            self.AuxButton.clicked.connect(lambda: self.parent().parent().parent().navToAbout(idx=1))


        def setAuxButtonToMain(self):
            # switch the button to direct to main page
            self.AuxButton.setText('Back')
            self.AuxButton.clicked.disconnect() # disconnect the link to other pages (this is CRITICAL!)
            self.AuxButton.clicked.connect(lambda: self.parent().parent().parent().navToMain())



class MainPageStackWidget(QStackedWidget):
    # the main stack that everything else sits on
    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent)
        
