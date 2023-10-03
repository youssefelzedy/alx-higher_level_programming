#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = str(number)
num = int(str[-1:])
if number < 0:
    num *= -1

if num > 5:
    if number < 0:
        print("Last digit of ", number, " is ", num, end=" ", sep="")
    else:
        print("Last digit of ", number, "is", num, end=" ")
    print("and is greater than 5")
elif num < 6 and num != 0:
    if number < 0:
        print("Last digit of ", number, " is ", num, end=" ", sep="")
    else:
        print("Last digit of", number, "is", num, end=" ")
    print("and is less than 6 and not 0")
else:
    print("Last digit of", number, "is", num, end=" ")
    print("and is 0")
