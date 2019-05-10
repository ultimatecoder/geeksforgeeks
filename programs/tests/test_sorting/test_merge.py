#! /usr/bin/env python

import unittest

from sorting import merge


class TestMergeSort(unittest.TestCase):

    def test_merge_sort(self):
        sample_inputs = (
            [-1, 0, 1, -3, -32],
            [2, 11, 23, 0.2, 23, 12],
            [1],
            [0],
            [-1, -1, -1, -1],
            [0.23, 0.111, 0.1, 0.001, 0.3],
            ["focus", "on", "challenges", "in", "implementing"]
        )
        for sample_input in sample_inputs:
            with self.subTest(sample_input=sample_input):
                expected_output = sample_input[:]
                merge.merge_sort(sample_input)
                self.assertListEqual(sample_input, sorted(expected_output))
