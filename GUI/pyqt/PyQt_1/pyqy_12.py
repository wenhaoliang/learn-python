#!/usr/bin/python
#coding:utf-8

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        #创建两个按钮
        okButton = QtGui.QPushButton("OK")
        cancelButton = QtGui.QPushButton("Cancel")

        #创建一个水平框布局，增加一个延展因素和两个按钮
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        #为了创建所需的布局，把水平布局放到垂直布局中
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        #设置窗体的主布局
        self.setLayout(vbox)

        self.setWindowTitle(u'框布局')
        self.resize(300, 150)

app = QtGui.QApplication(sys.argv)
fp = Example()
fp.show()
exit(app.exec_())