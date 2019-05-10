#! /usr/bin/env python
"""
Problem

    You need to sort elements of an array where the array can be of following
    data-types:
        * Integer
        * String
        * Floating number

Input

    The input line contains T, denoting the number of test cases. Each test
    case contains 2 lines. The first line contains N (size of array) and Q
    (type of array) separated by space. Below is the description about Q.

    * Q = 1, Means elements of the array are of integer type.
    * Q = 2, Means elements of the array are of string type.
    * Q = 3, Means elements of the array are of floating digit type.

    The second line contains N elements of the array separated by space.

Output

    For each test case in new line, print the elements in sorted form of given
    type of array separated by space.


Constraints

    * 1 <= T <= 50
    * 1 <= N <= 100
    * 1 <= Q <= 3

Example

    Input

        3
        3 3
        34.23 -4.35 3.4
        4 1
        123 -2311 837 0
        5 2
        focus on challenges in implementing

    Output

        -4.35 3.4 34.23
        -2311 0 123 837
        challenges focus implementing in on
"""
import utilities

from sorting import merge


if __name__ == "__main__":
    number_of_test_cases = int(input(''))
    utilities.validate(number_of_test_cases, lambda t: (t >= 1) and (t <= 50))

    for _ in range(number_of_test_cases):
        length_and_data_type = input('').split(' ')
        utilities.validate(
            length_and_data_type, lambda l: len(l) == 2
        )
        length_of_elements = int(length_and_data_type[0])
        utilities.validate(
            length_of_elements, lambda l: (l >= 1) and (l <= 100)
        )
        data_type = int(length_and_data_type[1])
        utilities.validate(
            data_type, lambda d: (d >= 1) and (d <= 3)
        )
        elements = input('').split(' ')
        if data_type == 1:
            elements = list(map(int, elements))
        elif data_type == 3:
            elements = list(map(float, elements))
        merge.merge_sort(elements)
        elements = map(str, elements)
        print(' '.join(elements))
