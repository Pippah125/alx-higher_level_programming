#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ""
    for a in range(len(str)):
        if a == n:
            continue
        new_string = new_string + str[a]
    return (new_string)
