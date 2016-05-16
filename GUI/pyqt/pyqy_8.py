#!/usr/bin/python
#coding:utf-8

import sys
from PyQt4 import QtGui, QtCore


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)

        self.resize(250, 150)
        self.setWindowTitle(u"菜单栏")

        exit = QtGui.QApplication.QIcon("icons")