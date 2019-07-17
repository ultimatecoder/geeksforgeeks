#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Program

    You are given an array 'A' of size 'N'. Find out the maximum difference
    between any two elements such that larger element appears after the smaller
    number in 'A'.

Input

    The first line of input contains an integer 'T' denoting the number of test
    cases. 'T' test cases follow will be followed by two lines for each test
    case. The first line of each test case is 'N' where 'N' is a size of an
    array. The second line of each test case contains 'N' elements separated by
    a space.

Output

    For each test case, print a maximum difference between two elements. If
    there are no differences which is satisfying the condition then print -1.

Constrains:

    * 1 <= T <= 100
    * 1 <= N <= 10^7
    * -10^6 <= A[i] <= 10^6
    * A[i] < A[j]
    * Where, 0 <= i <= j <= n

Example

    Input

        2
        7
        2 3 10 6 4 8 1
        6
        7 9 5 6 3 2

    Output

        8
        2

Explanation

    Test case 1

        Array is [2, 3, 10, 6, 4, 8, 1] then returned value is 8 (Difference
        between 10 and 2)

    Test case 2

        Array is [7, 9, 5, 6, 3, 2] then returned value is 2 (Difference
        between 7 and 9).

Problem link

    https://practice.geeksforgeeks.org/problems/maximum-difference/0
"""
import math

from utilities import validate


def find_maximum_difference(numbers):
    """Returns maximum difference from given set of numbers

    Calculated maximum difference of pair should satisfy below condition:

        * Left hand side number should be greater than right hand side number

        * Index of Left hand side should be greater than index of right hand
          side.

        * It should be maximum from all pairs satisfying above two conditions.

    Example of valid and invalid pairs:

        * Valid:

            * 3 - 1 = 2

        * Invalid:

            3 - 5 = -2

    Example of valid sequence:

        * Valid:

            numbers = [1, 2, 1, 4, 5]

            Pairs:

                * 2 - 1 = 1
                * 4 - 1 = 3
                * 4 - 2 = 2
                * 5 - 4 = 1
                * 5 - 1 = 4
                * 5 - 2 = 3

            Here, answer is 5 - 1 = 4 because it is maximum from all pairs.

    If no pairs are satisfying above condition then this method will return -1.
    """
    minimum = math.inf
    maximum_difference = -1
    for number in numbers:
        if number < minimum:
            minimum = number
            continue
        if number > minimum:
            difference = number - minimum
            if difference > maximum_difference:
                maximum_difference = difference
    return maximum_difference


def _convert(number_str):
    """Validates that given number is in range.

    Raises ValueError if any number is not under valid range.
    Returns integer of given value.
    """
    number = int(number_str)
    validate(number, lambda n: (n >= (-10 ** 7)) and (n <= (10 ** 7)))
    return number


if __name__ == "__main__":
    number_of_test_cases = int(input(''))
    validate(number_of_test_cases, lambda t: (t >= 1) and (t <= 100))
    for _ in range(number_of_test_cases):
        length_of_numbers = int(input(''))
        validate(
            length_of_numbers, lambda l: (l >= 1) and (l <= 10 ** 7)
        )
        numbers = input('').split()
        numbers = list(map(_convert, numbers))
        print(find_maximum_difference(numbers))
