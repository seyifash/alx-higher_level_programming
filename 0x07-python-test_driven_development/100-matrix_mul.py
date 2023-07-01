#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """A function that multiplies 2 matrices

    Args:
    m_a(int, float): the first matrix
    m_b(int, float): the second matrix

    Raises:
    TypeError: if m_a doesnt contain a list or it is not an int or float
    TypeError: if m_b doesnt conatin a list or it is not an int or float
    ValuError: if m_a or m_b is empty
    TypeError: if m_b or m_a does not have the same row size
    ValueError: if m_a and m_b cant be multiplied
    Returns:
    resulting matrix after multiplication
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_a == [[]]:
        raise ValueError("m_b can't be empty")
    if not all((isinstance(element, int) or isinstance(element, float))
            for element in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element, int) or isinstance(element, float))
            for element in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
         raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_a[0]) for row in m_b):
         raise TypeError("each row of m_b must should be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")


