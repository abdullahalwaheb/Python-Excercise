class Person:
    def __init__(self, name, email, phone, friends=None, greetingCount=0):
        self.name = name
        self.email = email
        self.phone = phone
        if friends is None:
            friends = []
        self.friends = friends
        self.greetingCount = greetingCount

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greetingCount += 1

    def printContactInfo(self):
        print("email:", self.email, "phone:", self.phone)

    def addFriend(self, friend):
        self.friends.append(friend)

    def numOfFriends(self):
        print(self.name, "has" ,len(self.friends), "friend(s)")

    def __str__(self):
        return "Person: {} {} {}".format(self.name, self.email, self.phone)

def main():
    #creating objects with data
    sonny = Person("Sonny","sonny@gmail.com","483-485-4948")
    jordan = Person("Jordan","jordan@gmail.com","495-586-3456")
    #call greet methods passing objects
    sonny.greet(jordan)
    sonny.greet(jordan) #second greeting for testing
    jordan.greet(sonny)
    #call print contact methods
    sonny.printContactInfo()
    jordan.printContactInfo()
    #storing data into objects attributes
    jordan.addFriend(sonny)
    sonny.addFriend(jordan)
    #number of friends per person/object
    jordan.numOfFriends()
    sonny.numOfFriends()
    #greeting times
    print("Greeting count for {}:".format(sonny.name), sonny.greetingCount)
    print("Greeting count for {}:".format(jordan.name), jordan.greetingCount)
    #overriding __str__
    print(jordan.__str__())
    print(sonny.__str__())

if __name__ == "__main__":
    main()