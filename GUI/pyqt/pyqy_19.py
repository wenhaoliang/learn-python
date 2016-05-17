
#coding:utf-8

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.button = QtGui.QPushButton(u'对话', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)

        self.button.move(20, 20)
        self.connect(self.button, QtCore.SIGNAL('clicked()'),
            self.showDialog)
        self.setFocus()

        self.label = QtGui.QLineEdit(self)
        self.label.move(130, 22)

        self.setWindowTitle(u'输入对话')
        self.setGeometry(300, 300, 350, 80)


    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, u'输入对话',
            u'输入您的名字:')

        if ok:
            self.label.setText(str(text))


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()