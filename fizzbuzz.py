for i in range(0,100):
    if i == 0:
        null = 0
    elif (i % 3 == 0 and i % 5 == 0):
        print(str(i) + " fizzbuzz")
    elif i % 3 == 0:
        print(str(i) + " fizz")
    elif i % 5 == 0:
        print(str(i) + " buzz")
    else:
        print(i)