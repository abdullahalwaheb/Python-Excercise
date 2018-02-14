class Character:

    #constructor
    def __init__(self, name, health, power, specialAttribute):
        self.name = name
        self.health = health
        self.power = power
        self.specialAttribute = specialAttribute

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