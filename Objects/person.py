class Person:
    def __init__(self, name, email, phone, friends=None):
        self.name = name
        self.email = email
        self.phone = phone
        if friends is None:
            friends = []
        self.friends = friends

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def printContactInfo(self):
        print("email:", self.email, "phone:", self.phone)

def main():
    #creating objects with data
    sonny = Person("Sonny","sonny@gmail.com","483-485-4948")
    jordan = Person("Jordan","jordan@gmail.com","495-586-3456")
    #call greet methods passing objects
    sonny.greet(jordan)
    jordan.greet(sonny)
    #call print contact methods
    sonny.printContactInfo()
    jordan.printContactInfo()
    #storing data into objects attributes
    jordan.friends.append(sonny)
    sonny.friends.append(jordan)
    #number of friends per person
    print(len(sonny.friends))
    for i in sonny.friends:
       print(i)

if __name__ == "__main__":
    main()