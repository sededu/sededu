import pytest

import sys, os, shutil
import numpy as np
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

import sededu.about as about


class RootWindowPlaceholder(QMainWindow):
    """
    This class just serves to fill the role of the parent RootWindow. We don't
    want to instantiate a real RootWindow because then coverage is raised
    artificially, due to all the code base being visited.
    """
    def __init__(self):
        QMainWindow.__init__(self)

        fileDir = os.path.dirname(__file__)
        self.thisPath = os.path.join(fileDir, os.pardir, 'sededu', '')
        self.rootPath = os.path.join(fileDir, os.pardir, os.pardir, 'sededu', '')
        self.privatePath = os.path.join(self.thisPath, os.pardir, 'sededu', 'private')
        self.categoryList = ['Rivers', 'Deltas', 'Deserts', 'Coasts', 
                             'Stratigraphy', 'Behind the \nModules']


def test_AboutPageWidget_instantiate(qtbot):
    p = RootWindowPlaceholder()
    apw = about.AboutPageWidget(parent=p)
    qtbot.addWidget(p)
    qtbot.addWidget(apw)

    p.setVisible(True)
    
    assert apw.width() >= 0
    assert apw.isVisible() == True


def test_AboutPageWidget__readmeJSON(qtbot):
    p = RootWindowPlaceholder()
    apwrj = about.AboutPageWidget(parent=p)
    data = apwrj._readmeJSON(readmeJSONPath=apwrj.readmeJSONPath)
    qtbot.addWidget(p)
    qtbot.addWidget(apwrj)

    # we just check that these fields are filled
    assert apwrj.categoryLabelText
    assert apwrj.descLabel
    assert apwrj.licenseLabel
    assert apwrj.contribBox
    assert apwrj.completeInfoLabel
    assert apwrj.SupportedBy


def test_AboutPageWidget__ContributorWidget(qtbot):
    p = RootWindowPlaceholder()
    apw = about.AboutPageWidget(parent=p)
    apwcw = about.AboutPageWidget._ContributorWidget(readmeText=apw.readmeText, parent=p)
    qtbot.addWidget(p)
    qtbot.addWidget(apw)
    qtbot.addWidget(apwcw)

    assert apwcw.width() > 0
    # need better tests here...


def test_AboutPageWidget__SupportedByWidget(qtbot):
    p = RootWindowPlaceholder()
    apw = about.AboutPageWidget(parent=p)
    apwsw = about.AboutPageWidget._SupportedByWidget(privatePath=apw.parent().privatePath, parent=p)
    qtbot.addWidget(p)
    qtbot.addWidget(apw)
    qtbot.addWidget(apwsw)

    assert apwsw.width() > 0
    # need better tests here...
