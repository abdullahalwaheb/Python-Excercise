numbers = list(range(1,20))

for i in numbers:
    if i%3==0:
        numbers.remove(i)
        numbers.insert(i,"Fizz")

print(numbers)