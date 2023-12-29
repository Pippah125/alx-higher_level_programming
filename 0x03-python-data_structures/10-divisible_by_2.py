#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiples = []
    for elements in range(len(my_list)):
        if elements % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)
    return multiples
