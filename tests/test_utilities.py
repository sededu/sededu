import pytest

import sys, os, shutil
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

import sededu.utilities as utls


def test_cutTitle_without_module():
    initial_string = 'Rivers modules:'
    new_string = utls.cutTitle(initial_string)

    assert new_string == initial_string

def test_cutTitle_with_module():
    initial_string = 'Behind the Modules modules:'
    new_string = utls.cutTitle(initial_string)

    assert new_string == 'Behind the Modules:'
    
    
# make a subdirectory structure and then check that it is correctly found


def test_subDirPath_with_root_dir_struct():
    os.mkdir('root_dir')
    os.mkdir(os.path.join('root_dir', 'folder_1'))
    os.mkdir(os.path.join('root_dir', 'folder_2'))
    open(os.path.join('root_dir','folder_1', 'file_1.txt'), 'a').close()
    open(os.path.join('root_dir','folder_1', 'file_2.txt'), 'a').close()
    open(os.path.join('root_dir','folder_2', 'file_3.txt'), 'a').close()

    directory_list = list(utls.subDirPath('root_dir'))

    shutil.rmtree('root_dir')
    
    assert len(directory_list) == 2

    
