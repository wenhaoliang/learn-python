#!/bin/env python
#coding:utf-8
import wx
import wx

class App(wx.App):

    def OnInit(self):
        frame = wx.Frame(parent = None, id = -1, title = "Bare")
        frame.Show()
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()