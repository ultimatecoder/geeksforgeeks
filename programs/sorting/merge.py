#! /usr/bin/env python
"""Implements Merge sort algorithm.

Reference: Introduction to Algorithm Chapter 2.3 (Designing algirithmms)
"""

import math


def _merge_sequences(elements, start_index, middle_index, end_index):
    """Merges elements1 with elements 2.

    Arguments:
        * elements: Sequence of elements
        * start_index : Index value from where elements will be sorted
        * middle_index: Index value from which the elements will be divided
                        into half.
        * end_index : Index value util elements will be sorted
    """
    preference = None
    left = elements[start_index: middle_index+1]
    left_index = 0

    right = elements[middle_index+1: end_index+1]
    right_index = 0

    for index in range(start_index, end_index+1):
        if (preference == 'left') or (
            left_index < len(left) and (left[left_index] <= right[right_index])
        ):
            elements[index] = left[left_index]
            left_index += 1
            if (left_index == len(left)):
                preference = 'right'
        else:
            elements[index] = right[right_index]
            right_index += 1
            if (right_index == len(right)):
                preference = 'left'


def _sort(elements, left_index, right_index):
    if left_index < right_index:
        middle_index = (left_index + right_index) // 2
        _sort(elements, left_index=left_index, right_index=middle_index)
        _sort(
            elements, left_index=middle_index + 1, right_index=right_index
        )
        _merge_sequences(elements, left_index, middle_index, right_index)


def merge_sort(elements):
    """Sorts the given elements using Merge sort"""
    _sort(elements, 0, len(elements) - 1)
