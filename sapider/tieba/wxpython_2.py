#coding:utf-8

import wx

class Frame(wx.Frame):
    pass

class App(wx.App):

    def OnInit(self):
        self.frame = Frame(parent = None, title = "Spare")
        self.frame.show()

