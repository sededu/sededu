import os
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

def mainLayout(inList, thisPath):
	buttonLayout = QGridLayout()
	nList = len(inList)
	# xPos = np.tile([0, 1], int(np.ceil(nList/2)))
	# yPos = np.tile(range(int(np.ceil(nList/2))), 2)
	gridSize = [3, 2]
	# xPos = np.tile( range(gridSize[1]), (1, int(np.ceil(nList/gridSize[1]))) )
	cPos = [0, 1, 0, 1, 0, 1]
	rPos = [0, 0, 1, 1, 2, 2] # this needs to be figured out how to make in numpy...
	for i in range(nList):
		iLabel = inList[i]
		iButton = QPushButton(iLabel)
		iPath = os.path.join(thisPath, "sededu", "private", \
			iLabel.lower().replace(" ","").replace("\n","") + ".jpg")
		# print(iPath)
		iIcon = QtGui.QIcon()
		iIcon.addPixmap(QtGui.QPixmap(iPath))
		iButton.setIcon(iIcon)
		iButton.setIconSize(QtCore.QSize(250,200))
		# print("x = " + str(xPos[i]) + "   y = " + str(yPos[i]))
		# iButton.clicked.connect(self.parent().drawNav(2)) # need to figure out how to set these buttons...
		buttonLayout.addWidget(iButton, rPos[i], cPos[i])
	return buttonLayout


class NavButton(QPushButton):
	def __init__(self, iLabel, thisPath, parent=None):
		QPushButton.__init__(self, parent)
		# iButton = QPushButton(iLabel)
		self.setText(iLabel)
		iPath = os.path.join(thisPath, "sededu", "private", \
			iLabel.lower().replace(" ","").replace("\n","") + ".jpg")
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