#! /usr/bin/env python

import unittest

from tree import binary_tree, node


class TestTree(unittest.TestCase):

    def setUp(self):
        pass

    def test_tree_is_intialized_with_default_arguments(self):
        tree = binary_tree.Tree()
        self.assertIsNone(tree.root)

    def test_tree_is_intialized_with_root_key(self):
        root_key = 4
        tree = binary_tree.Tree(root_key)
        self.assertEqual(tree.root.key, root_key)
        self.assertIsNone(tree.root.left)
        self.assertIsNone(tree.root.right)

    def test_find(self):
        # Example Tree data
        #           0
        #       1       2
        #   3       4

        tree = binary_tree.Tree(0)

        tree.root.left = node.Node(key=1)
        tree.root.right = node.Node(key=2)

        tree.root.left.left = node.Node(key=3)
        tree.root.left.right = node.Node(key=4)

        key_and_expected_values = (
            # Data representation
            #   Value at index 0 is key,
            #   Value at index 1 is expected_left_child_key
            #   Value at index 2 is expected_right_child_key,
            #)
            (0, 1, 2),
            (1, 3, 4),
            (2, None, None),
            (3, None, None),
            (4, None, None),
        )

        for (
            key,
            expected_left_child_key,
            expected_right_child_key,
        ) in key_and_expected_values:
            with self.subTest(
                key=key,
                expected_left_child_key=expected_left_child_key,
                expected_right_child_key=expected_right_child_key,
            ):
                _node = tree.find(key)
                if expected_left_child_key is not None:
                    self.assertEqual(_node.left.key, expected_left_child_key)
                else:
                    self.assertIsNone(_node.left)

                if expected_right_child_key is not None:
                    self.assertEqual(_node.right.key, expected_right_child_key)
                else:
                    self.assertIsNone(_node.right)

    def test_find_for_unknown_keys(self):
        tree = binary_tree.Tree(0)
        tree.insert_left_child(parent_key=0, key=1)
        tree.insert_right_child(parent_key=0, key=2)

        values = (100, 3, -1, 101)

        for value in values:
            with self.subTest(value=value):
                with self.assertRaises(KeyError):
                    tree.find(value)

    def test_insert_right_child(self):
        # Example Tree
        #           0
        #       1
        #   2
        root_key = 0
        tree = binary_tree.Tree(root_key)
        first_right_key = 1
        first_right_child = tree.insert_right_child(root_key, first_right_key)

        self.assertEqual(first_right_child.key, first_right_key)
        self.assertIsNone(first_right_child.right)
        self.assertIsNone(first_right_child.left)

        second_right_key = 2
        second_right_child = tree.insert_right_child(
            parent_key=first_right_key, key=second_right_key
        )

        self.assertEqual(second_right_child.key, second_right_key)
        self.assertIsNone(second_right_child.right)
        self.assertIsNone(second_right_child.left)

    def test_insert_right_child_for_unknown_keys(self):
        tree = binary_tree.Tree(0)
        tree.insert_left_child(parent_key=0, key=1)
        tree.insert_right_child(parent_key=0, key=2)

        parent_keys = (98, 3, "@", -1)

        for parent_key in parent_keys:
            with self.subTest(parent_key=parent_key):
                with self.assertRaises(KeyError):
                    tree.insert_right_child(parent_keys, 10)

    def test_insert_left_child(self):
        # Example Tree
        #           0
        #               1
        #                   2
        root_key = 0
        tree = binary_tree.Tree(root_key)
        first_left_key = 1
        first_left_child = tree.insert_left_child(root_key, first_left_key)

        self.assertEqual(first_left_child.key, first_left_key)
        self.assertIsNone(first_left_child.right)
        self.assertIsNone(first_left_child.left)

        second_left_key = 2
        second_left_child = tree.insert_left_child(
            parent_key=first_left_key, key=second_left_key
        )

        self.assertEqual(second_left_child.key, second_left_key)
        self.assertIsNone(second_left_child.right)
        self.assertIsNone(second_left_child.left)

    def test_insert_left_child_for_unknown_keys(self):
        tree = binary_tree.Tree(0)
        tree.insert_left_child(parent_key=0, key=1)
        tree.insert_left_child(parent_key=0, key=2)

        parent_keys = (2232, 22, "A", 0)

        for parent_key in parent_keys:
            with self.subTest(parent_key=parent_key):
                with self.assertRaises(KeyError):
                    tree.insert_left_child(parent_keys, 10)

    def test_leaves(self):
        tree = binary_tree.Tree(0)
        tree.insert_right_child(parent_key=0, key=1)
        tree.insert_left_child(parent_key=0, key=2)

        tree.insert_right_child(parent_key=1, key=3)
        tree.insert_left_child(parent_key=1, key=4)

        tree.insert_right_child(parent_key=2, key=5)
        tree.insert_left_child(parent_key=2, key=6)

        self.assertListEqual(
            tree.leaves,
            [6, 5, 4, 3],
            "Invalid values of leaves"
        )
