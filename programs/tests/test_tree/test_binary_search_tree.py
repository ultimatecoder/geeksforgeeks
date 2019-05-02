#! /usr/bin/env python

import unittest

from tree import binary_search_tree


class TestTree(unittest.TestCase):

    def setUp(self):
        self.tree = binary_search_tree.Tree()

    def test_tree_initialize_with_an_empty_root(self):
        self.assertIsNone(self.tree.root)

    def test_tree_insert(self):
        """Test insertion for example tree values

        Example Tree
                  4(2)
            1(1)   |      20(1)
                   |10(1)       30(1)

        4(2) = 4 is the Key value and 2 represents its count in the tree.
        """
        first_key = 4

        self.tree.insert(first_key)
        self.assertEqual(self.tree.root.key, first_key)
        self.assertEqual(self.tree.root.count, 1)
        self.assertIsNone(self.tree.root.left)
        self.assertIsNone(self.tree.root.right)

        second_key = 20

        self.tree.insert(second_key)
        self.assertEqual(self.tree.root.right.key, second_key)
        self.assertEqual(self.tree.root.right.count, 1)
        self.assertIsNone(self.tree.root.left)
        self.assertIsNone(self.tree.root.right.right)
        self.assertIsNone(self.tree.root.right.left)

        third_key = 30

        self.tree.insert(third_key)
        self.assertEqual(self.tree.root.right.right.key, third_key)
        self.assertEqual(self.tree.root.right.right.count, 1)
        self.assertIsNone(self.tree.root.right.left)
        self.assertIsNone(self.tree.root.right.right.left)
        self.assertIsNone(self.tree.root.right.right.right)


        fourth_key = 10

        self.tree.insert(fourth_key)
        self.assertEqual(self.tree.root.right.left.key, fourth_key)
        self.assertEqual(self.tree.root.right.right.key, third_key)
        self.assertEqual(self.tree.root.right.left.count, 1)
        self.assertEqual(self.tree.root.right.right.count, 1)
        self.assertIsNone(self.tree.root.right.left.right)
        self.assertIsNone(self.tree.root.right.left.right)

        fifth_key = 1

        self.tree.insert(fifth_key)
        self.assertEqual(self.tree.root.left.key, fifth_key)
        self.assertEqual(self.tree.root.left.count, 1)
        self.assertIsNone(self.tree.root.left.right)
        self.assertIsNone(self.tree.root.left.right)

        fifth_key = 1

        self.tree.insert(fifth_key)
        self.assertEqual(self.tree.root.left.key, fifth_key)
        self.assertEqual(self.tree.root.left.key, 1)
        self.assertIsNone(self.tree.root.left.right)
        self.assertIsNone(self.tree.root.left.right)

        # Re-adding the first key
        self.tree.insert(first_key)
        self.assertEqual(self.tree.root.key, first_key)
        self.assertEqual(self.tree.root.count, 2)


    def test_tree_leaves(self):
        """Test tree leaves is able to work against given input

        Example Tree
                        5(1)
                2(1)     |   6(1)
            1(1)    3(2) |
        """

        keys = [5, 2, 3, 3, 1, 6]
        for key in keys:
            self.tree.insert(key)

        self.assertListEqual(
            self.tree.leaves,
            [6, 3, 3, 1]
        )
