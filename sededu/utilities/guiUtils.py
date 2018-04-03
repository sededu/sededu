import os, subprocess, platform, re
import numpy as np
import json
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore



class NoFileMessageBox(QMessageBox):
    # warning nofile mesage box, path is a required arg.
    # custom text can be passed as string mainText
    default = 'There was no file found at the specified path.\n\n'

    def __init__(self, givenPath, mainText=default, 
                 informText=False, parent=None):
        QMessageBox.__init__(self, parent)
        self.setIcon(QMessageBox.Critical)
        self.setText(mainText)
        if informText:
            self.setInformativeText(informText)
        self.setDetailedText(' '.join(['Path given:\n\n', givenPath]))
        self.setWindowTitle("Error")
        self.setStandardButtons(QMessageBox.Ok)



class NoImageFiller(QGroupBox):
    # filler image, takes text for label
    def __init__(self, labelText, previewHeight, parent=None):
        QGroupBox.__init__(self, parent)
        label = QLabel(labelText)
        label.setAlignment(QtCore.Qt.AlignCenter)
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        self.setMinimumHeight(previewHeight)
        self.setSizePolicy(QSizePolicy(
                           QSizePolicy.Preferred,
                           QSizePolicy.Fixed))



class MultilineInfoLabel(QLabel):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        
        self.setWordWrap(True)


    def url_checker(self, labelText):
        name_regex = "[^]]+"
        url_regex = "[^)]+"
        join_url = '(\[{0}]\(\s*{1}\s*\))'.format(name_regex, url_regex)
        split_url = '\[({0})]\(\s*({1})\s*\)'.format(name_regex, url_regex)
        for j, s in zip(re.findall(join_url, labelText), re.findall(split_url, labelText)):
            labelText = labelText.replace(j, 
                ''.join(('<a href=\"', s[1], '\">', s[0], '</a>')))
        return labelText



class InfoLabel(MultilineInfoLabel):
    defaultFont = QtGui.QFont()
    def __init__(self, labelText='', theFont=defaultFont, parent=None):
        MultilineInfoLabel.__init__(self, parent)
        
        labelText = self.url_checker(labelText)
        self.setText(labelText)
        self.setWordWrap(True)
        self.setFont(theFont)
        self.setSizePolicy(QSizePolicy(
                           QSizePolicy.MinimumExpanding,
                           QSizePolicy.Maximum))
        self.setAlignment(QtCore.Qt.AlignTop)
        self.setOpenExternalLinks(True)


class GenericLargePushButton(QPushButton):
    def __init__(self, buttonText='', parent=None):
        QPushButton.__init__(self, parent)
        backBtn = QPushButton("Back to Main Menu")
        backBtn.clicked.connect(self.parent().drawMain)
        backBtn.setFixedSize(QtCore.QSize(200,40))
        backBtn.setFont(gui.subtitleFont())



def open_file(filename):
    platType = platform.system()
    if os.path.isfile(filename):
        if platType in {"Darwin", "Linux"}:
            subprocess.Popen(["xdg-open", filename])
        elif platType in {"Windows"}:
            subprocess.Popen(["open", filename])
        else:
            print("unknown platform type")
    else:
        msg = NoFileMessageBox(filename)
        msg.exec_()



def HLine(self):
    toto = QFrame()
    toto.setFrameShape(QFrame.HLine)
    toto.setFrameShadow(QFrame.Sunken)
    return toto



def VLine(self):
    toto = QFrame()
    toto.setFrameShape(QFrame.VLine)
    toto.setFrameShadow(QFrame.Sunken)
    return toto



## path definitions / file finders
def subDirPath(d):
    # list of direct subdirectories
    return filter(os.path.isdir, [os.path.join(d,f) for f in os.listdir(d)])



def category2path(c):
    # convert category name to folder name
    # this is very specific now -- any way to generalize the folders to
    # case insensitive?
    return c.lower().replace(" ","").replace("\n","")



def filesList(d):
    # list files in directory
    return [f for f in os.listdir(d) if os.path.isfile(os.path.join(d, f))]



## font definitions / text modifiers
def versionFont():
    font = QtGui.QFont()
    font.setBold(False)
    font.setItalic(True)
    font.setPointSize(9)
    return font



def titleFont():
    font = QtGui.QFont()
    font.setBold(True)
    font.setItalic(False)
    font.setPointSize(14)
    return font



def subtitleFont():
    font = QtGui.QFont()
    font.setBold(False)
    font.setItalic(False)
    font.setPointSize(12)
    return font



def cutTitle(text0):
    # Use QFontMetrics to get measurements, 
    # e.g. the pixel length of a string using QFontMetrics.width().
    # cut the titles down to textextext... for the list widgets

    # also removes word module from end of string if two present
    splt_t0 = text0.split()
    spltend_t0 = splt_t0[-2:]
    nospec_t0 = [ [''.join(e for e in x if e.isalnum()).lower()] 
                 for x in spltend_t0 ]
    if nospec_t0[0] == nospec_t0[1]: # if last two words are same (i.e., 'modules')
        text = ' '.join(splt_t0[:-1]) + ":"
    else:
        text = text0
    return text
