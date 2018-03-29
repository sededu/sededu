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
        
        # etcBox = gui.EtcBox("about", self)
        # etcBox = QLabel("FILLER")
        
        readmeText = self.ReadmeFileData(self.parent().thisPath)
        bodyBox = QGroupBox()
        bodyLayout = QVBoxLayout()
        categoryLabelText = gui.InfoLabel("About the SedEdu project:", gui.titleFont())
        descLabel = gui.MultilineInfoLabel(readmeText.summary)

        bodyLayout.addWidget(categoryLabelText)
        bodyLayout.addWidget(descLabel)
        bodyLayout.addWidget(gui.InfoLabel(readmeText.license))
        bodyLayout.addStretch(1)
        bodyLayout.addWidget(gui.InfoLabel("Contributors:"))
        
        for c in readmeText.contributors:
            contrib = gui.InfoLabel(c)
            contrib.setContentsMargins(10, 0, 0, 0)
            bodyLayout.addWidget(contrib)

        bodyLayout.addStretch(2)
        bodyLayout.addWidget(gui.InfoLabel('For complete information visit \
            the [SedEdu project page](https://github.com/amoodie/sededu).', gui.titleFont()))
        bodyLayout.addStretch(10)
        bodyLayout.addWidget(gui.InfoLabel("SedEdu is supported by:"))
        bodyLayout.addWidget(gui.SupportedBox(self.parent().privatePath))
        
        bodyBox.setLayout(bodyLayout)
        
        layout = QHBoxLayout()
        # layout.addWidget(etcBox)
        # layout.addWidget(gui.VLine(self))
        layout.addWidget(bodyBox, 100)
        self.setLayout(layout)





    class ReadmeFileData():
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