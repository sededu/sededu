import pytest

import sys, os, shutil
import numpy as np
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

import sededu.navigation as navigation

class placeholder_root(QMainWindow):
    """
    This class just serves to fill the role of the parent RootWindow. We don't
    want to instantiate a real RootWindow because then coverage is raised
    artificially, due to all the code base being visited.
    """
    def __init__(self):
        QMainWindow.__init__(self)

        fileDir = os.path.dirname(__file__)
        self.thisPath = os.path.join(fileDir,'')
        self.rootPath = os.path.join(fileDir, os.pardir,'')
        self.privatePath = os.path.join(self.thisPath, os.pardir, 'sededu', 'private')
        self.categoryList = ['Rivers', 'Deltas', 'Deserts', 'Coasts', 
                             'Stratigraphy', 'Behind the \nModules']


def test_NavigationPageWidget_instantiate(qtbot):
    p = placeholder_root()
    npw = navigation.NavigationPageWidget(p)
    qtbot.addWidget(p)
    qtbot.addWidget(npw)

    p.setVisible(True)
    
    assert npw.width() >= 0
    assert npw.isVisible() == True
    assert len(npw.buttonList) > 0


def test_NavigationPageWidget__NavigationCategoryButtonWidget_instantiate(qtbot):
    categoryName = 'Fake Category'
    npw_ncbw = navigation.NavigationPageWidget._NavigationCategoryButtonWidget(\
                    category=categoryName, privatePath='path')
    qtbot.addWidget(npw_ncbw)
    
    assert npw_ncbw.width() >= 0
    assert npw_ncbw.text() == '**icon not found**'
    assert npw_ncbw.categoryName == categoryName


def test_NavigationPageWidget__NavigationCategoryButtonWidget_withIcon(qtbot):
    p = placeholder_root()
    categoryName = 'Rivers'
    npw_ncbw = navigation.NavigationPageWidget._NavigationCategoryButtonWidget(\
                    category=categoryName, privatePath=p.privatePath, parent=p)
    qtbot.addWidget(p)
    qtbot.addWidget(npw_ncbw)
    
    assert npw_ncbw.width() >= 0
    assert npw_ncbw.text() == ''
    assert npw_ncbw.categoryName == categoryName
