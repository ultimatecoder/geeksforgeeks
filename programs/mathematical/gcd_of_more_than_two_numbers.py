"""
Problem

    Given an array of numbers, find GCD of the array elements.

Example 1

    Input

        [1, 2, 3]

    Output

        1

Example 2

    Input

        [2, 4, 6, 8]

    Output

        2
"""

def calculate_greatest_common_divisor_of_two_numbers(number_1, number_2):
    """Finds solution using Euclidean Algorithm

    Euclidean Algorithm link:
        https://simple.wikipedia.org/wiki/Euclidean_algorithm#The_algorithm_in_pseudocode
    """
    if number_1 < number_2:
        number_1, number_2 = number_2, number_1
    while number_2 != 0:
        remainder = number_1 % number_2
        number_1 = number_2
        number_2 = remainder
    return number_1


def find_greatest_common_divisor(numbers):
    if not numbers:
        return None
    if len(numbers) == 1:
        return numbers[0]
    gcd = calculate_greatest_common_divisor_of_two_numbers(
        numbers[0], numbers[1]
    )
    for index in range(2, len(numbers)):
        gcd = calculate_greatest_common_divisor_of_two_numbers(
            gcd, numbers[index]
        )
    return gcd
