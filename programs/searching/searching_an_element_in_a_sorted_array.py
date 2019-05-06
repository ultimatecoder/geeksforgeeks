#! /usr/bin/env python
"""
Problem

    Given a sorted array arr[] of N integers and a number K is given. The task
    is to check if the element K is present in the array or not.

Input

    First line of input contains number of test cases T. For each testcase,
    first line of input contains number of elements in the array and the number
    K separated by space. Next line contains N elements.

Output

    For each test case, if the element is present in the array print "1"
    (without quotes), else print "-1" (without quotes).

Constraints

    1 <= T <= 100
    1 <= N <= 10^6
    1 <= K <= 10^6
    1 <= arr[i] <= 10^6

Example

    Input

        2
        5 6
        1 2 3 4 6
        5 2
        1 3 4 5 6

    Output

        1
        -1
"""
import utilities

from searching import binary


if __name__ == "__main__":
    number_of_test_cases = int(input(''))
    utilities.validate(
        number_of_test_cases, lambda t: (t >= 1) and (t <= 100)
    )
    for _ in range(number_of_test_cases):
        length_of_elements, element_to_be_searched = input('').split(' ')
        length_of_elements = int(length_of_elements)
        utilities.validate(
            length_of_elements, lambda l: (l >= 1) and (l <= 10**6)
        )
        element_to_be_searched = int(element_to_be_searched)
        utilities.validate(
            element_to_be_searched, lambda e: (e >= 1) and (e <= 10**6)
        )
        elements = input('').split(' ')
        elements = list(map(int, elements))
        for element in elements:
            utilities.validate(element, lambda e: (e >= 1) and (e <= 10**6))
        index = binary.binary_search(elements, element_to_be_searched)
        if index is not None:
            print("1")
        else:
            print("-1")
