#!/usr/bin/python3
"""
2D matrix rotation.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix clockwise by 90 degrees.

    Args:
        matrix (List[List[int]]): The input
                2D matrix to be rotated.

    Returns:
        None: If the input matrix is not a list or
                if it is an empty list.
        None: If any of the elements in the input
                matrix is not a list.
        None: If the number of columns in each row
                of the input matrix is not the same.

    Raises:
        None

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> rotate_2d_matrix(matrix)
        >>> print(matrix)
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    rows = len(matrix)
    cols = len(matrix[0])
    if not all(map(lambda x: len(x) == cols, matrix)):
        return
    c, r = 0, rows - 1
    for i in range(cols * rows):
        if i % rows == 0:
            matrix.append([])
        if r == -1:
            r = rows - 1
            c += 1
        matrix[-1].append(matrix[r][c])
        if c == cols - 1 and r >= -1:
            matrix.pop(r)
        r -= 1
