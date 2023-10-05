#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        i = 0
        for thing in sys.argv:
            if i != 0:
                print("{}: {}".format(i, thing))
            i += 1
