from tkinter import *
import time
import sys

root = Tk()
root.title("TIMER CLOCK")

def get_time():
        time_string = time.strftime("%I:%M:%S")
        clock.config(text=time_string)
        clock.after(200, get_time)

clock=Label(root, font=("time", 20, "normal"))
clock.pack()

get_time()


root.mainloop()
        