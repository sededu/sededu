import pytest

import sys, os, shutil
import numpy as np
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

import sededu.utilities as navigation

# NavigationPageWidget

def test_MainBackgroundWidget_instantiate(qtbot):
    pass