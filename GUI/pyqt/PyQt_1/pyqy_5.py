#!/usr/bin/python
#coding:utf-8

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class MessageBox(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle(u"退出信息")

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, u'你好啊',
            u'你确定要退出吗？', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
                event.accept()
        else:
                event.ignore()

app = QtGui.QApplication(sys.argv)
qb = MessageBox()
qb.show()
sys.exit(app.exec_())