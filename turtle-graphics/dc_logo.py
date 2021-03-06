from turtle import *

#hideturtle()
#tracer(False)

def drawTri():
    right(60)
    forward(60)
    right(120)
    forward(60)
    right(120)
    forward(60)

def drawGreenQt():
    #draw
    begin_fill()
    color("green")
    drawTri()
    drawTri()
    #set pos
    penup()
    right(120)
    forward(60)
    pendown()
    #draw
    drawTri()
    end_fill()
    begin_fill()
    color("darkgreen")
    drawTri()
    #set pos
    penup()
    right(120)
    forward(60)
    pendown()
    #draw
    drawTri()
    end_fill()
    #set pos
    right(60)
    right(60)
    forward(60)
    #draw
    begin_fill()
    color("green")
    drawTri()
    end_fill()

def drawBlueQt():
    #draw
    begin_fill()
    color("blue")
    drawTri()
    drawTri()
    #set pos
    penup()
    right(120)
    forward(60)
    pendown()
    #draw
    drawTri()
    end_fill()
    begin_fill()
    color("darkblue")
    drawTri()
    #set pos
    penup()
    right(120)
    forward(60)
    pendown()
    #draw
    drawTri()
    end_fill()
    #set pos
    right(60)
    right(60)
    forward(60)
    #draw
    begin_fill()
    color("blue")
    drawTri()
    end_fill()

def drawBlueGreenJoint():
    #1st triangle
    begin_fill()
    color("blue")
    right(60)
    forward(60)
    right(120)
    forward(60)
    right(120)
    forward(60)
    end_fill()
    #2nd triangle
    begin_fill()
    color("blue")
    left(120)
    forward(60)
    left(120)
    forward(60)
    end_fill()
    #3rd triangle
    begin_fill()
    color("darkgreen")
    right(120)
    forward(60)
    right(120)
    forward(60)
    right(120)
    forward(60)
    end_fill()
    #4th triangle
    begin_fill()
    color("darkblue")
    right(60)
    forward(60)
    right(120)
    forward(60)
    end_fill()

#set initial pos
penup()
setx(-50)
sety(50)
pendown()
drawGreenQt()
#move to next pos
penup()
setx(-50)
sety(-50)
pendown()

#drawBlueQt()


done()