#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for thing in dir(hidden_4):
        if thing[0] != "_" and thing[1] != "_":
            print("{}".format(thing))
