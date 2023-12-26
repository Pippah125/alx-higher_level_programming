#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    index = len(sys.argv) - 1
    if index == 0:
        print("arguments")
    elif index == 1:
        print("argument = 1:")
    else:
        print("{} arguments:".format(index))
    for i in range(index):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
