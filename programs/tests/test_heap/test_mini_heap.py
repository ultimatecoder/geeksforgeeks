#! /usr/bin/env python

import unittest

from heap import mini_heap


class TestMinHeap(unittest.TestCase):

    def setUp(self):
        self.min_heap = mini_heap.MinHeap()

    def test_min_heap_operations_works_as_expected(self):
        number_1 = 4
        self.min_heap.insert(number_1)
        self.assertEqual(self.min_heap.pop(), number_1)

        numbers = [20, 2, 1, -1, 3, 5]
        expected_numbers = sorted(numbers)

        for number in numbers:
            self.min_heap.insert(number)

        for expected_number in expected_numbers:
            with self.subTest(number=expected_number):
                self.assertEqual(self.min_heap.pop(), expected_number)

    def test_pop_raises_error_when_no_elements_in_list(self):
        with self.assertRaises(IndexError):
            self.min_heap.pop()

        number = 3
        self.min_heap.insert(number)
        self.min_heap.pop()

        with self.assertRaises(IndexError):
            self.min_heap.pop()
