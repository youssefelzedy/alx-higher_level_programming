#!/usr/bin/python3
import random
number = -98
num = number % 10
if number < 0:
    num *= -1
if num == 0:
    print("Last digit of", number, "is", num, end=" ")
    print("and is 0")
if number > 0:
    print("Last digit of", number, "is", end=" ")
    if num > 5:
        print(f"{num} and is greater than 5")
    else:
        print(f"{num} and is less than 6 and not 0")
elif num < 0:
    print("Last digit of ", number, " is ", num, end=" ", sep="")
    print("and is less than 6 and not 0")
