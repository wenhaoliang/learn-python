#!/usr/bin/python
#coding:utf-8

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        label1 = QtGui.QLabel(u"教程", self)
        label1.move(15, 10)

        label2 = QtGui.QLabel(u"程序", self)
        label2.move(35, 40)

        self.setWindowTitle(u"绝对位置")
        self.resize(250, 150)

app = QtGui.QApplication(sys.argv)
fp = Example()
fp.show()
exit(app.exec_())