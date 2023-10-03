#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = str(number)

if int(str[-1:]) > 5:
    if number < 0:
        print("Last digit of ", number, " is -", str[-1:], end=" ", sep="")
    else:
        print("Last digit of ", number, "is", str[-1:], end=" ")
    print("and is greater than 5")
elif int(str[-1:]) < 6 and int(str[-1:]) != 0:
    if number < 0:
        print("Last digit of ", number, " is -", str[-1:], end=" ", sep="")
    else:
        print("Last digit of", number, "is", str[-1:], end=" ")
    print("and is less than 6 and not 0")
else:
    print("Last digit of", number, "is", str[-1:], end=" ")
    print("and is 0")
