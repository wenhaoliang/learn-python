#coding:utf-8

import wx

class Frame(wx.Frame):

    def __init__(self, image, parent = None, id = -1,
                 pos = wx.DefaultPosition,
                 title = "hello, wxpython!"):

        #显示图像
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.bmp = wx.StaticBitmap(parent = self, bitmap = temp)

class App(wx.App):

    def OnInit(self):
        image = wx.Image('hi.jpg', wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)

        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()