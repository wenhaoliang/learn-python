#coding:utf-8

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.connect(self, QtCore.SIGNAL('closeEmitApp()'),
            QtCore.SLOT('close()'))

        self.setWindowTitle('emit')
        self.resize(250, 150)


    def mousePressEvent(self, event):
        self.emit(QtCore.SIGNAL('closeEmitApp()'))


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())