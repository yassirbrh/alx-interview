#!/usr/bin/python3
'''
    Function island_perimeter that returns the perimeter of the island
    described in grid.
'''


def island_perimeter(grid):
    '''
        island_perimeter: function
        @grid: 2D Matrix representing the island.
        return: the perimeter of the island.
    '''
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i - 1 >= 0 and grid[i - 1][j] == 0:
                    perimeter += 1
                if i + 1 < len(grid) and grid[i + 1][j] == 0:
                    perimeter += 1
                if j - 1 >= 0 and grid[i][j - 1] == 0:
                    perimeter += 1
                if j + 1 < len(grid[i]) and grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
