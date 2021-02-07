from tkinter import *

class AboutUs():
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("About us")
        self.resizable(False, False)

        self.top = Frame(self, height=650, width=650, bg="#ffa500")
        self.top.pack(fill=BOTH)

        self.text = Label(self.top, text="hey this is about page"
        '\n this application is made for educational purpose'
        '\n you can contact me on'
        '\n Facebook - https; link'
        '\n Instagram - link',
        font='arial 14 bold', bg="#ffa500", fg="white"
        )

        self.text.place(x=50, y=50)
