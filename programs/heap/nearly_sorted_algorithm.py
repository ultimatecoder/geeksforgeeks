#! /usr/bin/env python

"""
Problem

    Given an array of n elements, where each element is at most K away from its
    target position. The task is to print array in sorted form.

Input

    First line consists of T test cases. First line of every test case consists
    of two integers N and K, denoting number of elements in array and at most K
    position away from its target position respectively. Second line of every
    test case consists of elements of array.

Output

    Single line output to print the sorted array.

Constraints

    1 <= T <= 100
    1 <= N <= 100
    1 <= K <= N

Example

    Input

        2
        3 3
        2 1 3
        6 3
        2 6 3 12 56 8

    Output

        1 2 3
        2 3 6 8 12 56
"""
import utilities
from heap import mini_heap


def insert_elements_to_heap(heap, elements):
    """Inserts given elements to the heap

    Arguments:
        * heap     : An instance of 'heap.MinHeap'
        * elements : collection of elements

    Return:
        None
    """
    for element in elements:
        heap.insert(element)


def sort_elements_specific_positions_away(elements, positions_away):
    """Sort elements specific positions away

    Arguments:
        * elements       : Sequence of elements (unsorted)
        * positions_away : Value where expected element is this much position
                           away for consider it as a sorted.

    Returns:
        * Sequence of sorted array

    Example:
        >>>sorted_elements_specific_positions_away(
        [1, 2, 4, 0, 3], 3) == [0, 1, 2, 3, 4]
    """
    result = []
    min_heap = mini_heap.MinHeap()
    for element in elements[:positions_away]:
        min_heap.insert(element)

    for element in elements[positions_away:]:
        result.append(min_heap.pop())
        min_heap.insert(element)

    for _ in range(len(elements[:positions_away])):
        result.append(min_heap.pop())
    return result


if __name__ == "__main__":
    number_of_testcases = int(input(''))
    utilities.validate(number_of_testcases, lambda t: (t >= 1) and (t <= 100))

    for _ in range(number_of_testcases):
        length_and_positions_away = input('').split(' ')
        length_of_elements = int(length_and_positions_away[0])
        utilities.validate(
            length_of_elements, lambda n: (n >= 1) and (n <= 100)
        )

        elements_this_positions_away = int(length_and_positions_away[1])
        utilities.validate(
            elements_this_positions_away,
            lambda k: (k >= 1) and (k <= length_of_elements)
        )
        elements = input('').split(' ')
        elements = list(map(int, elements))
        result = sort_elements_specific_positions_away(
            elements, elements_this_positions_away
        )
        result = map(str, result)
        print(' '.join(result))
