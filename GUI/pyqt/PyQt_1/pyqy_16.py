#coding:utf-8

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.setWindowTitle(u"事件重实现")
        self.resize(250, 150)

    def keyPressEvent(self, QKeyEvent):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

app = QtGui.QApplication(sys.argv)
fp = Example()
fp.show()
exit(app.exec_())