#!/usr/bin/python
#coding:utf-8

import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle(u'工具栏')

        self.exit = QtGui.QAction(QtGui.QIcon('icon/exit.png'), 'Exit', self)
        self.exit.setShortcut('Ctrl+Q')
        self.connect(self.exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.toolbar = self.addToolBar(u'退出')
        self.toolbar.addAction(self.exit)

app = QtGui.QApplication(sys.argv)
fp = MainWindow()
fp.show()
exit(app.exec_())
