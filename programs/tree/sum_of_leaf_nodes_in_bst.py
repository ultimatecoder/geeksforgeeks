#! /usr/bin/env python
"""
Problem

    Given a Binary Search Tree, find the sum of all leaf nodes. BST has the
    following property (duplicate nodes are possible):

        * The left subtree of a node contains only nodes with keys less than
        the node's key.

        * The right subtree of a node contains only nodes with keys greater
        than or equal to the node's key.

Input

    The first line of input contains a single integer "T" denoting the number
    of test cases. Then "T" cases follow. Each test case consists of integer N,
    denoting the number of elements in the BST. The second line of each test
    case consists of N space-seperated integers denoting the elements in the
    BST.

Output

    For each testcase, in a new line, print the sum of leaf nodes.

Constraints:

    1 <= T <= 10^3
    1 <= N <= 10^5

Example

    Input

        2
        6
        67 34 82 12 45 78
        1
        45

    Output

        135
        45
"""
import utilities

from tree import binary_search_tree


if __name__ == "__main__":
    number_of_testcases = int(input(''))
    utilities.validate(
        number_of_testcases, lambda n: (n >= 1) and (n <= 10**3)
    )
    for _ in range(number_of_testcases):
        tree = binary_search_tree.Tree()
        length_of_input = int(input(''))
        utilities.validate(
            length_of_input, lambda n: (n >= 1) and (n <= 10**5)
        )
        elements = input('').split(' ')
        elements = map(int, elements)
        for element in elements:
            tree.insert(element)
        print(sum(tree.leaves))
