# ------ completed/submitted ------
#----------------------uncomment block to use---------------------

#imports
import math
import numpy
import random
from matplotlib import pyplot
from numpy import arange

# #----------------------Hello Function---------------------
# def hello(name):
#     print("Hello", name)

# hello("John")


# #----------------------X+1---------------------
# def f(x):
#     return(x+1)

# def run():
#     xs = list(range(-3, 4))
#     ys = []
#     for x in xs:
#         ys.append(f(x))

#     pyplot.plot(xs, ys)
#     pyplot.show()

# if __name__ == "__main__":
#     run()


# #---------------------Square of X---------------------
# def f(x):
#     return(x*x)

# def run():
#     xs = list(range(-100, 101))
#     ys = []
#     for x in xs:
#         ys.append(f(x))

#     pyplot.plot(xs, ys)
#     pyplot.show()

# if __name__ == "__main__":
#     run()

# #---------------------Odd or even---------------------
# def f(x):
#     if (x%2 == 0):
#         return(-1)
#     elif (x%2 <= 1):
#         return(1)

# def run():
#     xs = list(range(-5,6))
#     ys = []
#     for x in xs:
#         ys.append(f(x))

#     pyplot.bar(xs,ys)
#     pyplot.show()

# if __name__ == "__main__":
#     run()


# #---------------------Sine---------------------
# def f(x):
#     return(math.sin(x))

# def run():
#     xs = list(range(-5,6))
#     ys = []
#     for x in xs:
#         ys.append(f(x))

#     pyplot.plot(xs,ys)
#     pyplot.show()

# if __name__ == "__main__":
#     run()


# #---------------------Sine 2---------------------
# def f(x):
#     return(math.sin(x))

# def run():
#     xs = arange(-5,6,0.1)
#     ys = []
#     for x in xs:
#         ys.append(f(x))

#     pyplot.plot(xs,ys)
#     pyplot.show()

# if __name__ == "__main__":
#     run()


# #---------------------Temperature---------------------
# def f(x):
#     temp = (x*1.8)+32
#     return temp

# def run(x):
#     #calc temperature
#     temp = ((x*1.8)+32)
#     #set background color
#     ax = pyplot.subplot()
#     ax.set_facecolor('blue')  
#     #plot and draw
#     pyplot.plot([temp],[temp],"ro")
#     pyplot.axis([0, 160, 0, 160])
#     pyplot.show()

# if __name__ == "__main__":
#     run(40)


# #---------------------Play Again / Play again? Again---------------------
# def play(*answer):
#     randomList = ["Brave!","Keep Fighting","Go on champ!","Look at ya","Let's go"]
#     answer = input("Do you want to play again? ")

#     if (answer == "Y" or answer == "y"):
#         print(random.choice(randomList))
#         return play()
#     elif (answer == "N" or answer == "n"):
#         print("Looser, bye")
#         exit
#     else:
#         #to force the user to enter either Y or N
#         print("Invalid answer!")
#         play()

# if __name__ == "__main__":
#     play()