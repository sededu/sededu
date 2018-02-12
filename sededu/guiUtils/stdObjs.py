import os
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

def mainLayout(inList, thisPath):
	buttonLayout = QGridLayout()
	nList = len(inList)
	xPos = np.tile([0, 1], int(np.ceil(nList/2)))
	yPos = np.tile(range(int(np.ceil(nList/2))), 2)
	for i in range(nList):
		iLabel = inList[i]
		iButton = QPushButton(iLabel)
		iPath = os.path.join(thisPath, "sededu", "private", \
			iLabel.lower().replace(" ","").replace("\n","") + ".jpg")
		# print(iPath)
		iIcon = QtGui.QIcon()
		iIcon.addPixmap(QtGui.QPixmap(iPath))
		iButton.setIcon(iIcon)
		iButton.setIconSize(QtCore.QSize(300,200))
		buttonLayout.addWidget(iButton, xPos[i], yPos[i])
	return buttonLayout


def quitButton(self):
	# this is old tk code
    self.quitButton = tk.Button(self, text='Quit',
        command=self.quit)
    self.quitButton.grid()
    return self


def etcButton(btnStr):
	etcBtn = QPushButton(btnStr)
	etcBtn.resize(1,10)
	return etcBtn

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