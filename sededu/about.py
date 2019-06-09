import sys, os
import numpy as np
import json
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

from . import utilities as utls



class AboutPageWidget(QWidget):
    # class for about page
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QVBoxLayout())
        
        # construct readme data to parse out into fields
        self.readmeJSONPath = os.path.join(self.parent().thisPath, '_readme.json')
        self.readmeText = self._readmeJSON(self.readmeJSONPath)

        # construct the header
        self.categoryLabelText = utls.OneLineInfoLabel('About the SedEdu project:', utls.titleFont())
        
        # construct the summary multiline text
        self.descLabel = utls.ParagraphInfoLabel(self.readmeText['summary'])

        # construct the license label text
        self.licenseLabel = utls.ShortInfoLabel(self.readmeText['license'])

        # construct the contributors box
        self.contribBox = self._ContributorWidget(self.readmeText)

        # construct the more information text
        self.completeInfoLabel = utls.ShortInfoLabel('For complete information visit \
            the [SedEdu project page](https://github.com/amoodie/sededu).', utls.titleFont())

        # construct the supported by box
        self.SupportedBy = self._SupportedByWidget(self.parent().privatePath)

        # add widgets in specific vertical order
        self.layout().addWidget(self.categoryLabelText)
        self.layout().addWidget(self.descLabel)
        self.layout().addWidget(self.licenseLabel)
        
        self.layout().addStretch(1)
        self.layout().addWidget(self.contribBox)

        self.layout().addStretch(2)
        self.layout().addWidget(self.completeInfoLabel)

        self.layout().addStretch(10)
        self.layout().addWidget(self.SupportedBy)

    def _readmeJSON(self, readmeJSONPath):
        # read json to dictionary
        with open(readmeJSONPath) as f:
            data = json.load(f)

            return data
        

    class _ContributorWidget(QGroupBox):
        # grouping box for the contributors list
        def __init__(self, readmeText, parent=None):
            QGroupBox.__init__(self, parent)
            self.setLayout(QVBoxLayout())
            self.setContentsMargins(0, 0, 0, 0)

            self.layout().addWidget(utls.OneLineInfoLabel('Contributors:'))

            for c in readmeText['contributors']:
                contrib = utls.ShortInfoLabel(c)
                contrib.setContentsMargins(10, 0, 0, 0)
                self.layout().addWidget(contrib)


    class _SupportedByWidget(QWidget):
        # grouping for supported by logo list
        def __init__(self, privatePath, parent=None):
            QWidget.__init__(self, parent)
            self.setLayout(QVBoxLayout())

            LogoBox = self.LogoBoxWidget()

            supportedText = utls.OneLineInfoLabel('SedEdu is supported by:')
            nsfLogo = self.LogoPixmapWidget(os.path.join(privatePath, 'nsf.gif'))
            riceLogo = self.LogoPixmapWidget(os.path.join(privatePath, 'rice.png'))
            
            self.layout().addWidget(supportedText)
            self.layout().addWidget(LogoBox)
            LogoBox.layout().addWidget(nsfLogo)
            LogoBox.layout().addWidget(riceLogo)
            LogoBox.layout().addStretch(1)


        class LogoBoxWidget(QGroupBox):
            # grouping box for the logos
            def __init__(self, parent=None):
                QGroupBox.__init__(self, parent)
                self.setLayout(QHBoxLayout())
                self.layout().setContentsMargins(0, 0, 0, 0)
                self.setAlignment(QtCore.Qt.AlignLeft)


        def LogoPixmapWidget(self, path):
            # logo objects
            logo = QLabel()
            logo.setPixmap(QtGui.QPixmap(path).scaledToHeight(100))
            return logo
