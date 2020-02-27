import os, subprocess, platform, re
import numpy as np
import json
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore



class ParagraphInfoLabel(QLabel):
    # the base class of the InfoLabel classes
    defaultFont = QtGui.QFont()
    def __init__(self, labelText='', theFont=defaultFont, parent=None):
        QLabel.__init__(self, parent)

        # check for links as markdown
        if isinstance(labelText, str):
            self._labelText, self.isurl = self.url_checker(labelText)
        
        # check if the string is a path to a file
        if os.path.isfile(labelText):
            self._labelText = self.file_checker(labelText)
            self.isfile = True
        else:
            self.isfile = False
        
        self.setText(self._labelText)

        # set to wrap, font, and open links
        self.setWordWrap(True)
        self.setFont(theFont)
        self.setOpenExternalLinks(True)

        self.setLineWidth(0)
        self.setFrameStyle(QFrame.Panel | QFrame.Plain)


    def url_checker(self, labelText):
        # check for markdown formatted urls
        name_regex = '[^]]+'
        url_regex = '[^)]+'
        join_url = '(\[{0}]\(\s*{1}\s*\))'.format(name_regex, url_regex)
        split_url = '\[({0})]\(\s*({1})\s*\)'.format(name_regex, url_regex)
        isurl = False # false by default
        for j, s in zip(re.findall(join_url, labelText), re.findall(split_url, labelText)):
            labelText = labelText.replace(j,
                ''.join(('<a href=\"', s[1], '\">', s[0], '</a>')))
            isurl = True # changed to true if into the loop
        return labelText, isurl


    def file_checker(self, labelText):
        # convert string to a link
        labelText = ''.join(('<a href=\"file:///', labelText, '\">open README</a>'))
        return labelText



class ShortInfoLabel(ParagraphInfoLabel):
    # a shortened version of the InfoLabel
    # made to work in the ModuleInfoPage listings
    defaultFont = QtGui.QFont()
    def __init__(self, labelText='', theFont=defaultFont, parent=None):
        ParagraphInfoLabel.__init__(self, labelText, theFont, parent)

        self.setSizePolicy(QSizePolicy(
                           QSizePolicy.MinimumExpanding,
                           QSizePolicy.Maximum))
        self.setAlignment(QtCore.Qt.AlignTop)



class OneLineInfoLabel(ShortInfoLabel):
    # shortest version of InfoLabel, no word wrapping
    defaultFont = QtGui.QFont()
    def __init__(self, labelText='', theFont=defaultFont, parent=None):
        ShortInfoLabel.__init__(self, labelText, theFont, parent)

        self.setWordWrap(False)



class GenericLargePushButton(QPushButton):
    # larger than normal push button for general use
    def __init__(self, text='', height=50, parent=None):
        QPushButton.__init__(self, parent)

        self.setText(text)
        self.setMinimumHeight(height)
        self.setFont(subtitleFont())



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
        self.setWindowTitle('Error')
        self.setStandardButtons(QMessageBox.Ok)



def open_file(filename):
    # utility for opening files
    platType = platform.system()
    if os.path.isfile(filename):
        if platType in {'Linux'}:
            try:
                sp = subprocess.Popen(['xdg-open', filename])
                # output, error = sp.communicate()
            except FileNotFoundError as e:
                platRelease = platform.release()
                pyType = platform.python_build()
                raise RuntimeError('Error raised when trying to open file: \n\t {filename} \n'
                                   'Identified on platform type: \n\t {platType} \n'
                                   'Platform release identfied as: \n\t {platRelease} \n'
                                   'Python type: \n\t {pyType} \n'
                                   '\n Full error msg was: \n\t {errmsg}'.format(filename=filename, platType=platType,
                                                                            platRelease=platRelease, pyType=pyType, errmsg=e))
        elif platType in {'Darwin', 'Windows'}:
            sp = subprocess.Popen(['open', filename])
        else:
            raise RuntimeError('unknown platform type: %s' % platType)   
    else:
        msg = NoFileMessageBox(filename)
        msg.exec_()



def HLine():
    # horizontal line
    toto = QFrame()
    toto.setFrameShape(QFrame.HLine)
    toto.setFrameShadow(QFrame.Sunken)
    return toto



def VLine():
    # vertical line
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
    return c.lower().replace(' ','').replace('\n','')



def filesList(d):
    # list files in directory
    return [f for f in os.listdir(d) if
            os.path.isfile(os.path.join(d, f))]



## font definitions / text modifiers
def versionFont():
    # a smaller, italics font for a version number
    font = QtGui.QFont()
    font.setBold(False)
    font.setItalic(True)
    font.setPointSize(9)
    return font



def titleFont():
    # a larger bold font for titles
    font = QtGui.QFont()
    font.setBold(True)
    font.setItalic(False)
    font.setPointSize(14)
    return font



def subtitleFont():
    # a medium sized font for a subtitle
    font = QtGui.QFont()
    font.setBold(False)
    font.setItalic(False)
    font.setPointSize(12)
    return font



def cutTitle(text0):
    # removes word module from end of string if two present
    splt_t0 = text0.split()
    spltend_t0 = splt_t0[-2:]
    nospec_t0 = [ [''.join(e for e in x if e.isalnum()).lower()]
                 for x in spltend_t0 ]
    if len(nospec_t0) > 1 and nospec_t0[0] == nospec_t0[1]: # if last two words are same (i.e., 'modules')
        text = ' '.join(splt_t0[:-1]) + ':'
    else:
        text = text0
    return text
