#! /usr/bin/env python
"""
Problem

    Given an array of size N consisting of only 0's and 1's, which is sorted in
    such a manner that all the 1's are placed first and then they are followed
    by all the 0's.

Input

    The first line of input contains an integer T denoting the number of test
    cases. Then T test cases follow. The first line of each test case contains
    an integer N, where N is the size of the array A[]. The second line of each
    test case contains N space seperated integers of all 1's followed by all
    the 0's, denoting elements of the array A[].

Output

    Print out the number of 0's in the array.

Constraints

    1 <= T <= 100
    1 <= N <= 30
    0 <= A[i] <= 1

Example

    Input

        3
        12
        1 1 1 1 1 1 1 1 1 0 0 0
        5
        0 0 0 0 0
        6
        1 1 1 1 1 1

    Output

        3
        5
        0
"""
import utilities


def count_zeros(elements):
    """Calculates zeros in given elements

    This method performs the search operation using Bisection method. Time
    complexity of this method is O(log n).

    Arguemnts:
        * elements: Reverse sorted binary array. Element of the array can be 0
                    or 1.
    Returns:
        An integer representing count of zero's in a given element.
    """
    left = 0
    right = len(elements) - 1

    while (left <= right):
        middle = (left + right) // 2
        if elements[middle] == 0:
            right = middle - 1
        else:
            left = middle + 1
    return (len(elements) - left)


if __name__ == "__main__":
    number_of_test_cases = int(input(''))
    utilities.validate(number_of_test_cases, lambda t: (t >= 1) and (t <= 100))

    for _ in range(number_of_test_cases):
        length_of_elements = int(input(''))
        utilities.validate(
            length_of_elements,
            lambda n: (n >=1) and (n <= 30)
        )
        elements = input('').split(' ')
        elements = list(map(int, elements))
        for element in elements:
            utilities.validate(element, lambda e: (e == 0) or (e == 1))
        print(count_zeros(elements))
