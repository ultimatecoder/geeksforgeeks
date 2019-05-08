#! /usr/bin/env python

import unittest

from searching import count_the_zeros


class TestCountTheZeros(unittest.TestCase):

    def test_count_zeros(self):
        elements_and_expected_output = (
            ([1], 0),
            ([0], 1),
            ([1, 1, 0], 1),
            ([0, 0, 0], 3),
            ([1, 1, 1], 0),
            ([1, 1, 1, 0, 0], 2)
        )

        for elements, expected_count_of_zero in elements_and_expected_output:
            with self.subTest(
                elements=elements, output=expected_count_of_zero
            ):
                self.assertEqual(
                    count_the_zeros.count_zeros(elements),
                    expected_count_of_zero
                )
