#incomplete - work in progress
import random

randomNum = random.randint(1,100)
print("Is the number in your head:", randomNum)

def rounder():
    randomNum = randomNum - 10

while True:
    try:
        choice = int(input("1.Higher\n2.Less\n3.You got it!)\n"))
        if(choice==1):
            print("too high")
            break
        elif (choice==2):
            print("too low")
            break
        elif (choice==3):
            print("thats it")
            break
    except ValueError:
        print("invalid option")


