import pytest

import sys, os, shutil
import numpy as np
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

import sededu.utilities as utls


def test_ParagraphInfoLabel_defaults():
    info = utls.ParagraphInfoLabel()

    assert info.text() == ''
    assert info.wordWrap() == True


def test_ParagraphInfoLabel_labelText_strings():
    info1 = utls.ParagraphInfoLabel(labelText='SomeOneWordString')
    info2 = utls.ParagraphInfoLabel(labelText='SomeTwo WordString')
    info3 = utls.ParagraphInfoLabel(labelText='10!is a We?rd #')

    assert info1.text() == 'SomeOneWordString'
    assert info1.isurl == False
    assert info1.isfile == False
    assert info2.text() == 'SomeTwo WordString'
    assert info3.text() == '10!is a We?rd #'


def test_ParagraphInfoLabel_labelText_urls():
    url1 = 'https://github.com/sededu/sededu/blob/release/CONTRIBUTING.md'
    info1 = utls.ParagraphInfoLabel(labelText=url1)
    url2 = '[Contributing.md](https://github.com/sededu/sededu/blob/release/CONTRIBUTING.md)'
    info2 = utls.ParagraphInfoLabel(labelText=url2)

    assert info1.text() == url1
    assert info2.text() != url2
    assert info1.isurl == False
    assert info2.isurl == True


def test_ParagraphInfoLabel_labelText_files():
    fileDir = os.path.dirname(__file__)
    thisPath = os.path.join(fileDir,'')

    file1 = os.path.join(thisPath)
    info1 = utls.ParagraphInfoLabel(labelText=file1)
    file2 = os.path.join(thisPath, 'test_utilities.py')
    info2 = utls.ParagraphInfoLabel(labelText=file2)
    file3 = os.path.join(thisPath, 'not_a_real_file.py')
    info3 = utls.ParagraphInfoLabel(labelText=file3)
    
    assert info1.text() == file1
    assert info1.isfile == False
    assert info1.isurl == False
    assert info2.text() != file2
    assert info2.isfile == True
    assert info2.isurl == False
    assert info3.text() == file3
    assert info3.isfile == False
    assert info3.isurl == False


def test_VLine():
    vline = utls.VLine()

    assert vline.frameShape() == 5


def test_HLine():
    hline = utls.HLine()

    assert hline.frameShape() == 4


def test_cutTitle_without_module():
    initial_string = 'Rivers modules:'
    new_string = utls.cutTitle(initial_string)

    assert new_string == initial_string


def test_cutTitle_with_module():
    initial_string = 'Behind the Modules modules:'
    new_string = utls.cutTitle(initial_string)

    assert new_string == 'Behind the Modules:'


def test_subDirPath():
    docs_directory_list = list(utls.subDirPath('docs'))
    ci_directory_list = list(utls.subDirPath('.ci'))
    docs_file_list = list(utls.filesList('docs'))
    
    assert len(docs_directory_list) == 2
    assert len(ci_directory_list) == 3
    assert len(docs_file_list) == 8


def test_filesList():
    docs_file_list = list(utls.filesList('docs'))
    
    assert len(docs_file_list) == 8


def test_category2path_with_real_names():
    categoryList = ['Rivers', 'Deltas', 'Deserts', 'Coasts', 
                    'Stratigraphy', 'Behind the \nModules']

    assert utls.category2path('Rivers') == 'rivers'
    assert utls.category2path('Deltas') == 'deltas'
    assert utls.category2path('Behind the \nModules') == 'behindthemodules'


def test_category2path_with_fake_names():
    assert utls.category2path('Andrew Moodie') == 'andrewmoodie'
    assert utls.category2path('SedEdu!IsFun!') == 'sededu!isfun!'
    # note that this is expected behavior, but 'sededu!isfun!'
    #    is not a valid file name. It would be best to replace 
    #    all special characters, or better validate the names?


