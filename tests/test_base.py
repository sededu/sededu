import pytest

import sys, os, shutil
import numpy as np
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

import sededu.base as base


def test_MainBackgroundWidget_instantiate(qtbot):
    mbw = base.MainBackgroundWidget()
    qtbot.addWidget(mbw)

    mbw.setVisible(True)
    
    assert mbw.width() >= 0
    assert mbw.isVisible() == True


def test_MainSideBarWidget_instantiate(qtbot):
    msbw = base.MainSideBarWidget()
    qtbot.addWidget(msbw)

    msbw.setVisible(True)
    
    assert msbw.width() >= 0
    assert msbw.isVisible() == True


def test_MainSideBarWidget__SideBarHeaderWidget_instantiate(qtbot):
    msbw_sbhw = base.MainSideBarWidget._SideBarHeaderWidget()
    qtbot.addWidget(msbw_sbhw)

    msbw_sbhw.Logo.text() == '**logo not found**'
    msbw_sbhw.Desc.text() != ''
    msbw_sbhw.Vers.text() != ''


def test_MainSideBarWidget__SideBarButtonsWidget_instantiate(qtbot):
    msbw_sbbw = base.MainSideBarWidget._SideBarButtonsWidget()
    qtbot.addWidget(msbw_sbbw)

    msbw_sbbw.Quit.text() == 'Quit'
    msbw_sbbw.AuxButton.text() == 'About'


def test_MainPageStackWidget_instantiate(qtbot):
    mpsw = base.MainPageStackWidget()
    qtbot.addWidget(mpsw)

    mpsw.setVisible(True)
    
    assert mpsw.currentIndex() == -1
    assert mpsw.isVisible() == True
