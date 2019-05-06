#! /usr/bin/env python

import unittest

from heap import mini_heap, nearly_sorted_algorithm


class TestNearlySortedAlgorithm(unittest.TestCase):

    def test_insert_elements_to_heap(self):
        min_heap = mini_heap.MinHeap()
        elements = range(5)
        nearly_sorted_algorithm.insert_elements_to_heap(min_heap, elements)

        for expected_element in elements:
            with self.subTest(element=expected_element):
                self.assertEqual(min_heap.pop(), expected_element)

    def test_sort_elements_specific_positions_away(self):
        input_elements_and_positions_away = (
            ([2, 1, 3], 3),
            ([2, 6, 3, 12, 56, 8], 3)
        )
        custom_sort = (
            nearly_sorted_algorithm.sort_elements_specific_positions_away
        )
        for elements, positions_away in input_elements_and_positions_away:
            with self.subTest(
                elements=elements, positions_away=positions_away
            ):
                result = sorted(elements)
                self.assertListEqual(
                    result, custom_sort(elements, positions_away)
                )
