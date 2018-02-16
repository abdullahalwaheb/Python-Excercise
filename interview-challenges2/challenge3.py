# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

result = []

for i in range (1,2521):
    for k in range(1,11):
        if (i % k == 0):
            result.append(k)
    else:
        pass

print(result)
