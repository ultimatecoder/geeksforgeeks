#! /usr/bin/env python
"""
Problem

    Given an integer K and a queue of integers, we need to reverse the order of
    the first K elements of the queue, leaving the other elements in the same
    relative order.

    Only following standard operations are allowed on queue.

        * enqueue(x): Add an item x to rear of queue.
        * dequeue(): Removes an item from front of queue.
        * size(): Returns number of elements in queue.
        * front(): Finds front item.

    Input format:

        First line consists of T test cases. First line of every test case
        consists of 2 integers, N and K, denoting number of elements and number
        of elements to be reversed respectively. Second line of every test case
        consists of elements of array.

    Output format:

        For each testcase, in a new line, print the modified queue.

    Your task:

        Since this is a function problem, you don't need to take inputs. Just
        complete the provided functions.

    Constrains:

        1 <= T <= 100
        1 <= N <= 1000
        1 <= K <= N

    Example

        Input

            1
            5 3
            1 2 3 4 5

        Output

            3 2 1 4 5
"""
import utilities

import queue


if __name__ == "__main__":
    number_of_test_cases = int(input(''))
    utilities.validate(
        number_of_test_cases,
        lambda n: (n >= 1) and (n <= 100)
    )

    for _ in range(number_of_test_cases):
        length_of_elements, elements_to_reverse = input('').split(' ')

        length_of_elements = int(length_of_elements)
        utilities.validate(
            length_of_elements,
            lambda n: (n >= 1) and (n <= 1000)
        )

        elements_to_reverse = int(elements_to_reverse)
        utilities.validate(
            elements_to_reverse,
            lambda n: (n >= 1) and (n <= length_of_elements)
        )
        elements = input('').split(' ')
        elements = map(int, elements)

        _queue = queue.Queue()
        for element in elements:
            _queue.enqueue(element)
        _queue.reverse(elements_to_reverse)
        output = []
        for _ in range(len(_queue)):
            output.append(str(_queue.dequeue()))
        print(' '.join(output))
