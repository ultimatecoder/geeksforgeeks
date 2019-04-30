#! /usr/bin/env python
"""
Problem

    Given a struck array of type Height, having two elements feet and inches.
    Find the maximum height, where height is calculated sum of feet and inches
    after converting feet into inches.

Input

    First line of input contains number of testcases. For each testcase, first
    line of input contains N, number of given heights. Next line contains 2*N
    number of elements (feet and inches for each N).

Output

    Output maximum height from array.

Your Task

    Your task is to only complete the function of find maximum height from
    given array.

Constrains

    1 <= T <= 100
    1 <= N <= 10^5
    0 <= Feet, Inches <= 10^5

Example

    Input

        2
        2
        1221
        4
        35795655

    Output

        25
        93

Explanation

    Testcase 1

        (1, 2) and (2, 1) are respective given heights. After converting both
        heights in to inches, we get 14 and 25 as respective heights. So, 25 is
        the maximum height.
"""
import utilities


def parse_feets_and_inches(feets_and_inches):
    """Parse feets and inches into individual iterator

    The function already assumes that the length of given list is a factor of
    `2`.

    Arguments:
        * feets_and_inputs : An interable of object where all odd positioned
                             values are value for feet and all odd values are
                             values of inches
    Returns:
        A squence of tuples where first argument is value of feet and second
        argument is value for inche.

    Example:
        >>>assert parse_feets_and_inputs([1, 2, 2, 1]) == [(1, 2), (2, 1)]
    """
    parsed = []
    for iterator in range(0, len(feets_and_inches), 2):
        parsed.append(tuple(feets_and_inches[iterator: iterator+2]))
    return parsed


def inches(feets):
    """Converts value of given feets to inches

    12 inches = 1 feet

    Arguments:
        * feets: Interger or Float value of feets to be converted

    Retunrs:
        Returns Float value of inches for given feets
    """
    return 12*feets


if __name__ == "__main__":
    answers = []
    number_of_testcases = int(input(''))
    utilities.validate(number_of_testcases, lambda n: (1 <= n) and (n <= 100))

    for _ in range(number_of_testcases):
        length_of_inputs = int(input(''))
        utilities.validate(
            length_of_inputs, lambda n: (1 <= n) and (n <= 10**5)
        )

        feets_and_inches = input('')
        utilities.validate(
            len(feets_and_inches), lambda l: 2*length_of_inputs
        )
        utilities.validate(
            len(feets_and_inches), lambda l: (l >= 0) and (l <= 10**5)
        )

        feets_and_inches = list(map(int, feets_and_inches))
        feets_and_inches = parse_feets_and_inches(feets_and_inches)
        _inches = list(map(lambda i: inches(i[0]) + i[1], feets_and_inches))
        print(max(_inches))
