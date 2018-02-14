class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        if(self.health >= 0):
            return True

    def attack(self,enemy):
        enemy.health -= self.power
        print(self,"do {} damage to the".format(self.power),enemy)

    def print_status(self):
        print(self.__str__(),"has {} health and {} power.".format(self.health, self.power))

class Hero(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power

class Goblin(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power

def main():
    hero = Hero(10,5)
    goblin = Goblin(6,2)

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            if(goblin.health <= 0):
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
            if hero.health <= 0:
                print("You are dead.")

main()