#!/bin/env python
#coding:utf-8
import wx

app = wx.App()
window = wx.Frame(None, title = u"你好啊,wxPython", size = (400, 300))
panel = wx.Panel(window)
label = wx.StaticText(panel, label = u"你好啊~~~~", pos = (100, 100))
window.Show(True)
app.MainLoop()