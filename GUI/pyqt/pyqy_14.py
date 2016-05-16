#coding:utf-8


import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        title = QtGui.QLabel(u"标题")
        author = QtGui.QLabel(u"作者")
        review = QtGui.QLabel(u"评论")

        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1,0)
        grid.addWidget(titleEdit, 1,1)

        grid.addWidget(author, 2,0)
        grid.addWidget(authorEdit,2,1)

        grid.addWidget(review, 3,0)
        grid.addWidget(reviewEdit,3,1,5,1)

        self.setLayout(grid)

        self.setWindowTitle(u"网格布局")
        self.resize(450,300)

app = QtGui.QApplication(sys.argv)
fp = Example()
fp.show()
exit(app.exec_())