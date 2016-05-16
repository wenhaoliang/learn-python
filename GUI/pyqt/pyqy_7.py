#!/usr/bin/python
#coding:utf-8

import sys
from PyQt4 import QtGui


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)

        self.resize(250,150)
        self.setWindowTitle(u"状态栏")

        self.statusBar().showMessage(u"准备")

app = QtGui.QApplication(sys.argv)
fp = MainWindow()
fp.show()
sys.exit(app.exec_())