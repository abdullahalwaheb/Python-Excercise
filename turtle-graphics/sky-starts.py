from turtle import *
import random

#skip animation
tracer(0,0)

#set the star and the background color
color("WhiteSmoke")
bgcolor("MidnightBlue")

#allows changing the initial pos without drawing
penup()

#change position randomly
def changePos():
    randomNum = random.randint(-290,290)
    setx(randomNum)
    randomNum = random.randint(-290,290)
    sety(randomNum)

#draw star
def starDraw():
    for side in range(5):
        pendown()
        left(144)
        forward(6)
        penup()

#draw star at random coordinates continuously. 
#60 stars, change it to more/less
for i in range(1,60):
    changePos()
    starDraw()

#freeze the screen at the end
done()

