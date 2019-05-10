#! /usr/bin/env python
"""
Problem

    Consider lines of slop - 1 passing between nodes. The diagonal sum in a
    binary tree is the sum of all node's data lying between these lines. Given
    a Binary Tree, print all diagonal sums.

                        1

                2               3

            9       6        4     5

             10   11       12  7

    Diagonal travelsel will be
        * 1 -> 3  -> 5
        * 2 -> 6  -> 4 -> 7
        * 9 -> 10 -> 11 -> 12

Input

    The first line consists of T test cases. The first line of every test case
    consists of N, denoting the number of edges in the tree. The second and
    third of every test case consists of N, nodes of the binary tree.

Output

    Print space seperated integers which are the diagonal sums for every
    diagonal present in the tree with slop -1.

Constraints

    * 1 <= T <= 100
    * 1 <= N <= 100

Example

    Input

        2
        3
        4 1 L 4 3 R 3 3 L
        5
        10 8 L 10 2 R 8 3 L 8 5 R 2 2 L

    Output

        7 4
        12 15 3
"""
from queue import queue
from tree import binary_tree, tree_utilities
import utilities


def calculate_sum_of_diagonal_nodes(tree_obj):
    """Calculates sum of Diagonal nodes.

    Arguments:
        * tree_obj : An instance of tree.binary_tree.Tree class.

    Returns:
        * Collection of sum calculated by traversing nodes diagonally.
    """
    sum_of_diagonal_nodes = []
    next_queue = queue.Queue()
    next_queue.enqueue(tree_obj.root)

    while len(next_queue) > 0:
        current_queue = next_queue
        next_queue = queue.Queue()
        sum_of_nodes = 0

        while len(current_queue) > 0:
            node = current_queue.dequeue()
            sum_of_nodes += node.key

            if node.left is not None:
                next_queue.enqueue(node.left)
            if node.right is not None:
                current_queue.enqueue(node.right)

        sum_of_diagonal_nodes.append(sum_of_nodes)
    return sum_of_diagonal_nodes


if __name__ == "__main__":
    number_of_test_cases = int(input(''))
    utilities.validate(
        number_of_test_cases, lambda t: (t >= 1) and (t <= 100)
    )
    for _ in range(number_of_test_cases):
        tree = binary_tree.Tree()
        length_of_nodes = int(input(''))
        utilities.validate(
            length_of_nodes,
            lambda l: (l >= 1) and (l <= 100)
        )
        pairs = input('').split(' ')
        pairs = tree_utilities.parse(pairs)
        for pair in pairs:
            tree_utilities.insert_key(
                tree, parent=pair[0], key=pair[1], side=pair[2]
            )
        sums = calculate_sum_of_diagonal_nodes(tree)
        sums = map(str, sums)
        print(' '.join(sums))
