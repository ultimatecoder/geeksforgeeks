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

#def get_empty_cells(board):
#    rows = len(board)
#    columns = len(board[0])
#    row_index = 0
#    column_index = 0
#
#    for row_index, row in enumerate(board):
#        for column_index, cell in enumerate(row):
#            if cell is None:
#                yield (row_index, column_index)
#
#
#def backtrack(board, number_of_ways_counter=0):
#
#    for row_index, column_index in get_empty_cells(board):
#        for knight in ['b', 'w']:
#            board[row_index][column_index] = knight
#            number_of_ways_counter += 1
#            backtrack(board, number_of_ways_counter)
#    return number_of_ways_counter

def backtrack(board, row_index=0, column_index=0):

    if (row_index == len(board)):
        return
    else:
        for knight in ['b', 'w']:
            board[row_index][column_index] = knight
            print(board)
            if (column_index < (len(board[0]) - 1)):
                backtrack(board, row_index, column_index+1)
            else:
                backtrack(board, row_index+1, column_index=0)
        board[row_index][column_index] = None


if __name__ == "__main__":
    board = [
        [None, None],
        [None, None]
    ]
    #number_of_ways = backtrack(board)
    #print(number_of_ways)
    backtrack(board)
