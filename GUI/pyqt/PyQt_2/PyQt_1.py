#coding:utf-8
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
button = QtGui.QPushButton(u"你好啊")
button.show()
app.exec_()