#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
newList = []
oldlist = list(range(1,61))

for i in range(1,61):
    newList.append( oldlist[i] )
 

print(newList)