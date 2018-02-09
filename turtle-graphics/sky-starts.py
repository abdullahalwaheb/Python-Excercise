from turtle import *

def starDraw():
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(50)
    end_fill()
    penup()

#this will draw a light grey star on a dark blue background
color("WhiteSmoke")
bgcolor("MidnightBlue")

#use the function to draw stars!
starDraw()
forward(100)
starDraw()
left(120)
forward(150)
starDraw()
