from charSelection import *
from character_action import *

def battle():
    while (chList[0].isAlive() and chList[1].isAlive()):
        print("")
        print("Select an action")
        print("1. Attack!")
        print("2. Stand By")
        print("3. Use Item")
        print("4. Flee")
        print(">>", end=" ")
        charactersStatus()
        raw_input = input()
        #good attacks evil
        if (raw_input == "1"):
            #normal attack
            chList[0].attack(chList[1])
            #execute random status if 20% is met
            chList[0].randomStatus(chList[1])
            #enemy dies
            if (chList[1].health <= 0):
                print(chList[1].name, "is ☠️") 
                #enemy drops coins
                chList[0].dropCoins(chList[1])
                #show store
                items.listItems()
                #character purchase items
                chList[0].buyItems()
                #test if item was obtained and coins were spent
                print("Inventory")
                print("=================")
                for item in chList[0].inventory:
                    print(item)
                print("")
                print("Coins")
                print("=================")
                print(chList[0].coins,"coins available")
                #keep playing (remove dead enemy and add a new one)
                print("")
                print("Keep Fighting")
                chList.remove(chList[1])
                enemySelection()
        elif (raw_input == "2"):
            pass
        elif (raw_input == "3"):
            if (len(chList[0].inventory) <=0):
                print("No items available")
                battle()
            else:
                for i in chList[0].inventory:
                    print(i)
            chList[0].useItemVsEnemy(chList[1], input(">> Type item to use: "))
        elif (raw_input == "4"):
            print("\U0001F4A8")
            break
        else:
            print("Invalid input {}".format(raw_input))
            battle()
        #evil attacks character
        if (chList[1].health > 0):
            chList[1].attack(chList[0])
            #character dies
            if (chList[0].health <= 0):
                print(chList[0].name, "is ☠️")
                print("---GAME OVER---")
                break
