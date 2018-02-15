from character import Character

class Hero(Character):
    #constructor
    def __init__(self, name, health, power, coins, inventory=None):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        if (inventory is None):
            inventory=[]
        self.inventory = inventory

class Archer(Character):
    #constructor
    def __init__(self, name, health, power, coins, inventory=None):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        if (inventory is None):
            inventory=[]
        self.inventory = inventory

class Medic(Character):
    #constructor
     def __init__(self, name, health, power, coins, inventory=None):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        if (inventory is None):
            inventory=[]
        self.inventory = inventory

class Shadow(Character):
    #constructor
    def __init__(self, name, health, power, coins, inventory=None):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        if (inventory is None):
            inventory=[]
        self.inventory = inventory

class Zombie(Character):
    #constructor
    def __init__(self, name, health, power, coins, inventory=None):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        if (inventory is None):
            inventory=[]
        self.inventory = inventory

class Goblin(Character):
    #constructor
    def __init__(self, name, health, power, coins, inventory=None):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        if (inventory is None):
            inventory=[]
        self.inventory = inventory

class Dark_Night(Character):
    #constructor
    def __init__(self, name, health, power, coins, inventory=None):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        if (inventory is None):
            inventory=[]
        self.inventory = inventory