#!/usr/bin/python3
import sys
import add_0 as an
if __name__ == "__main__":
    a = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    b = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    result = an.add(a, b)
    print(f'{a}+ {b} = {result}')
