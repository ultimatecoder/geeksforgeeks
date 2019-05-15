#! /usr/bin/env python
"""
Problem

    How many ways are there to place a black and white knight on a N * M
    chessboard such that they do not attack each other? The kights have to be
    placed on different squares. A knight can move two squares horizontally and
    one square vertically (L shaped), or two squares vertically and one square
    horizontally (L shaped). The knights attack each other if one can reach the
    other in one move.

Input

    The first line contains the number of test cases T. Each of the next T
    lines contains two integers N and M which is size of Matrix.

Output

    For each testcase, print the required answer, i.e., number of possible ways
    to place knights.

Constraints

    * 1 <= T <= 100
    * 1 <= N, M <= 10^5

Example

    Input

        3
        2 2
        2 3
        4 5

    Output

        12
        26
        312
"""
import utilities


def _get_empty_cells(
    board, row_index_of_knight=None, column_index_of_knight=None
):
    """Gives empty cell with current situation of the board.

    If the knight is present on board, then this method will avoid returning
    positions in which existing knight can attack. If no positions were given
    than this method assumes that there is no knight present on the board.

    Arguments:
        * row_index_of_knight: Row index of existing knight on board
        * column_index_of_knight: Column index of existing knight on board

    Raises
        'StopIteration' when there are not cell left
    """
    total_rows = len(board)
    total_columns = len(board[0])

    row_index = 0
    column_index = 0

    if (
        (row_index_of_knight is not None) and
        (column_index_of_knight is not None)
    ):
        attack_sensitive_cells = list(_get_possible_moves_of_knight(
            board, row_index_of_knight, column_index_of_knight
        ))
    else:
        attack_sensitive_cells = []

    while row_index < total_rows:
        while column_index < total_columns:
            if (
                (board[row_index][column_index] is None) and
                ((row_index, column_index) not in attack_sensitive_cells)
            ):
                yield (row_index, column_index)
            column_index += 1
        column_index = 0
        row_index += 1


def _get_possible_moves_of_knight(
    board, row_index_of_knight, column_index_of_knight
):
    total_rows = len(board)
    total_columns = len(board[0])
    # (Column, Row)
    differences = (
        (-2, +1),  # Left side down
        (-2, -1),  # Left side up
        (+2, +1),  # Right side down
        (+2, -1),  # Right side up
        (-1, -2),  # Up side left
        (+1, -2),  # Up side right
        (-1, +2),  # Down side left
        (+1, +2),  # Down side right
    )
    for row_difference, column_difference in differences:
        row_index = row_index_of_knight - row_difference
        column_index = column_index_of_knight - column_difference
        if (
            ((row_index >= 0) and (row_index < total_rows)) and
            ((column_index >= 0) and (column_index < total_columns))
        ):
            yield (row_index, column_index)


def construct_board(number_of_rows, number_of_columns):
    """Constructs an empty Chess board in the form of Matrix."""
    board = []
    row_index = 0
    column_index = 0
    while row_index < number_of_rows:
        board.append([])
        while column_index < number_of_columns:
            board[row_index].append(None)
            column_index += 1
        column_index = 0
        row_index += 1
    return board


def calculate_ways(board):
    """Calculate ways for two different colored knights on a board

    This method calculates the possible ways to place a two different colored
    knights on a board in which both do not attack each other.

    Arguments:
        * board: The board is a Matrix of rows * columns. It represents an
                 empty chess board.

    Returns:
        Counted ways in which both knights can be placed on a given chess board
        without attacking each other.
    """
    number_of_ways_counter = 0

    for row_index, column_index in _get_empty_cells(board):
        board[row_index][column_index] = 'b'
        for _row_index, _column_index in _get_empty_cells(
            board, row_index, column_index
        ):
            board[_row_index][_column_index] = 'w'
            number_of_ways_counter += 1
            board[_row_index][_column_index] = None
        board[row_index][column_index] = None

    return number_of_ways_counter


if __name__ == "__main__":
    number_of_test_cases = int(input(''))
    utilities.validate(
        number_of_test_cases, lambda t: (t >= 1) and (t <= 100)
    )
    for _ in range(number_of_test_cases):
        number_of_rows, number_of_columns = input('').split(' ')
        number_of_rows = int(number_of_rows)
        utilities.validate(
            number_of_rows, lambda r: (r >= 1) and (r <= 10**5)
        )
        number_of_columns = int(number_of_columns)
        utilities.validate(
            number_of_columns, lambda c: (c >= 1) and (c <= 10**5)
        )
        board = construct_board(number_of_rows, number_of_columns)
        print(calculate_ways(board))
