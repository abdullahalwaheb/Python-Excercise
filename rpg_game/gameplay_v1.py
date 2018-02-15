#imports
import sys
sys.path.append('/Users/abdullah/Desktop/DigitalCrafts/Python/rpg_game/characters')
from character_class import *
from store import items
#add two characters to the list to battle one another
chList = []
#select your character
def characterSelect():
    #the while loop will validate the user's selection for character
    while (chList == []):
        print("")
        print("Select your character")
        print("=======================")
        print("1. Hero")
        print("2. Archer")
        print("3. Medic")
        print("4. Shadow")
        print("5. Quit")
        print(">>", end=" ")
        raw_input = input()
        if (raw_input == "1"):
            hero = Hero("Hero",10,5,0,None)
            chList.append(hero)
        elif (raw_input == "2"):
            archer = Archer("Archer",8,4,0,None)
            chList.append(archer)
        elif (raw_input == "3"):
            medic = Medic("Medic",9,3,0,None)
            chList.append(medic)
        elif (raw_input == "4"):
            shadow = Shadow("Shadow",1,7,0,None)
            chList.append(shadow)
        elif (raw_input == "5"):
            print("Goodbye!")
            quit()
        else:
            print("Invalid selection {}".format(raw_input))
#select the enemy
def enemySelection():
    #the while loop will validate the user's selection for enemy
    while (len(chList)<2):
        print("")
        print("Select your enemy")
        print("=======================")
        print("1. Goblin")
        print("2. Dark Knight")
        print("3. Zombie")
        print(">>", end=" ")
        raw_input = input()
        if (raw_input == "1"):
            goblin = Goblin("Goblin",7,2,5,None)
            chList.append(goblin)
        elif (raw_input == "2"):
            d_knight = Dark_Night("Dark Knight",9,2,6,None)
            chList.append(d_knight)
        elif (raw_input == "3"):
            zombie = Zombie("Zombie",99999999,1,0,None)
            chList.append(zombie)
        else:
            print("Invalid selection {}".format(raw_input))
#print character and enmey status
def charactersStatus():
    chList[0].printStatus()
    chList[1].printStatus()
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