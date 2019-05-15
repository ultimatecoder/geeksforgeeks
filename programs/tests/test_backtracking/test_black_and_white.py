#! /usr/bin/env python

import unittest

from backtracking import black_and_white


class TestBlackAndWhite(unittest.TestCase):

    def test_backtrack(self):
        sample_combinations = (
            # board, expected count
            ([[None, None], [None, None]], 12),
            ([[None, None, None], [None, None, None]], 26),
            ([
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None]
            ], 312)
        )
        for board, expected_counts in sample_combinations:
            with self.subTest(board=board, expected_count=expected_counts):
                self.assertEqual(
                    black_and_white.calculate_ways(board),
                    expected_counts
                )

    def test_construct_board(self):
        sample_combinations = (
            # Number of Rows, Number of Columns
            ((2, 2), [[None, None], [None, None]]),
            ((2, 3), [[None, None, None], [None, None, None]]),
            ((4, 5), [
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None]
            ])
        )
        for board_dimensions, expected_board in sample_combinations:
            number_of_rows, number_of_columns = board_dimensions
            with self.subTest(
                number_of_rows=number_of_rows,
                number_of_columns=number_of_columns
            ):
                self.assertListEqual(
                    black_and_white.construct_board(
                        number_of_rows, number_of_columns
                    ),
                    expected_board
                )
