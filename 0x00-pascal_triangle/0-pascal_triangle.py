#!/usr/bin/python3
""" 0-pascal_triangle.py """


def pascal_triangle(n):
    """
    This function generates Pascal's triangle up to a given number of rows.

    Args:
        n: The number of rows in the Pascal's triangle.

    Returns:
        A list of lists representing the Pascal's triangle.
    """
    if n <= 0:
        return []
    result = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(result[i - 1][j - 1] + result[i - 1][j])
        row.append(1)
        result.append(row)
    return result
