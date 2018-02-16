# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#variables
result = []
num = 1
denominator = 1

#algorithm
while True:  
    if (num % denominator == 0):
        #does not matter what number to append, this is just to fill the length up to 20
        result.append("0")
        denominator += 1
    elif (num % denominator != 0):
        result = []
        num += 1
        denominator = 1
    if (len(result) == 20):
        break

#The number should be 232792560
print(num)

#validate the result
for i in range(1,21):
    print(num%i)