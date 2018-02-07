#uncomment the block to use

# #-----------------1 to 10-----------------
# for i in range(1,11):
#     print(i)


# #-----------------n to m-----------------
# startNum = int(input("Starting from: "))
# endNum = int(input("Ending on: "))

# for i in range(startNum,endNum):
#     print(i)


# #-----------------odd numbers-----------------
# for i in range(1, 11):
#     if (i%2>0):
#         print(i)


# #-----------------Print a square-----------------
# #using two dims array
# n = int(input("How big the square is? "))
# #setting the size of the array
# squareArry = [[0] * n for i in range(n)] 
# #set col and row elements to *
# for row in range(n):
#     for col in range(n):
#         squareArry[row][col] = "*"
# #print
# for k in squareArry:
#     print(k)


# #-----------------Print a box-----------------
# width = int(input("Width? "))
# height = int(input("Height? "))

# print("*"*width)
# for i in range(height-1):
#     print("*"," "*(width-4),"*")
# print("*"*width)


# #-----------------Print a triangle-----------------
# height = int(input("Triangle Height? "))
# #tri 1
# for i in range(height+1):
#     print("*"*i)

# print("\n")
# #tri 2
# for k in range(height):
#     gaps = height - k - 1
#     strs = k * 2 + 1
#     print((' ' * gaps) + ('*' * strs))


# #------------Print a multiplication table------------
# for i in range(1,11):
#     result = 0
#     for j in range(1,11):
#         result = i*j
#         print(i," x ",j," = ",result)


# #-----------------Bonus: Print a banner-----------------
# text = input("Enter a text\n")
# print("*"*(len(text)+4))#4 is the num of generic spaces created
# print("*",text,"*")
# print("*"*(len(text)+4))