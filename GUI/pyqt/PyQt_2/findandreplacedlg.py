#coding:utf-8

import re
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_AddressBook



 ui_AddressBook.Ui_MainWindow):

    def __init__(self, parent=None):

        super(QtAddressbook, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = QtAddressbook()
    form.show()
    app.exec_()