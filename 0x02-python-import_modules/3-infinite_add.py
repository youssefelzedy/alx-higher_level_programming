#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sm = 0
    i = 0
    for thing in sys.argv:
        if i != 0:
            sm += int(thing)
        i += 1
    print("{}".format(sm))
