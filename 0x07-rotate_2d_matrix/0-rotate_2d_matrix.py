#!/usr/bin/python3
'''
    rotate_2d_matrix function that rotates a n x n matrix 90 degrees.
'''


def rotate_2d_matrix(matrix):
    '''
        rotate_2d_matrix: function
        @matrix: Matrix to rotate.
        return: None
    '''
    new_matrix = []
    for x in range(len(matrix)):
        new_line = []
        for y in range(len(matrix)):
            new_line.append(matrix[y][x])
        new_line.reverse()
        new_matrix.append(new_line)
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            matrix[x][y] = new_matrix[x][y]
