import sys, os
import numpy as np
import json
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from sededu.utilities import guiUtils as gui



class AboutPageWidget(QWidget):
    # class for about page
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QVBoxLayout())
        
        # construct readme data to parse out into fields
        readmeText = self._ReadmeFileData(self.parent().thisPath)
        
        # construct the header
        categoryLabelText = gui.InfoLabel("About the SedEdu project:", gui.titleFont())
        
        # construct the summary multiline text
        descLabel = gui.MultilineInfoLabel(readmeText.summary)

        # construct the contributors box
        contribBox = self._ContributorWidget(readmeText)

        # construct the more information text
        completeInfoLabel = gui.InfoLabel('For complete information visit \
            the [SedEdu project page](https://github.com/amoodie/sededu).', gui.titleFont())

        # construct the supported by box
        SupportedBy = self._SupportedByWidget(self.parent().privatePath)

        # add widgets in specific vertical order
        self.layout().addWidget(categoryLabelText)
        self.layout().addWidget(descLabel)
        self.layout().addWidget(gui.InfoLabel(readmeText.license))
        
        self.layout().addStretch(1)
        self.layout().addWidget(contribBox)

        self.layout().addStretch(2)
        self.layout().addWidget(completeInfoLabel)

        self.layout().addStretch(10)
        self.layout().addWidget(SupportedBy)
        

    class _ContributorWidget(QGroupBox):
        def __init__(self, readmeText, parent=None):
            QGroupBox.__init__(self, parent)
            self.setLayout(QVBoxLayout())
            self.setContentsMargins(0, 0, 0, 0)

            self.layout().addWidget(gui.InfoLabel("Contributors:"))

            for c in readmeText.contributors:
                contrib = gui.InfoLabel(c)
                contrib.setContentsMargins(10, 0, 0, 0)
                self.layout().addWidget(contrib)


    class _SupportedByWidget(QWidget):
        def __init__(self, privatePath, parent=None):
            QWidget.__init__(self, parent)
            self.setLayout(QVBoxLayout())

            LogoBox = self.LogoBoxWidget()

            supportedText = gui.InfoLabel("SedEdu is supported by:")
            nsfLogo = self.logoPixmap(os.path.join(privatePath, "nsf.gif"))
            riceLogo = self.logoPixmap(os.path.join(privatePath, "rice.png"))
            
            self.layout().addWidget(supportedText)
            self.layout().addWidget(nsfLogo)
            self.layout().addWidget(riceLogo)
            self.layout().addStretch(100)


        class LogoBoxWidget(QGroupBox):
            def __init__(self, parent=None):
                QGroupBox.__init__(self, parent)
                self.setLayout(QHBoxLayout())
                self.layout().setContentsMargins(0, 0, 0, 0)


        def logoPixmap(self, path):
            logo = QLabel()
            logo.setPixmap(QtGui.QPixmap(path).scaledToHeight(100))
            return logo


    class _ReadmeFileData(object):
        def __init__(self, path):
            raw, lines = self.make_info(path)
            self.summary = self.make_summary(lines)
            self.license = self.make_license(lines)
            self.contributors = self.make_contributors(lines)
            

        def make_info(self, path):
            readmePath = os.path.join(path, "README.md")
            raw = open(readmePath, 'rt')
            lines = [l.replace("\n","").replace("*","") for l in raw]
            return raw, lines


        def make_summary(self, lines):
            summaryIdx = lines.index("# SedEdu") + 2
            summary = lines[summaryIdx]
            return summary


        def make_license(self, lines):
            licenseIdx = lines.index("## License") + 2
            license = lines[licenseIdx]
            return license


        def make_contributors(self, lines):
            licenseIdx = lines.index("## License") + 2
            contributorsIdx = lines.index("## Authors") + 2
            contributorsRaw = lines[contributorsIdx:licenseIdx-4]
            contributors = contributorsRaw
            return contributors