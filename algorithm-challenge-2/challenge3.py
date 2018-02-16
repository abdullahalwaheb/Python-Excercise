# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

result = []
num = 2515
i = 1

def repeat():
    while (num % i == 0):
        result.append(num)
        i+= 1
    else:
        result = []
        num += 1
        i = 1
        repeat()
        

if (len(result) == 10):
    result = []
    result.append(num)
else:
    print("the number is not found")

repeat()
print(num)
print(result)