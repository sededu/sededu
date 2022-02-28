import pytest

import sys, os, shutil
import numpy as np
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

import sededu.category as category

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
        self.categoryList = ['Rivers and deltas', 'Landscapes', 'Deserts', 'Coasts', 
                             'Stratigraphy']


class ItemPlaceholder(object):
    """
    This class fills the place of an item clicked in the module or doc list
    """
    def __init__(self, idx):
        self.idx = idx


def test_CategoryPageWidget_instantiate(qtbot):
    p = RootWindowPlaceholder()
    cpw = category.CategoryPageWidget(category='Rivers and deltas', parent=p)
    qtbot.addWidget(p)
    qtbot.addWidget(cpw)

    p.setVisible(True)
    
    assert cpw.width() >= 0
    assert cpw.isVisible() is True
    assert len(cpw.ModuleList) == 0  # zero because no submodules cloned


@pytest.mark.xfail()
def test_CategoryPageWidget_setModulePage(qtbot):
    p = RootWindowPlaceholder()
    cpw = category.CategoryPageWidget(category='Rivers and deltas', parent=p)
    qtbot.addWidget(p)
    qtbot.addWidget(cpw)

    p.setVisible(True)
    item0 = ItemPlaceholder(idx=0)
    item1 = ItemPlaceholder(idx=1)

    cpw.setModulePage(item1)
    
    assert cpw.ModuleInformationPageStack.currentIndex() == 1
