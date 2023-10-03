#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = str(number)
print("Last digit of", number, "is", str[-1:], "and is", end=" ")
if int(str[-1:]) > 5:
    print("greater than 5")
elif int(str[-1:]) < 6 and int(str[-1:]) != 0:
    print("less than 6 and not 0")
else:
    print("0")
