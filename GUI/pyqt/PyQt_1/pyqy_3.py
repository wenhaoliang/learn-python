#!/usr/bin/python
#coding:utf-8

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class Tooltip(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle(u"你好啊")

        self.setToolTip(u'这是一个小部件233')
        QtGui.QToolTip.setFont(QtGui.QFont())

app = QtGui.QApplication(sys.argv)
tooltip = Tooltip()
tooltip.show()
sys.exit(app.exec_())