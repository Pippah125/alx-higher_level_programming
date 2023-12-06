#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) != 0:
        for item1 in range(len(matrix)):
            for item2 in range(len(matrix[item1])):
                print('{:d}'.format(matrix[item1][item2]), end="")
                if item2 != (len(matrix[item1]) - 1):
                    print(" ", end="")
            print("")
