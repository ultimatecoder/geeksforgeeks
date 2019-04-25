#! /usr/bin/env python

import unittest

from arrays import maximum_in_struct_array


class TestMaximumInStructArray(unittest.TestCase):

    def test_validate_for_invalid_values(self):
        def _validate(value):
            return ((value >= 100) and (value <= 200))

        values_and_callables = (
            ("Y", lambda c: len(c) > 2),
            (2333, lambda w: (w >= 1) and (w <= 100)),
            (400, _validate)
        )
        for value, _callable in values_and_callables:
            with self.subTest(value=value, callable=_callable):
                with self.assertRaises(ValueError):
                    maximum_in_struct_array.validate(value, _callable)

    def test_validate_for_correct_values(self):
        def _validate(value):
            return ((value >= 1) and (value <= 100))

        values_and_callables = (
            ("Y", lambda c: len(c) == 1),
            (234, lambda n: (n >= 0) and (n <= 300)),
            (20, _validate)
        )

        for value, _callable in values_and_callables:
            with self.subTest(value=value, callable=_callable):
                maximum_in_struct_array.validate(value, _callable)

    def test_inches(self):
        values_and_expected_return_values = (
            (2, 24),
            (23.3, 279.6),
            (-12.3, -147.60000000000002)
        )
        for value, expected_return_value in values_and_expected_return_values:
            with self.subTest(value=value, return_value=expected_return_value):
                self.assertEqual(
                    maximum_in_struct_array.inches(value),
                    expected_return_value
                )

    def test_parse_feets_and_inches(self):
        values_and_expected_return_values = (
            ([1, 2, 2, 1], [(1, 2), (2, 1)]),
            ([3, 5, 7, 9, 5, 6, 5, 5], [(3, 5), (7, 9), (5, 6), (5, 5)])
        )
        for value, expected_return_value in values_and_expected_return_values:
            with self.subTest(value=value, return_value=expected_return_value):
                self.assertListEqual(
                    maximum_in_struct_array.parse_feets_and_inches(value),
                    expected_return_value
                )
