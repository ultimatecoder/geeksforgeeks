import unittest

from mathematical.gcd_of_more_than_two_numbers import (
    find_greatest_common_divisor,
    calculate_greatest_common_divisor_of_two_numbers
)


class TestGCD(unittest.TestCase):

    def test_find_greatest_common_divisor(self):
        sample_numbers_and_expected_answers = (
            ([1, 2, 1, 1, 1], 1,),
            ([1], 1),
            ([], None),
            ([2, 4, 6, 8, 16], 2),
            ([1, 2, 3], 1),
            ([2, 4, 6, 8], 2),
            ([2], 2),
            ([10, 1, 2], 1),
        )
        for numbers, expected_answer in sample_numbers_and_expected_answers:
            self.assertEqual(
                find_greatest_common_divisor(numbers), expected_answer
            )

    def test_calculate_greatest_common_divisor_of_two_numbers(self):
        sample_numbers_and_expected_answers = (
            (1, 2, 1,),
            (1, 1, 1),
            (2, 4, 2),
            (1, 2, 1),
            (6, 8, 2),
            (10, 1, 1),
        )
        for number_1, number_2, expected_answer in (
            sample_numbers_and_expected_answers
        ):
            self.assertEqual(
                calculate_greatest_common_divisor_of_two_numbers(
                    number_1, number_2
                ), expected_answer
            )
