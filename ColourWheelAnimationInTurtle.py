#################### COLOUR WHEEL IN PYTHON #####################

# import graphics capabilities from turtle module
from turtle import *
# create a window for the graphics
setup()
# create a turtle pen for drawing
tl = Turtle()

# list of colours to randomly choose from
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# import random capabilities
import random

# basic turtle setup
# pickup the pen so no marks are left
tl.up()
# move the turtle to the left
tl.goto(-200, 0)
# put the pen back down to start marking
tl.down()
# change pen thickness
tl.width(5)
# hide the turtle icon
tl.hideturtle()
# set turtle speed to maximum
tl.speed(0) 

# create a loop for the graphics to be built
for i in range(9001):
    # chooose a random colour for the turtle
    colorchoice = random.choice(colors)
    # have the turtle take randomly choosen color
    tl.color(colorchoice)
    # move the turtle forward
    tl.forward(400)
    # have the turtle turn 181 degrees (anything over 180 degrees works)
    tl.right(181)
