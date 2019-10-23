
i=1
while i<=100:
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    i += 1

# II sposob


for x in range(1,101):
    if x % 3 != 0 and x % 5 != 0:
        print(x)
    elif x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")




