#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calcc
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, calcc.add(a, b)))
    print("{} - {} = {}".format(a, b, calcc.sub(a, b)))
    print("{} * {} = {}".format(a, b, calcc.mul(a, b)))
    print("{} / {} = {}".format(a, b, calcc.div(a, b)))
