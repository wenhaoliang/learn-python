#!/usr/bin/python
#coding:utf-8

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class QuitButton(QtGui.QWidget):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle(u"退出")

        quit = QtGui.QPushButton(u"关闭", self)
        quit.setGeometry(100, 100, 64, 35)

        self.connect(quit, QtCore.SIGNAL("clicked()"),
                     QtGui.qApp, QtCore.SLOT("quit()"))


app = QtGui.QApplication(sys.argv)
qb = QuitButton()
qb.show()
sys.exit(app.exec_())
