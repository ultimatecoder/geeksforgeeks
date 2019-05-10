#! /usr/bin/env python

import unittest

from tree import binary_tree, tree_utilities


class TestSumOfLeafNodes(unittest.TestCase):

    def setUp(self):
        self.tree = binary_tree.Tree()

    def test_insert_key_with_wrong_parent_key(self):
        tree_utilities.insert_key(self.tree, 10, 20, 'L')

        with self.assertRaises(KeyError):
            tree_utilities.insert_key(self.tree, 50, 60, 'R')

    def test_insert_key_with_wrong_side(self):
        with self.assertRaises(ValueError):
            tree_utilities.insert_key(self.tree, 50, 60, 'J')

    def test_insert_key_works_appropriately(self):
        values = (
            (10, 20, 'L'),
            (10, 30, 'R'),
            (20, 40, 'L'),
            (20, 60, 'R'),
            (30, 90, 'L')
        )
        for parent, key, side in values:
            with self.subTest(parent=parent, key=key, side=side):
                tree_utilities.insert_key(self.tree, parent, key, side)

        self.assertEqual(self.tree.root.key, 10)
        self.assertEqual(self.tree.root.left.key, 20)
        self.assertEqual(self.tree.root.right.key, 30)
        self.assertEqual(self.tree.root.left.right.key, 60)
        self.assertEqual(self.tree.root.left.left.key, 40)
        self.assertEqual(self.tree.root.right.left.key, 90)
        self.assertIsNone(self.tree.root.right.right)

    def test_parse(self):
        self.assertListEqual(
            tree_utilities.parse(["10", "20", "L", "10", "30", "R"]),
            [(10, 20, "L"), (10, 30, "R")]
        )
        self.assertListEqual(
            tree_utilities.parse(
                [
                    "10", "20", "L",
                    "10", "30", "R",
                    "20", "40", "L",
                    "20", "60", "R",
                    "30", "90", "L"
                ]
            ),
            [
                (10, 20, "L"),
                (10, 30, "R"),
                (20, 40, "L"),
                (20, 60, "R"),
                (30, 90, "L")
            ]
        )
