import pytest

import sys, os, shutil
import numpy as np
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

import sededu.utilities as utls


def test_ParagraphInfoLabel_defaults(qtbot):
    info1 = utls.ParagraphInfoLabel()
    qtbot.addWidget(info1)

    assert info1.text() == ''
    assert info1.wordWrap() == True


def test_ParagraphInfoLabel_labelText_strings(qtbot):
    info1 = utls.ParagraphInfoLabel(labelText='SomeOneWordString')
    info2 = utls.ParagraphInfoLabel(labelText='SomeTwo WordString')
    info3 = utls.ParagraphInfoLabel(labelText='10!is a We?rd #')
    qtbot.addWidget(info1)
    qtbot.addWidget(info2)
    qtbot.addWidget(info3)

    assert info1.text() == 'SomeOneWordString'
    assert info1.isurl == False
    assert info1.isfile == False
    assert info2.text() == 'SomeTwo WordString'
    assert info3.text() == '10!is a We?rd #'


def test_ParagraphInfoLabel_labelText_urls(qtbot):
    url1 = 'https://github.com/sededu/sededu/blob/release/CONTRIBUTING.md'
    info1 = utls.ParagraphInfoLabel(labelText=url1)
    url2 = '[Contributing.md](https://github.com/sededu/sededu/blob/release/CONTRIBUTING.md)'
    info2 = utls.ParagraphInfoLabel(labelText=url2)
    qtbot.addWidget(info1)
    qtbot.addWidget(info2)

    assert info1.text() == url1
    assert info2.text() != url2
    assert info1.isurl == False
    assert info2.isurl == True


def test_ParagraphInfoLabel_labelText_files(qtbot):
    fileDir = os.path.dirname(__file__)
    thisPath = os.path.join(fileDir,'')

    file1 = os.path.join(thisPath)
    info1 = utls.ParagraphInfoLabel(labelText=file1)
    file2 = os.path.join(thisPath, 'test_utilities.py')
    info2 = utls.ParagraphInfoLabel(labelText=file2)
    file3 = os.path.join(thisPath, 'not_a_real_file.py')
    info3 = utls.ParagraphInfoLabel(labelText=file3)
    qtbot.addWidget(info1)
    qtbot.addWidget(info2)
    qtbot.addWidget(info3)
    
    assert info1.text() == file1
    assert info1.isfile == False
    assert info1.isurl == False
    assert info2.text() != file2
    assert info2.isfile == True
    assert info2.isurl == False
    assert info3.text() == file3
    assert info3.isfile == False
    assert info3.isurl == False


def test_ShortInfoLabel(qtbot):
    labelText = 'Title of my mixtape'
    info1 = utls.ShortInfoLabel(labelText)
    qtbot.addWidget(info1)

    assert info1.text() == labelText
    assert info1.wordWrap() == True
    assert info1.font().bold() == False


def test_OneLineInfoLabel(qtbot):
    labelText = 'Subtitle of my mixtape'
    info1 = utls.OneLineInfoLabel(labelText)
    qtbot.addWidget(info1)

    assert info1.text() == labelText
    assert info1.wordWrap() == False


def test_OneLineInfoLabel_versionFont(qtbot):
    labelText = '1.0.0'
    versionFont = utls.versionFont()
    info1 = utls.OneLineInfoLabel(labelText, theFont=versionFont)
    qtbot.addWidget(info1)

    assert info1.text() == labelText
    assert info1.wordWrap() == False
    assert info1.font().bold() == False
    assert info1.font().italic() == True
    assert info1.font().pointSize() == 9


def test_OneLineInfoLabel_titleFont(qtbot):
    labelText = 'A big important title'
    titleFont = utls.titleFont()
    info1 = utls.OneLineInfoLabel(labelText, theFont=titleFont)
    qtbot.addWidget(info1)

    assert info1.text() == labelText
    assert info1.wordWrap() == False
    assert info1.font().bold() == True
    assert info1.font().italic() == False
    assert info1.font().pointSize() == 14


def test_OneLineInfoLabel_subtitleFont(qtbot):
    labelText = 'A less important subtitle'
    subtitleFont = utls.subtitleFont()
    info1 = utls.OneLineInfoLabel(labelText, theFont=subtitleFont)
    qtbot.addWidget(info1)

    assert info1.text() == labelText
    assert info1.wordWrap() == False
    assert info1.font().bold() == False
    assert info1.font().italic() == False
    assert info1.font().pointSize() == 12


def test_GenericLargePushButton_defaults(qtbot):
    butt1 = utls.GenericLargePushButton()
    qtbot.addWidget(butt1)

    assert butt1.text() == ''
    assert butt1.minimumHeight() == 50


def test_GenericLargePushButton_labelText(qtbot):
    text = 'some text for a big button'
    butt1 = utls.GenericLargePushButton(text)
    qtbot.addWidget(butt1)

    assert butt1.text() == text
    assert butt1.minimumHeight() == 50


def test_GenericLargePushButton_height(qtbot):
    height = 30
    butt1 = utls.GenericLargePushButton(height=height)
    qtbot.addWidget(butt1)

    assert butt1.text() == ''
    assert butt1.minimumHeight() == height


def test_NoFileMessageBox_defaults(qtbot):
    box = utls.NoFileMessageBox(givenPath='some/file/path')
    qtbot.addWidget(box)

    # assert box.windowTitle() == 'Error' # fails on osx
    assert box.informativeText() == ''
    assert box.icon() == QMessageBox.Critical


def test_NoFileMessageBox_informativeText(qtbot):
    informativeText = 'This is some informative text that will help!'
    box = utls.NoFileMessageBox(givenPath='some/file/path', 
                                informText=informativeText)
    qtbot.addWidget(box)

    # assert box.windowTitle() == 'Error' # fails on osx
    assert box.informativeText() == informativeText
    assert box.icon() == QMessageBox.Critical


def test_VLine(qtbot):
    vline = utls.VLine()
    qtbot.addWidget(vline)

    assert vline.frameShape() == 5


def test_HLine(qtbot):
    hline = utls.HLine()
    qtbot.addWidget(hline)

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


