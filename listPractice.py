#declaring variables
myList = [-1,-2,-5,1,2,3,4,5,6]
newList = []

#Sum of numbers in a list
print("The sum of numbers in the list is: ", sum(myList))

#Largest number in a list
print("The largest number in the list is: ", max(myList))

#Smallest number in a list
print("The smallest number in the list is: ", min(myList))

#Even numbers in a list
print("The even numbers in this list are:")
for i in myList:
    if (i%2 == 0):
        print(i)

#Positive numbers in a list
print("The positive numbers in this list are:")
for i in myList:
    if (i > 0):
        print(i)

#Positive numbers2 in a new list
print("The positive numbers from list one to two are:")
for i in myList:
    if (i > 0):
        newList.append(i)
print(newList)

#more varialbes for multiplication --------------
list1 = [1,2,3]
list2 = [2,3,2]
vectorList = []
additionList = []


#multiplication of vector
print("The new multiplication list is:")
for k in range(0, len(list1)):
    vectorList.append(list1[k]*list2[k])
print(vectorList)

#addition of two lists
print("The addition list is:")
for k in range(0, len(list1)):
    additionList.append(list1[k]+list2[k])
print(additionList)