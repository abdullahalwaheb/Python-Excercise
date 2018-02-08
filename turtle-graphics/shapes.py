from turtle import *

#changing the icon to a turtle
shape("turtle")

#circle
def circleDraw():
    pencolor("black")
    width(5)
    circle(90)

#hexagon
def hexagonDraw():
    for i in range(6):
        forward(90)
        right(360/6)

#octagon
def octagonDraw():
    for i in range(8):
        forward(70)
        right(360/8)

#pentagon
def pentagonDraw():
    for i in range(5):
        forward(90)
        right(360/5)

#square
def squareDraw():
    for i in range(4):
        forward(100)
        right(90)

#star
def starDraw():
    for i in range(5):
        forward(100)
        right(144)

#triangle
def triangleDraw():
    right(60)
    forward(200)
    right(120)
    forward(200)
    right(120)
    forward(200)