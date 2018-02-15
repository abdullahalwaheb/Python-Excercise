#each item with its value
itemsDict = {
    "Armor" : 3,
    "SuperTonic" : 2,
    "Shuriken" : 5,
    "Evade" : 2,
    "Sacrifice" : 2
    }

def listItems():
    number = 1
    print("")
    print("  🛡️  Blacksmith Store 🛡️")
    print("===========================")
    for key,value in itemsDict.items():
        print("{}. {} for {} coins".format(number, key, value))
        number+= 1
    print("6. Skip")
    print("")
    print("Buy an item from the list or press any key to pass")
    print(">>")