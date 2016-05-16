#coding:utf-8

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        lcd = QtGui.QLCDNumber(self)
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        self.connect(slider, QtCore.SIGNAL('valueChanged(int)'), lcd,
                     QtCore.SLOT('display(int)'))

        self.setWindowTitle(u"信号与插槽")
        self.resize(250,150)

app = QtGui.QApplication(sys.argv)
fp = Example()
fp.show()
exit(app.exec_())