#!/usr/bin/python
#coding:utf-8

import sys
from PyQt4 import QtGui, QtCore

class Center(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle(u"在中央显示")
        self.resize(250, 150)
        self.center()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

app = QtGui.QApplication(sys.argv)
fp = Center()
fp.show()
sys.exit(app.exec_())