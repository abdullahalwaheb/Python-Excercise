import pickle

phoneBookDictionary = {}

#look up an entry1
def findEntry():
    name = input("Enter a name to find: ")
    for name,phone in phoneBookDictionary.items():
        print(phoneBookDictionary.get(name))

#add/set an entry method
def setEntry():
    entryName = input("Enter name: ")
    entryPhoneNum = input("Phone Number: ")
    entryEmail = input("Enter Email: ")
    entryWebsite = input("Enter Website: ")
    phoneBookDictionary[entryName] = entryPhoneNum, entryEmail, entryWebsite
    print("--Entry stored for {}--".format(entryName))

#delete an entry
def delEntry():
    print("\nAvailable Contacts to erase: \n===============================")
    for key in phoneBookDictionary:
        print(key)
    name = input("\nEnter a name to erase:")
    del phoneBookDictionary[name]

#display all entries
def findAll():
    print("\nAvailable Contacts in memory: \n===============================")
    for key, value in phoneBookDictionary.items():
        print(key,": {}".format(value))

#update contacts in phonebooks
def updatePhoneBook():
    fileHandler = open('phonebook.pickle', 'wb')
    pickle.dump(phoneBookDictionary, fileHandler)
    fileHandler.close()
    print("\nPhonebook updated!\n")

#retrieve data from the pickle file
def retrievePhoneBook():
    fileHandler = open('phonebook.pickle', 'rb')
    phoneBookDictionary = pickle.load(fileHandler)
    print("\nRetrieved! from previous phonebook")
    print(phoneBookDictionary)
    fileHandler.close()
    
def run():
    while True:
        print("\nElectronic Phone Book\n===============================")
        print("1. Look up an entry\n"
            "2. Set an entry\n"
            "3. Delete an entry\n"
            "4. List all entries\n"
            "5. Update Phonebook (Save entries)\n"
            "6. Retrieve Phonebook (Load entries)\n"
            "7. Quit\n")
        try:
            choice = int(input(" "))
            if choice == 1:
                findEntry()
            elif choice == 2:
                setEntry()
            elif choice == 3:
                delEntry()
            elif choice == 4:
                findAll()
            elif choice == 5:
                updatePhoneBook()
            elif choice == 6:
                retrievePhoneBook()
            elif choice == 7:
                break
                quit()
        except:
            print("Invalid selection")


def main():
    retrievePhoneBook() #retrieve contacts on start-up
    run()


if __name__ == "__main__":
    main()
