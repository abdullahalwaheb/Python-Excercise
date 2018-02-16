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
            hero = Hero("Hero",100,5,0,0,None)
            chList.append(hero)
        elif (raw_input == "2"):
            archer = Archer("Archer",8,5,0,0,None)
            chList.append(archer)
        elif (raw_input == "3"):
            medic = Medic("Medic",9,3,0,0,None)
            chList.append(medic)
        elif (raw_input == "4"):
            shadow = Shadow("Shadow",1,7,0,0,None)
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
            goblin = Goblin("Goblin",7,2,0,5,None)
            chList.append(goblin)
        elif (raw_input == "2"):
            d_knight = Dark_Night("Dark Knight",9,2,0,6,None)
            chList.append(d_knight)
        elif (raw_input == "3"):
            zombie = Zombie("Zombie",99999999,1,0,0,None)
            chList.append(zombie)
        else:
            print("Invalid selection {}".format(raw_input))
#print character and enmey status
def charactersStatus():
    chList[0].printStatus()
    chList[1].printStatus()