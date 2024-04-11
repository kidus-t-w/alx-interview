#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function called `pascal_triangle(n)` that
      returns a list containing n lists of integers,
      representing the rows of Pascal's triangle up to the nth row.
    """
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle
