#! /usr/bin/env python

def binary_search(elements, element):
    """Finds an index of the element using Binary search algorithm

    This method finds an index of the given element into collection of elements
    using Binary Search algorithm.

    This procedure do not deal with duplicate elements.

    Arguments:
        * elements : A collection of elements in which the given element will
                     be searched. The elements should be sorted in order.

        * element  : The value which will be searched at the collection of
                     elements.

    Returns:
        Index of given element in elements collection. Returns None if no index
        has found.
    """
    left = 0
    right = len(elements) - 1

    while (left <= right):
        middle = (left + right) // 2
        if elements[middle] < element:
            left = middle + 1
        elif elements[middle] > element:
            right = middle - 1
        else:
            return middle
    return None
