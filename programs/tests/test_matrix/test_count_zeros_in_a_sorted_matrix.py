#! /usr/bin/env python

import unittest

from matrix import count_zeros_in_a_sorted_matrix


class TestCountZerosInASortedMatrix(unittest.TestCase):

    def test_convert_to_matrix(self):
        sample_elements = (
            ([0, 0, 1, 1], 2, 2, [[0, 0], [1, 1]]),
            ([0, 1, 1, 0, 1, 1, 0, 1, 1], 3, 3, [
                [0, 1, 1], [0, 1, 1], [0, 1, 1]
            ])
        )
        for elements, columns, rows, expected_matrix in sample_elements:
            with self.subTest(
                elements=elements,
                columns=columns,
                rows=rows,
                expected_matrix=expected_matrix
            ):
                self.assertListEqual(
                    count_zeros_in_a_sorted_matrix.convert_to_matrix(
                        elements, columns, rows
                    ),
                    expected_matrix
                )

    def test_count_zeros(self):
        sample_matrix = (
            ([[0, 0], [1, 1]], 2),
            ([[1, 1], [1, 1]], 0),
            ([[0, 0], [0, 0]], 4),
            ([[0, 0, 1], [0, 1, 1], [1, 1, 1]], 3),
            ([[0], [1]], 1)
        )

        for matrix, expected_output in sample_matrix:
            with self.subTest(matrix=matrix, expected_output=expected_output):
                self.assertEqual(
                    count_zeros_in_a_sorted_matrix.count_zeros(matrix),
                    expected_output
                )
