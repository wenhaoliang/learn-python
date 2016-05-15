from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text = "hello, world")
        self.helloLabel.pack()
        self.quitButton = Button(self, text = 'Quit', command = self.quit)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or "wrold"
        tkMessageBox.showinfo("Message", "hello, %s" % name)

app = Application()
app.master.title("hello world")
app.mainloop()
