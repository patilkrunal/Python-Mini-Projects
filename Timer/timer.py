from tkinter import *

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.h = 0
        self.m = 0
        self.s = 0
        self.clock=Label(root, font=("time", 20, "bold"), width= 13, fg='yellow', bg='black')
        self.clock.pack(fill=BOTH, expand=1)
        self.get_time()

    def get_time(self):
        time_string = str(self.h).zfill(2)+":"+str(self.m).zfill(2)+":"+str(self.s).zfill(2)
        self.clock.config(text=time_string)
        
        self.update_time()
        self.clock.after(1000, self.get_time)

    def update_time(self):
        self.s += 1
        if self.s == 60:
            self.s = 0
            self.m += 1
        if self.m == 60:
            self.m = 0
            self.h += 1

if __name__ == "__main__":
    root = Tk()
    app = App(master=root)
    root.mainloop()