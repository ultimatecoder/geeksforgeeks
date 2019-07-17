#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from arrays import maximum_difference


class TestMaximumDifference(unittest.TestCase):

    def test_find_maximum_difference(self):
        numbers_and_expected_answers = (
            ([1, 2, 3, 4, 5], 4),
            ([10, 3, 0, -1, -22, 10], 32),
            ([2, 3, 10, 6, 4, 8, 1], 8),
            ([0, 0], -1),
            ([1], -1),
            ([-12, 1, 3], 15),
            ([7, 9, 5, 6, 3, 2], 2),
            ([4, 3, 2, 1], -1),
            ([-1, -2, -3, -4, -5], -1),
            ([0, -1, -2, -3, -4, -5], -1),
            ([-5, -3, -2], 3)
        )

        for numbers, expected_answer in numbers_and_expected_answers:
            with self.subTest(
                numbers=numbers, expected_answer=expected_answer
            ):
                self.assertEqual(
                    maximum_difference.find_maximum_difference(numbers),
                    expected_answer
                )
