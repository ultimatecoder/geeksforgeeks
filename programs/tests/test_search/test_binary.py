#! /usr/bin/env python

import unittest

from searching import binary


class TestBinarySearch(unittest.TestCase):

    def test_binary_search_with_various_cases(self):
        sample_elements_and_element = (
            ([1, 3, 4, 13, 100], 100),
            ([-3, -2, -1], -1),
            (["aa", "bb", "cc", "dd", "ee"], "cc"),
            (["A"], "A"),
            ([1, 2, 3, 4, 5], 2)
        )
        for elements, element in sample_elements_and_element:
            with self.subTest(elements=elements, element=element):
                index = binary.binary_search(elements, element)
                expected_index = elements.index(element)
                self.assertEqual(
                    index,
                    expected_index,
                    (f"Computed {index} for element {element} is not equal"
                     f"to expected index {expected_index}")
                )
