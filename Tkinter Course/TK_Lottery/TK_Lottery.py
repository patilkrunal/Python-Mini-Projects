##  A SIMPLE APPLICATION TO PICK NUMBERS FOR A LOTTERY ENTRY
# Planning the program
    #   Program purpose
    #     • The program will generate a series of six unique random numbers
    #       in the range (1-59) and have the ability to be reset.
    #   Functionality required
    #     • A function to generate and display six unique random numbers.
    #     • A function to clear the last six random numbers from display.
    #  Interface widgets needed
    #     • One non-resizable window to contain all other widgets and to
    #       display the application title.
    #     • One Label widget to display a static application logo image –
    #       just to enhance the appearance of the interface.
    #     • Six Label widgets to dynamically display the generated series
    #       of unique random numbers – one number per Label.
    #     • One Button widget to generate and display the numbers in the
    #       Label widgets when this Button gets clicked. This Button
    #       will not be enabled when the numbers are on display.
    #     • One Button widget to clear the numbers on display in
    #       the Label widgets when this Button gets clicked. This
    #       Button will not be enabled when the numbers are not on display.
# DESIGNING THE INTERFACE
    #   Nos in firstrow
    #   Buttons in second row span 4 & 2 columns
# ASSIGNING STATIC PROPERTIES
    #   These values will not change during execution of the program
# INITIALIZING DYNAMIC PROPERTIES
    #   initial values can now be specified for those properties whose
    #   values will change dynamically during execution of the program.
# ADDING RUNTIME FUNCTIONALITY
    #   Functionality to respond to clicks on the Button widgets during
    #   execution of the program
# TESTING THE PROGRAM
# INSTALLING A FREEZING TOOL
    #   To ensure the application will execute successfully without the
    #   Python interpreter, your program files can be “frozen” into a
    #   bundle within a single stand-alone executable file. The
    #   “PyInstaller” tool is a free program for freezing Python scripts
    #   into executables for Windows, Linux, or Mac. 
# FREEZING THE PROGRAM
    #   Applications developed in the Python language can be frozen for
    #   Windows, Linux, and Mac systems using the PyInstaller tool

#==========================================================================
# FREEZING THE PROGRAM
import os
def resource_path(relative_path):
    absolute_path = os.path.abspath(__file__)
    root_path = os.path.dirname(absolute_path)
    base_path = getattr(sys, '_MEIPASS', root_path)
    print("****", base_path)
    return os.path.join(base_path, relative_path)

# WIDGETS:
from tkinter import *

window = Tk()
img = PhotoImage(file=resource_path('favicon.png'))

imgLbl = Label(window, image=img)
label1 = Label(window, relief='groove', width=2)
label2 = Label(window, relief='groove', width=2)
label3 = Label(window, relief='groove', width=2)
label4 = Label(window, relief='groove', width=2)
label5 = Label(window, relief='groove', width=2)
label6 = Label(window, relief='groove', width=2)
getBtn = Button(window)
rstBtn = Button(window)

# GEOMETRY:
imgLbl.grid(row=1, column = 1, rowspan = 2)
label1.grid(row = 1, column = 2, padx = 10)
label2.grid(row = 1, column = 3, padx = 10)
label3.grid(row = 1, column = 4, padx = 10)
label4.grid(row = 1, column = 5, padx = 10)
label5.grid(row = 1, column = 6, padx = 10)
label6.grid(row = 1, column = 7, padx = (10, 20))
getBtn.grid(row = 2, column = 2, columnspan = 4)
rstBtn.grid(row = 2, column = 6, columnspan = 2)

# STATIC PROPERTIES:
window.title("Lottery Number Picker")
window.resizable(0, 0)

getBtn.configure(text = 'Get My Lucky Numbers')
rstBtn.configure(text = 'Reset')
    
# INITIAL PROPERTIES:
label1.configure(text = '...')
label2.configure(text = '...')
label3.configure(text = '...')
label4.configure(text = '...')
label5.configure(text = '...')
label6.configure(text = '...')

rstBtn.configure(state=DISABLED)

# DYNAMIC PROPERTIES
from random import sample

def pick():
    nums = sample(range(1, 59), 6)
    label1.configure(text = nums[0])
    label2.configure(text = nums[1])
    label3.configure(text = nums[2])
    label4.configure(text = nums[3])
    label5.configure(text = nums[4])
    label6.configure(text=nums[5])
    getBtn.configure(state=DISABLED)
    rstBtn.configure(state=NORMAL)

def reset():
    label1.configure(text='...')
    label2.configure(text='...')
    label3.configure(text='...')
    label4.configure(text='...')
    label5.configure(text='...')
    label6.configure(text='...')
    getBtn.configure(state=NORMAL)
    rstBtn.configure(state=DISABLED)

getBtn.configure(command=pick)
rstBtn.configure(command=reset)

# SUSTAIN WINDOW:
window.mainloop()