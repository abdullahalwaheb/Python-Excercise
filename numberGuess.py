#-----------------------Guess a number game---------------------
import random
#variables
answer = 0
randomNum = random.randint(1,10)

#start
def guessNum():
    chance = 3
    #user prompt
    print("\nHint! the secret number is: ",randomNum)
    #guess logic
    while True:
        try:
            answer = int(input("What is the secret number? Choose from 1 to 10\n(3 Chances available)\n"))
            if (answer == randomNum):
                print("Spot on! you win")   
            else:
                while (answer != randomNum):
                    chance -= 1
                    print("Wrong answer, you have %d chance left. Try again" % chance)
                    answer = int(input("What is the secret number?\n"))
                    if (answer == randomNum):
                        print("Spot on! you win") 
                        break
                    if (chance == 1):
                        print("No chances left, next time!")
                        break
        except ValueError:
            print("Entry must be a number")
        else:
            break

#calling methods
guessNum()