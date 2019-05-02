#! /usr/bin/env python
"""
Problem

    Given a Binary Tree of size N. The task is to find the sum of leaves of the
    given tree.

Input

    First line of input contains number of testcases T. For each testcase,
    there will be two lines, first of which containing the number of edges
    (between two nodes) in the tree. Next line contains N pairs (considering a
    and b) with a 'L' (means node b on left of a) or 'R' (means node b on right
    of a) after a and b.

Output

    For each testcase, there will be a single line containing the sum of all
    leaf nodes in the tree.

Constraints

    1 <= T <= 100
    1 <= N <= 10^3

Example

    Input

        2
        2
        1 2 L 1 3 R
        5
        10 20 L 10 30 R 20 40 L 20 60 R 30 90 L

    Output

        5
        190
"""
import utilities

from tree import binary_tree, node


def insert_key(tree, parent, key, side):
    """Inserts key as a child at parent of the tree

    Arguments:
        * tree   : An instance of binary_tree.Tree
        * parent : Key value of the parent
        * key    : Value of key to be inserted as child of parent
        * side   : The value of side can be 'L' or 'R'. The value 'L' will add
                   child key as the left child of the parent. The 'R' will add
                   child key as the right child of the parent.

    Raises:
        * `KeyError` if parent key is not found
        * `ValueError` if vlaue of size is different then values 'L' and 'R'.
    """
    if side not in ('L', 'R'):
        raise ValueError(
            f"The value of side can be 'L' or 'R', but not {side}"
        )

    if tree.root is None:
        tree.root = node.Node(parent)
    if side == 'L':
        tree.insert_left_child(parent, key)
    else:
        tree.insert_right_child(parent, key)


def parse(pairs):
    """Parses given input into batch of 3 values.

    Example:
    >>>parse(["10", "20", "L", "10", "30", "R"]) == [
    (10, 20, "L"), (10, 30, "R")
    ]
    """
    result = []
    gap = 3
    window = gap
    start = 0
    for _ in range(len(pairs)//3):
        pair = pairs[start:window]
        result.append((int(pair[0]), int(pair[1]), pair[2]))
        start = window
        window += gap
    return result


if __name__ == "__main__":
    number_of_testcases = int(input(''))
    utilities.validate(number_of_testcases, lambda n: (n >= 1) and (n <= 100))

    for _ in range(number_of_testcases):
        tree = binary_tree.Tree()
        length_of_pairs = int(input(''))
        utilities.validate(
            length_of_pairs,
            lambda l: (l >= 1) and (l <= 10**3)
        )
        pairs = input('').split(' ')
        pairs = parse(pairs)
        for pair in pairs:
            insert_key(tree, parent=pair[0], key=pair[1], side=pair[2])

        print(sum(tree.leaves))
