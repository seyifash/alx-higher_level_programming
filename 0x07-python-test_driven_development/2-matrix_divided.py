#!/usr/bin/python3
def matrix_divided(matrix, div):
    """A function that divides all elements of matrix

    Args:
    matrix(list): A list of lists and int
    div(int/float): the divisor
    Raises:
    TypeError: if the matrix is not a list matrix is empty
    TypeError: if the matrix contains rows of  different sizes
    TypeError: if the all element in the row is not an int or a float
    TypeError: If div is not an int or float.
    ZeroDivisionError: if div is 0

    Returns:
    Returns a matrix containing the product of dividing div by each element
    """

    if (not isinstance(matrix, list) or matrix == []
            or not all(isinstance(row, list)for row in matrix) or
            not all((type(element) in [int, float])
            for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
