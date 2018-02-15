from charSelection import *
#start playing   
def play():
    characterSelect()
    enemySelection()
    while (chList[0].isAlive() and chList[1].isAlive()):
        charactersStatus()
        print("")
        print("Select an action")
        print("1. Attack!")
        print("2. Stand By")
        print("3. Flee")
        print(">>", end=" ")
        raw_input = int(input())
        #good attacks evil
        if (raw_input == 1):
            #normal attacs
            chList[0].attack(chList[1])
            #random status if 20% is met
            chList[0].randomStatus(chList[1])
            #enemy dies
            if (chList[1].health <= 0):
                print(chList[1].name, "is ☠️") 
                #enemy drops items
                chList[0].dropItems(chList[1])
                items.listItems()
                #character purchase items
                chList[0].buyItems()
                #test if item was obtained and coins were spent
                for i in chList[0].inventory:
                    print(i)
                print(chList[0].coins)
        elif (raw_input == 2):
            pass
        elif (raw_input == 3):
            print("\U0001F4A8")
            break
        else:
            print("Invalid input {}".format(raw_input))
        #evil attacks character
        if (chList[1].health > 0):
            chList[1].attack(chList[0])
            #character dies
            if (chList[0].health <= 0):
                print(chList[0].name, "is ☠️")
                print("---GAME OVER---")

def main():
    play()

if __name__ == "__main__":
    main()