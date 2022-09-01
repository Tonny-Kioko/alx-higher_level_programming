#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matr = []
    for x in matrix:
        matr.append(list(map(lambda x: x**2, x)))
    return (matr)
