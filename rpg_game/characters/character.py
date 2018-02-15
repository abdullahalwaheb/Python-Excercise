import random

class Character:

    #constructor
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

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

            


