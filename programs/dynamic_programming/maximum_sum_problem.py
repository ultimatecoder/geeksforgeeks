#! /usr/bin/env python
"""
Problem

    Given a number n, we can divide it in only three parts n/2, n/3 and n/4 (we
    will consider only integer part). The task is to find the maximum sum we
    can make by dividing number in three parts recursively and summing up them
    together.

    Note: Sometimes, the maximum sum can be obtained by not dividing n.

Input

    The first line of input contains an integer T denoting the number of test
    cases. Then T test cases follow. The first line of each test case contains
    the integer n.

Output

    For each test case, in a new line, print the maximum sum possible.

Constraints

    * 1 <= T <= 100
    * 1 <= 10^5

Example

    Input

        2
        12
        24

    Output

        13
        27
"""
import utilities


def calculate_maximum_sum(number, cached_result=None):

    if cached_result is None:
        cached_result = {0: 0}

    try:
        return cached_result[number]
    except KeyError:
        sum_of_half = calculate_maximum_sum(
            number // 2, cached_result=cached_result
        )
        sum_of_one_third = calculate_maximum_sum(
            number // 3, cached_result=cached_result
        )
        sum_of_one_fourth = calculate_maximum_sum(
            number // 4, cached_result=cached_result
        )
        cached_result[number] = max(
            number, sum_of_half + sum_of_one_third + sum_of_one_fourth
        )
        return cached_result[number]


if __name__ == "__main__":
    number_of_test_cases = int(input(''))
    utilities.validate(
        number_of_test_cases, lambda t: (t >= 1) and (t <= 100)
    )

    for _ in range(number_of_test_cases):
        number = int(input(''))
        utilities.validate(number, lambda n: (n >= 1) and (n <= 10**5))
        print(calculate_maximum_sum(number))
