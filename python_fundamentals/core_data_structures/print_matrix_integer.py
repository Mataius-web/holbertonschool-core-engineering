#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in range(0, len(row)):
            if element == len(row) - 1:
                print("{}".format(row[element]))
            else:
                print("{}".format(row[element]), end=" ")
