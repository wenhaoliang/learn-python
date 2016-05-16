#!/usr/bin/python
#coding:utf-8

import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle(u"你好啊")
widget.show()

sys.exit(app.exec_())
