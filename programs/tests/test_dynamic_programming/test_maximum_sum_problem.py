#! /usr/bin/env python

import unittest

from dynamic_programming import maximum_sum_problem


class TestMaximumSumProblem(unittest.TestCase):

    def test_calculate_maximum_sum(self):
        sample_numbers_and_expected_answers = (
            (1, 1),
            (100000, 203708),
            (12, 13),
            (24, 27)
        )

        for number, expected_answer in sample_numbers_and_expected_answers:
            with self.subTest(number=number, expected_answer=expected_answer):
                self.assertEqual(
                    maximum_sum_problem.calculate_maximum_sum(number),
                    expected_answer
                )
