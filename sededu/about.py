import sys, os
import numpy as np
import json
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

import sededu.utilities as utls



class AboutPageWidget(QWidget):
    # class for about page
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QVBoxLayout())
        
        # construct readme data to parse out into fields
        readmeText = self._ReadmeFileData(self.parent().thisPath)
        
        # construct the header
        categoryLabelText = utls.OneLineInfoLabel("About the SedEdu project:", utls.titleFont())
        
        # construct the summary multiline text
        descLabel = utls.ParagraphInfoLabel(readmeText.summary)

        # construct the contributors box
        contribBox = self._ContributorWidget(readmeText)

        # construct the more information text
        completeInfoLabel = utls.ShortInfoLabel('For complete information visit \
            the [SedEdu project page](https://github.com/amoodie/sededu).', utls.titleFont())

        # construct the supported by box
        SupportedBy = self._SupportedByWidget(self.parent().privatePath)

        # add widgets in specific vertical order
        self.layout().addWidget(categoryLabelText)
        self.layout().addWidget(descLabel)
        self.layout().addWidget(utls.ShortInfoLabel(readmeText.license))
        
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

            self.layout().addWidget(utls.OneLineInfoLabel("Contributors:"))

            for c in readmeText.contributors:
                contrib = utls.ShortInfoLabel(c)
                contrib.setContentsMargins(10, 0, 0, 0)
                self.layout().addWidget(contrib)


    class _SupportedByWidget(QWidget):
        def __init__(self, privatePath, parent=None):
            QWidget.__init__(self, parent)
            self.setLayout(QVBoxLayout())

            LogoBox = self.LogoBoxWidget()

            supportedText = utls.OneLineInfoLabel("SedEdu is supported by:")
            nsfLogo = self.LogoPixmapWidget(os.path.join(privatePath, "nsf.gif"))
            riceLogo = self.LogoPixmapWidget(os.path.join(privatePath, "rice.png"))
            
            self.layout().addWidget(supportedText)
            self.layout().addWidget(LogoBox)
            LogoBox.layout().addWidget(nsfLogo)
            LogoBox.layout().addWidget(riceLogo)
            LogoBox.layout().addStretch(1)


        class LogoBoxWidget(QGroupBox):
            def __init__(self, parent=None):
                QGroupBox.__init__(self, parent)
                self.setLayout(QHBoxLayout())
                self.layout().setContentsMargins(0, 0, 0, 0)
                self.setAlignment(QtCore.Qt.AlignLeft)


        def LogoPixmapWidget(self, path):
            logo = QLabel()
            logo.setPixmap(QtGui.QPixmap(path).scaledToHeight(100))
            return logo


    class _ReadmeFileData(object):
        def __init__(self, path):
            raw, lines = self.extract_from_file(path)
            self.summary = self.make_summary(lines)
            self.license = self.make_license(lines)
            self.contributors = self.make_contributors(lines)
            

        def extract_from_file(self, path):
            readmePath = os.path.join(path, 'README.md')
            raw = open(readmePath, 'rt')
            lines = [l.replace('\n','').replace('*','') for l in raw]
            return raw, lines


        def strip_and_join(self, lines_raw):
            lines_rstripped = [l.rstrip() for l in lines_raw]
            lines = ' '.join(lines_rstripped)
            return lines


        def make_summary(self, lines):
            summaryIdx = lines.index('# SedEdu') + 2
            imageIdx = [i for i, s in enumerate(lines) 
                        if '![image of SedEdu main menu]' in s]
            imageIdx = imageIdx[0]
            summary_raw = lines[summaryIdx:imageIdx]
            summary = self.strip_and_join(summary_raw)
            return summary


        def make_license(self, lines):
            licenseIdx = lines.index('## License') + 2
            acknowledgeIdx = lines.index('## Acknowledgments')
            license_raw = lines[licenseIdx:acknowledgeIdx]
            license = self.strip_and_join(license_raw)
            return license


        def make_contributors(self, lines):
            contributorsIdx = lines.index('## Authors') + 2
            licenseIdx = lines.index('## License')
            contributors_raw = lines[contributorsIdx:licenseIdx]
            contributors = contributors_raw
            return contributors