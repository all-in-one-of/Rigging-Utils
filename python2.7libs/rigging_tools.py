from hutil.Qt import QtGui
from hutil.Qt import QtWidgets
from hutil.Qt import QtCore

import hou

import rigutils

class RiggingTools(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        # UI
        makerctrl = QtWidgets.QPushButton("Make R CTRL", self)
        makerctrl.setCheckable(False)
        scaleButtonLayout = QtWidgets.QHBoxLayout()
        scaleButtonLayout.addWidget(makerctrl)
        scaleButtonLayout.addStretch()

        makerctrlclicked = makerctrl.clicked.connect(self.makerctrl)

        masterLayout = QtWidgets.QVBoxLayout()
        masterLayout.addLayout(scaleButtonLayout)

        masterLayout.addStretch()

        self.setLayout(masterLayout)

    def makerctrl(self):
        rigutils.makeRctrl()



