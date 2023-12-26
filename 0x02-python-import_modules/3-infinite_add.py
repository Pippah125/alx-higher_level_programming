#!/usr/bin/python3
import sys

if __name__ == '__main__':
    length = len(sys.argv)
    total = 0
    if length > 1:
        for a in range(1, length):
            total = total + int(sys.argv[a])

    print(total)
