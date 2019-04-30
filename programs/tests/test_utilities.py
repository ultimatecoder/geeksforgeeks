#! /usr/bin/env python
import unittest

import utilities

class TestValidation(unittest.TestCase):

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
                    utilities.validate(value, _callable)

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
                utilities.validate(value, _callable)
