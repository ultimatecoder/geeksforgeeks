#!/usr/bin/env python
"""
Problem

    Given a M x N binary Matrix A where each row and column of the matrix is
    sorted in ascending order, Your task is to find the count of number of 0s
    present in it.

Note

    Elements in Matrix can be either 1 or 0

Input

    The first line of input will be the no of test cases then T test cases will
    follow. The second line of each test case contains two space separated
    integers M, N denoting the size of the 2d Matrix. Then in the next lines
    are the space separated values of the matrix A [][].


Output

    The output will be the number of zeroes present in the square matrix.

Constraints

    1 <= T <= 50
    1 <= M, N <= 50
    0 <= A[][] <= 1

Example

    Input

        1
        3
        0 0 0 0 0 1 0 1 1

    Output

        6
"""
import utilities


def convert_to_matrix(elements, length_of_columns, length_of_rows):
    """Converts an M x N Matrix from given elements

    The method will convert given elements into a matrix of given colums and
    rows.

    Returns:
        A 2 dimensional Matrix constructed from given elements

    Example:
        >>>convert_to_matrix([0, 1, 1, 1], 2, 2) == [[0, 1], [1, 1]]
    """
    matrix = []
    index = 0
    for column in range(length_of_columns):
        for row in range(length_of_rows):
            try:
                matrix[column].append(elements[index])
            except IndexError:
                matrix.append([elements[index]])
            index += 1
    return matrix


def count_zeros(matrix):
    """Counts number of 0s in a given 2d Matrix

    Time complexity of this algorithm is O(rows+columns)

    Returns:
        An integer representing counting zeros (0) at given matrix.
    """
    zeros = 0
    end_rows = len(matrix) - 1
    end_columns = len(matrix[0]) - 1
    row = end_rows
    column = 0
    while (column <= end_columns) and (row >= 0):
        if (matrix[row][column] == 0):
            zeros += (row + 1)
            column += 1
        else:
            row -= 1
    return zeros


if __name__ == "__main__":
    number_of_test_cases =  int(input(''))
    utilities.validate(
        number_of_test_cases,
        lambda t: (t >= 1) and (t <= 50)
    )
    for _ in range(number_of_test_cases):
        length_of_columns_and_rows = input('').split(' ')
        length_of_columns = int(length_of_columns_and_rows[0])
        utilities.validate(
            length_of_columns,
            lambda c: (c >= 1) and (c <= 50)
        )

        length_of_rows = int(length_of_columns_and_rows[1])
        utilities.validate(
            length_of_rows,
            lambda r: (r >= 1) and (r <= 50)
        )
        elements = input('').split(' ')
        elements = list(map(int, elements))
        for element in elements:
            utilities.validate(element, lambda e: (e == 1) or (e == 0))
        matrix = convert_to_matrix(elements, length_of_columns, length_of_rows)
        print(count_zeros(matrix))
