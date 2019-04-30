#! /usr/bin/env python
import unittest

from queue import queue_operations


class TestQueueOperations(unittest.TestCase):

    def test_validate_elements_with_correct_input(self):
        elements = [1, 2, 3, 4, 5]
        queue_operations.validate_elements(
            elements, lambda n: (n >= 1) and (n <= 10)
        )

    def test_validate_elements_with_wrong_values(self):
        elements = [100, 12, 1000, 2]

        with self.assertRaises(ValueError):
            queue_operations.validate_elements(
                elements, lambda n: (n >= 10) and (n <= 100)
            )
