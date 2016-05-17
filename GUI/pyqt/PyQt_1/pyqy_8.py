#!/usr/bin/python
#coding:utf-8

import sys
from PyQt4 import QtGui, QtCore


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle(u"菜单栏")

        exit = QtGui.QAction(QtGui.QIcon("icon/exit.png"), u"退出", self)
        exit.setShortcut("Ctrl+Q")
        exit.setStatusTip(u"退出程序")
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu(u'&菜单')
        file.addAction(exit)

app = QtGui.QApplication(sys.argv)
fp = MainWindow()
fp.show()
exit(app.exec_())