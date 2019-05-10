#! /usr/bin/env python

import unittest

from tree import binary_tree, diagonal_sum_in_binary_tree


class TestDiagonalSumInBinaryTree(unittest.TestCase):

    def test_calculate_sum_of_diagonal_nodes_for_sample_case_1(self):
        """Tree
                4
            1       3
                 3
        """
        tree = binary_tree.Tree(root_key=4)

        tree.insert_left_child(4, 1)
        tree.insert_right_child(4, 3)

        tree.insert_left_child(3, 3)

        self.assertListEqual(
            diagonal_sum_in_binary_tree.calculate_sum_of_diagonal_nodes(tree),
            [7, 4]
        )

    def test_calculate_sum_of_diagonal_nodes_for_sample_case_2(self):
        """Tree
                10
            2   |   8
              2 | 5   3
        """
        tree = binary_tree.Tree(root_key=10)

        tree.insert_left_child(10, 8)
        tree.insert_right_child(10, 2)

        tree.insert_left_child(8, 3)
        tree.insert_right_child(8, 5)

        tree.insert_left_child(2, 2)

        self.assertListEqual(
            diagonal_sum_in_binary_tree.calculate_sum_of_diagonal_nodes(tree),
            [12, 15, 3]
        )
