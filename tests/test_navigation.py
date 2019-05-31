import pytest

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

from sededu.root import RootWindow


def test_navigation_to_about_page_by_function(qtbot):
    root = RootWindow()
    root.navToAbout()
    assert root.MainPageStack.currentIndex() == 1

def test_navigation_to_about_page_by_button(qtbot):
    root = RootWindow()
    qtbot.addWidget(root)

    # click on the AuxButton and make sure it updates the appropriate label and page on stack
    qtbot.mouseClick(root.MainSideBar.SideBarButtons.AuxButton, QtCore.Qt.LeftButton)

    assert root.MainSideBar.SideBarButtons.AuxButton.text() == 'Back'

