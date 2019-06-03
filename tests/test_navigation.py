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
    assert root.MainPageStack.currentIndex() == 1

def test_navigation_to_about_and_back_to_nav_page_by_button(qtbot):
    root = RootWindow()
    qtbot.addWidget(root)

    # click on the AuxButton and make sure it updates the appropriate label and page on stack
    qtbot.mouseClick(root.MainSideBar.SideBarButtons.AuxButton, QtCore.Qt.LeftButton)
    qtbot.mouseClick(root.MainSideBar.SideBarButtons.AuxButton, QtCore.Qt.LeftButton)

    assert root.MainSideBar.SideBarButtons.AuxButton.text() == 'About'
    assert root.MainPageStack.currentIndex() == 0

def test_navigation_to_rivers_page_by_button(qtbot):
    root = RootWindow()
    qtbot.addWidget(root)

    # click on the rivers nav button and make sure it updates the appropriate label and page on stack
    # manually emit the clicked signal
    root.MainPageStack.NavigationPage.buttonList[0].clicked.emit()
    # click the button using qtbot (doesn't work for some reason...)
    # qtbot.mouseClick(root.MainPageStack.NavigationPage.buttonList[0], QtCore.Qt.LeftButton)

    assert root.MainPageStack.children()[-1].children()[-2].text() == 'Rivers modules:'
    assert root.MainSideBar.SideBarButtons.AuxButton.text() == 'Back'
    assert root.MainPageStack.currentIndex() == 2

def test_navigation_to_stratigraphy_page_and_back_to_nav_page_by_button(qtbot):
    root = RootWindow()
    qtbot.addWidget(root)

    # click on the stratigraphy nav button and make sure it updates the appropriate label and page on stack
    # manually emit the clicked signal
    root.MainPageStack.NavigationPage.buttonList[4].clicked.emit()

    # click on the back button
    qtbot.mouseClick(root.MainSideBar.SideBarButtons.AuxButton, QtCore.Qt.LeftButton)

    assert root.MainSideBar.SideBarButtons.AuxButton.text() == 'About'
    assert root.MainPageStack.currentIndex() == 0
