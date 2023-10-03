#!/usr/bin/python3
def print_last_digit(number):
    digit = 10 - (number % 10) if number < 0 else number % 10
    print("{}".format(digit), end="")
    return (digit)
