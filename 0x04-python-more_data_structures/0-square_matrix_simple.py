#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_copy = [row[:] for row in matrix]
    matrix_rows = len(matrix)
    matrix_columns = max(len(row) for row in matrix) if matrix else 0
    new_matrix = [[0] * matrix_columns for _ in range(matrix_rows)]

    # Apply the lambda functions to each element in the matrix
    for i in range(matrix_rows):
        for j in range(matrix_columns):
            new_matrix[i][j] = (lambda x: x ** 2)(matrix_copy[i][j])

    return new_matrix


