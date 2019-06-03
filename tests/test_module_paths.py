import pytest

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

from sededu.root import RootWindow


def test_check_paths_of_all_found_modules(qtbot):
    root = RootWindow()
    
    