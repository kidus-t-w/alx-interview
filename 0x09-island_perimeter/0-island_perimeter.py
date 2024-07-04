#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculates perimeter of the island described in grid
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
    Return:
        returns the perimeter of the island
    """

    v = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    v += 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    v += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    v += 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    v += 1
    return v
