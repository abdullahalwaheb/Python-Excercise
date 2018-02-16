import sys
sys.path.append('/Users/abdullah/Desktop/DigitalCrafts/Python/rpg_game/store')
import random
from items import *

class Character:
    #constructor
    def __init__(self, name, health, power, defence, coins, inventory=None):
        self.name = name
        self.health = health
        self.power = power
        self.defence = defence
        self.coins = coins
        if (inventory is None):
            inventory=[]
        self.inventory = inventory

    #status print method
    def printStatus(self):
        print(self.name, "has {} health, {} power and {} coins".format(self.health, self.power, self.coins))

    #attack method
    def attack(self, enemy):
        enemy.health -= (self.power-enemy.defence)
        print(self.name, "🗡️ ", enemy.name, "and does {} damage".format(self.power))

    #alive or dead boolean method
    def isAlive(self):
        if (self.health > 0):
            return True
    
    #random status that occurs during attack
    def randomStatus(self,enemy):        
        #getting 5 from range 1-5 would be a 20% probablity
        someNum = random.randint(1,5)
        if (self.name == "Hero" and someNum == 5):
            enemy.health -= self.power
            print("Double Attack!", self.name, "🗡️ ", enemy.name, "again and does {} damage".format(self.power))
        elif (self.name == "Medic" and someNum == 5):
            self.health += 2
            print(self.name,"has restored 2 health points")
        elif (self.name == "Archer" and someNum == 5):
            enemy.health -= 999
            print("Deadly Arrow!!",self.name, "instantly kills", enemy.name)
        elif (self.name == "Shadow" and someNum < 5):
            self.health += enemy.power
            print(self.name,"Evades incoming hits")
        else:
            pass

    #coins dropped after the battle won
    def dropCoins(self, enemy):
        self.coins += enemy.coins
        print(self.name,"earned {} coins".format(enemy.coins))

    #buy items after battle from the store
    def buyItems(self):
        while True:
            raw_input = input()
            if (raw_input == "1" and self.coins >= itemsDict["Armor"]):
                self.inventory.append("Armor")
                self.coins -= itemsDict["Armor"]
                break
            elif (raw_input == "2" and self.coins >= itemsDict["SuperTonic"]):
                self.inventory.append("SuperTonic")
                self.coins -= itemsDict["SuperTonic"]
                break
            elif (raw_input == "3" and self.coins >= itemsDict["Shuriken"]):
                self.inventory.append("Shuriken")
                self.coins -= itemsDict["Shuriken"]
                break
            elif (raw_input == "4" and self.coins >= itemsDict["Evade"] and self.inventory.count("Evade") < 4):
                self.inventory.append("Evade")
                self.coins -= itemsDict["Evade"]
                break
            elif (raw_input == "4" and self.coins >= itemsDict["Evade"] and self.inventory.count("Evade") == 4):
                print ("Cannot carry more Evade, max is reached")
            elif (raw_input == "5" and self.coins >= itemsDict["Sacrifice"]):
                self.inventory.append("Sacrifice")
                self.coins -= itemsDict["Sacrifice"]
                break
            elif (raw_input == "6"):
                break
            else:
                print("Invalid choice, choose an item again")
        
    #use item and update character status
    def useItemVsEnemy(self, enemy, itemUsed):
        while True:
            if (itemUsed == "Armor" or itemUsed == "armor"):
                self.inventory.remove("Armor")
                self.defence += 1
                print("Used Armor and boosted defence")
                break
            elif (itemUsed == "SuperTonic" or itemUsed == "supertonic"):
                self.inventory.remove("SuperTonic")
                self.health += 2
                print("Used SuperTonic and restored 2 health points")
                break
            elif (itemUsed == "Shuriken" or itemUsed == "shuriken"):
                self.inventory.remove("Shuriken")
                self.power += 5
                print("Used Shuriken and boosted power")
                break
            elif (itemUsed == "Evade" or itemUsed == "evade"):
                self.inventory.remove("Evade")
                self.health += enemy.power
                print("Used Evade and dodged incoming hit!")
                break
            elif (itemUsed == "Sacrifice" or itemUsed == "sacrificed"):
                self.inventory.remove("Sacrifice")
                self.health = 0
                print("May your soul rest in peace Guardian")
                break
            else:
                print("{} is unavailable".format(itemUsed))
                print("{} lost turn".format(self.name))
                return False

