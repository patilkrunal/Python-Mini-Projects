import time
from turtle import *

setup()
tl = Turtle()
tl.speed(0)
hours = 2
minutes = 59
seconds = 56

while True:
        tl.clear()
        tl.write(str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2), font=("arial", 35, "normal"))
        seconds += 1
        time.sleep(1)
        
        if seconds == 60:
                seconds = 0
                minutes += 1
        
        if minutes == 60:
                minutes = 0
                hours += 1
        
        