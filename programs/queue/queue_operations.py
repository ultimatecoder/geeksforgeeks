#! /usr/bin/env python
"""
Problem

    Given N integers, the task is to insert those elements in the queue. Also,
    given M integers, task is to find the frequency of each number in The
    Queue.

Input format

    First line of input contains number of testcases T. For each testcase,
    there will be four lines. First line contains N, second line contains N
    integers seperated by space. Third line contains M, next line contains M
    integers seperated.

Output Format

    For each testcase, print the frequency of given elements.

Your task

    Your task is to complete the function 'insert()' and 'findFrequency()'
    which inserts the element into the queue and find the count of occurences
    of element in the queue respectively.

Constraints

    1 <= T <= 100
    1 <= N <= 10^3
    1 <= M <= 10^3
    1 <= Elements of Queue <= 10^6

Example

    Input

        1
        8
        1 2 3 4 5 2 3 1
        5
        1 3 2 9 10

    Output

        2
        2
        2
        -1
"""
import utilities

import queue


def validate_elements(elements, constraint):
    """Validates elements against given constraints

    This method picks individual element from the collection of elements and
    validate it for given constraints.

    Arguments
    * elements: Iterable.
        * constraint: A function which will be fired against given element.

    Raises
        If any element value is invalid by given constraints then it will raise
      `ValidationError`
    """
    for element in elements:
        utilities.validate(element, constraint)


if __name__ == "__main__":
    number_of_test_cases = int(input(''))
    utilities.validate(
        number_of_test_cases, lambda n: (n >= 1) and (n <= 100)
    )

    for _ in range(number_of_test_cases):
        _queue = queue.Queue()
        length_of_elements = int(input(''))
        utilities.validate(
            length_of_elements, lambda n: (n >= 1) and (n <= 10**3)
        )

        elements = input('').split(' ')
        elements = list(map(int, elements))t
        validate_elements(elements, lambda n: (n >= 1) and (n <= 10**6))
        for element in elements:
            _queue.enqueue(element)

        length_of_find_frequency_elements = int(input(''))
        utilities.validate(
            length_of_find_frequency_elements,
            lambda n: (n >= 1) and (n <= 10**3)
        )

        find_frequency_elements = input('').split(' ')
        find_frequency_elements = list(map(int, find_frequency_elements))
        validate_elements(
            find_frequency_elements, lambda n: (n >= 1) and (n <= 10**6)
        )
        for element in find_frequency_elements:
            frequency = _queue.frequency(element)
            print(-1 if frequency == 0 else frequency)
