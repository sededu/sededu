import os
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

class NavButton(QPushButton):
	def __init__(self, iLabel, thisPath, parent=None):
		QPushButton.__init__(self, parent)
		# iButton = QPushButton(iLabel)
		# self.setText(iLabel)
		iPath = os.path.join(thisPath, "sededu", "private", \
			iLabel.lower().replace(" ","").replace("\n","") + ".png")
		# print(iLabel + "path:" + iPath)
		iIcon = QtGui.QIcon()
		iIcon.addPixmap(QtGui.QPixmap(iPath))
		self.setIcon(iIcon)
		self.setIconSize(QtCore.QSize(300,200))

def etcButton(btnStr):
	etcBtn = QPushButton(btnStr)
	etcBtn.resize(1,10)
	return etcBtn

def categoryListItem():
	a=1

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