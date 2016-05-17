#!/usr/bin/python
#coding:utf-8

import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(350, 250)
        self.setWindowTitle(u"把它们放在一起")

        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        exit = QtGui.QAction(QtGui.QIcon("icon/exit.png"), u'退出', self)
        exit.setShortcut("Ctrl+Q")
        exit.setStatusTip(u"退出")
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu(u"&菜单")
        file.addAction(exit)

        toolbar = self.addToolBar(u'退出')
        toolbar.addAction(exit)

app = QtGui.QApplication(sys.argv)
fp = MainWindow()
fp.show()
sys.exit(app.exec_())
