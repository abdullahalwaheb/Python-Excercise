#imports
import sys
sys.path.append('/Users/abdullah/Desktop/DigitalCrafts/Python/rpg_game/characters')
from character_class import *
#add two characters to the list to battle one another
chList = []

def characterSelect():
    print("")
    print("Select your character")
    print("=======================")
    print("1. Hero")
    print("2. Archer")
    print("3. Medic")
    print("4. Shadow")
    print("5. Quit")
    print(">>", end=" ")
    raw_input = int(input())
    if (raw_input == 1):
        hero = Hero("Hero",10,5)
        chList.append(hero)
    elif (raw_input == 2):
        archer = Archer("Archer",8,4)
        chList.append(archer)
    elif (raw_input == 3):
        medic = Medic("Medic",9,3)
        chList.append(medic)
    elif (raw_input == 4):
        shadow = Shadow("Shadow",1,7)
        chList.append(shadow)
    elif (raw_input == 5):
        print("Goodbye!")
        quit()
    else:
        print("Invalid selection {}".format(raw_input))

def enemySelection():
    print("")
    print("Select your enemy")
    print("=======================")
    print("1. Goblin")
    print("2. Dark Knight")
    print("3. Zombie")
    print(">>", end=" ")
    raw_input = int(input())
    if (raw_input == 1):
        goblin = Goblin("Goblin",7,2)
        chList.append(goblin)
    elif (raw_input == 2):
        d_knight = Dark_Night("Dark Knight",9,2)
        chList.append(d_knight)
    elif (raw_input == 3):
        zombie = Zombie("Zombie",999,1)
        chList.append(zombie)
    else:
        print("Invalid selection {}".format(raw_input))

def charactersStatus():
    chList[0].printStatus()
    chList[1].printStatus()
    
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
            #normal attac
            chList[0].attack(chList[1])
            #random status if 20% is met
            chList[0].randomStatus(chList[1])
            if (chList[1].health <= 0):
                print(chList[1].name, "is ☠️")     
        elif (raw_input == 2):
            pass
        elif (raw_input == 3):
            print("\U0001F4A8")
            break
        else:
            print("Invalid input {}".format(raw_input))
        #evil attacks you
        if (chList[1].health > 0):
            chList[1].attack(chList[0])
            if (chList[0].health <= 0):
                print(chList[0].name, "is ☠️")

def main():
    play()

if __name__ == "__main__":
    main()