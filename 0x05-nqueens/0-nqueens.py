#!/usr/bin/python3
""" N queens """
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, i=0, a=[], b=[], c=[]):
    """
    Find possible positions for N queens on an nxn chessboard.

    Args:
        n (int): The size of the chessboard.
        i (int, optional): The current row being filled. Defaults to 0.
        a (list, optional): The current column positions of the queens.
        b (list, optional): The current diagonals formed by the queen.
        c (list, optional): The current diagonals formed by the queen.
    Yields:
        list: A list of column positions for the queens in the current row.
    """
    # Base case: all queens have been placed
    if i < n:
        for j in range(n):
            # Check if the queen can be placed in the current column
            if j not in a and i + j not in b and i - j not in c:
                # Recursively find possible positions for the next row
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        # Return the current row of queen positions
        yield a


def solve(n):
    """
    Solve the N-queens problem by iterating through all possible solutions
    and printing each one.

    Args:
        n (int): The size of the chessboard.
    """
    # Initialize an empty list to hold the current solution
    k = []
    # Initialize an index to keep track of the current column
    i = 0
    # Iterate through all possible solutions
    for solution in queens(n, 0):
        # Iterate through the columns in the current solution
        for s in solution:
            # Add the current column and index to the current solution
            k.append([i, s])
            # Increment the index
            i += 1
        # Print the current solution
        print(k)
        # Reset the current solution and index
        k = []
        i = 0


solve(n)
