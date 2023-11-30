#!/usr/bin/python3
import sys
import add_0
a = int(sys.argv[1]) if len(sys.argv) > 1 else 1
b = int(sys.argv[2]) if len(sys.argv) > 2 else 2
result = add_0.add(a, b)
string = f'{a}+ {b} = {result}'
print(string)
