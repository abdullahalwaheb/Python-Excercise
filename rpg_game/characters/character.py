import random
from store import items

class Character:
    #constructor
    def __init__(self, name, health, power, coins, inventory=None):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        if (inventory is None):
            inventory=[]
        self.inventory = inventory

    #status print method
    def printStatus(self):
        print(self.name, "has {} health and {} power".format(self.health, self.power))

    #attack method
    def attack(self, enemy):
        enemy.health -= self.power
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

    #items/coins dropped after the battle won
    def dropItems(self, enemy):
        self.coins += enemy.coins
        print(self.name,"earned {} coins".format(enemy.coins))

    #buy items after battle from the store
    def buyItems(self):
        raw_input = int(input())
        if (raw_input == 1 and self.coins >= itemsDict["Armor"]):
            self.inventory.append("Armor")
            self.coins -= itemsDict["Armor"]
        elif (raw_input == 2 and self.coins >= itemsDict["SuperTonic"]):
            self.inventory.append("SuperTonic")
            self.coins -= itemsDict["SuperTonic"]
        elif (raw_input == 3 and self.coins >= itemsDict["Shuriken"]):
            self.inventory.append("Shuriken")
            self.coins -= itemsDict["Shuriken"]
        elif (raw_input == 4 and self.coins >= itemsDict["Evade"]):
            self.inventory.append("Evade")
            self.coins -= itemsDict["Evade"]
        elif (raw_input == 5 and self.coins >= itemsDict["Sacrifice"]):
            self.inventory.append("Sacrifice")
            self.coins -= itemsDict["Sacrifice"]
        else:
            pass