#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz", end=", " if i < 99 else "\n")
            else:
                print("Fizz", end=", ")
        elif i % 5 == 0:
            if i % 3 == 0:
                print("FizzBuzz", end=", " if i < 99 else "\n")
            else:
                print("Buzz", end=", ")
        else:
            print("{:d}".format(i), end=", " if i < 99 else "\n")
