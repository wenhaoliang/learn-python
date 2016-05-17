#!/usr/bin/env python
# coding=utf-8

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class FontPropertiesDlg(QDialog):
    # 初始化
    def __init__(self, parent=None):
        # super函数完成对话框的初始化
        super(FontPropertiesDlg, self).__init__(parent)
        FontStyleLabel = QLabel(u"中文字体:")
        FontstyleComboBox = QComboBox()
        FontstyleComboBox.addItems([u"宋体", u"黑体", u"仿宋",
                                    u"隶书", u"楷体"])
        FontSizeLabel = QLabel(u"字体大小")
        FontSizeSpinBox = QSpinBox()
        FontSizeSpinBox.setRange(0, 90)


        FontEffectCheckBox = QCheckBox(u"使用特效")
        okButton = QPushButton(u"确定")
        cancelButton = QPushButton(u"取消")
        # 确定控件的布局
        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)
        layout = QGridLayout()
        layout.addWidget(FontStyleLabel, 0, 0)
        layout.addWidget(FontstyleComboBox, 0, 1)
        layout.addWidget(FontSizeLabel, 1, 0)
        layout.addWidget(FontSizeSpinBox, 1, 1)
        layout.addWidget(FontEffectCheckBox, 1, 2)
        layout.addLayout(buttonLayout, 2, 0, 1, 3)
        self.setLayout(layout)
        # 窗口的标题
        self.setWindowTitle(u"字体")

app = QApplication(sys.argv)
font = FontPropertiesDlg()
font.show()
app.exec_()