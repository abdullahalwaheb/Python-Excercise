numbers = list(range(1,101))

for i in range(1,101):
    if (i%3 == 0) and (i%5==0):
        numbers.insert(i,"FizzBuzz")
        numbers.remove(i)
    elif (i%3)==0:
        numbers.insert(i,"Fizz")
        numbers.remove(i)
    elif (i%5)==0:
        numbers.insert(i,"Buzz")
        numbers.remove(i)

print(numbers)