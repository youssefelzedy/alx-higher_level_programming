#!/usr/bin/python3
"""2-matrix_divided module"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.
    Args:
        matrix (list): A list of lists of integers or floats.
        div (int or float): The divisor.
    Returns:
        list: A new matrix with the result of the division.
    """
    if not isinstance(div, (float, int)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    length = len(matrix[0])
    new_matrix = []
    for row in matrix:
        rows = []
        if len(row) != length:
            raise TypeError('Each row of the matrix must have the same size')
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for elem in row:
            if not isinstance(elem, (float, int)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
            rows.append(round(elem / div, 2))
        new_matrix.append(rows)
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
