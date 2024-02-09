#!/usr/bin/python3

import sys
""" Class for nqueens """


class nqueens:

    """ Initialisation of the class nqueens """
    board = []
    solutions = []
    probable_solution = []
    __size = None

    def __init__(self, size):
        """ Initialisation of the constructor of the class nqueens """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        self.__size = size
        for i in range(size):
            for j in range(size):
                self.board.append([i, j])

    def exclude_positions(self, board, x, y):
        """
            exclude positions depending on the position of the queen
        """
        i = y
        j = x
        for j in range(x, self.__size):
            if [j, y] in board:
                board.remove([j, y])
        for i in range(y, self.__size):
            if [x, i] in board:
                board.remove([x, i])
        j = x
        i = y
        for j in range(x, -1, -1):
            if [j, y] in board:
                board.remove([j, y])
        for i in range(y, -1, -1):
            if [x, i] in board:
                board.remove([x, i])
        y_position = 0
        j = x
        for j in range(x, self.__size):
            if [j, y + y_position] in board:
                board.remove([j, y + y_position])
            if [j, y - y_position] in board:
                board.remove([j, y - y_position])
            y_position += 1
        y_position = 0
        j = x
        for j in range(x, -1, -1):
            if [j, y + y_position] in board:
                board.remove([j, y + y_position])
            if [j, y - y_position] in board:
                board.remove([j, y - y_position])
            y_position += 1

    def search_solutions(self, board, y, x=0):
        """ search solutions """
        self.probable_solution.append([x, y])
        if len(self.probable_solution) == self.__size:
            self.solutions.append(self.probable_solution.copy())
        self.exclude_positions(board, x, y)
        x_position = x + 1
        new_board = []
        for elem in board:
            if elem[0] == x_position:
                new_board.append(elem)
        for elem in new_board:
            self.search_solutions(board.copy(), elem[1], elem[0])
            self.probable_solution.pop(-1)

    def launch(self):
        """ Initialisation of the launch method """
        for y in range(self.__size):
            working_board = self.board.copy()
            self.probable_solution = []
            self.search_solutions(working_board, y)

    def print_solutions(self):
        return self.solutions


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)
size = int(sys.argv[1])
if size < 4:
    print("N must be at least 4")
    exit(1)
new_nqueens = nqueens(size)
new_nqueens.launch()
solutions = new_nqueens.print_solutions()
for solution in solutions:
    print(solution)
