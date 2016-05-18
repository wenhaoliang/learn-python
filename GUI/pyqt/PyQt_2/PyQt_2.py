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
        FontStyleLabel = QLabel(u"中文字体:")#文本框
        FontstyleComboBox = QComboBox()#组合框
        FontstyleComboBox.addItems([u"宋体", u"黑体", u"仿宋",
                                    u"隶书", u"楷体"])#添加组合下拉框
        FontSizeLabel = QLabel(u"字体大小")#文本框
        FontSizeSpinBox = QSpinBox()#QspinBox类是一个带有上下箭头的，可以调整数据值大小的旋转按钮，如文本编辑软件中调整字体大小的剖件一样
        FontSizeSpinBox.setRange(0, 90)#设置数值范围


        FontEffectCheckBox = QCheckBox(u"使用特效")#创建一个复选框
        okButton = QPushButton(u"确定")#创建按键
        cancelButton = QPushButton(u"取消")#创建按键
        # 确定控件的布局
        '''
        常用的三种布局方法：
        （1）使用水平布局类QHBoxLayout；
        （2）使用垂直布局类QVBoxLayout；
        （3）使用网格布局类QGridLayout。
        '''
        buttonLayout = QHBoxLayout()#水平布局
        buttonLayout.addStretch()#空白弹簧，控制两个控件之间的距离
        buttonLayout.addWidget(okButton)#添加按键
        buttonLayout.addWidget(cancelButton)#添加按键
        layout = QGridLayout()#网格布局
        layout.addWidget(FontStyleLabel, 0, 0)
        layout.addWidget(FontstyleComboBox, 0, 1)
        layout.addWidget(FontSizeLabel, 1, 0)
        layout.addWidget(FontSizeSpinBox, 1, 1)
        layout.addWidget(FontEffectCheckBox, 1, 2)
        layout.addLayout(buttonLayout, 2, 0, 2, 3)
        '''
        layout.addLayout(buttonLayout, x, y, z, p)
        x,y 确定控件在网格中的位置
        z,p 确定控件所占行与列
        '''
        self.setLayout(layout)
        # 窗口的标题
        self.setWindowTitle(u"字体")

app = QApplication(sys.argv)
font = FontPropertiesDlg()
font.show()
app.exec_()