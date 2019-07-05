#! /usr/bin/env python

import unittest

from tree.binary_tree import Tree
from tree.node import Node
from tree import binary_tree_mirror


class TestConstructMirrorTree(unittest.TestCase):

    def test_mirror_tree_for_example_1(self):
        tree = Tree(5)
        tree.root.left = Node(6)
        tree.root.right = Node(9)
        tree.root.left.left = Node(7)
        tree.root.left.right = Node(8)
        tree.root.right.right = Node(10)

        binary_tree_mirror.mirror_tree(tree.root)

        self.assertEqual(tree.root.key, 5)
        self.assertEqual(tree.root.left.key, 9)
        self.assertEqual(tree.root.right.key, 6)
        self.assertEqual(tree.root.left.left.key, 10)
        self.assertIsNone(tree.root.left.right)
        self.assertEqual(tree.root.right.left.key, 8)
        self.assertEqual(tree.root.right.right.key, 7)

    def test_mirror_tree_for_example_2(self):
        tree = Tree(1)
        tree.root.left = Node(3)
        tree.root.right = Node(2)
        tree.root.right.left = Node(5)
        tree.root.right.right = Node(4)

        binary_tree_mirror.mirror_tree(tree.root)

        self.assertEqual(tree.root.key, 1)
        self.assertEqual(tree.root.left.key, 2)
        self.assertEqual(tree.root.right.key, 3)
        self.assertEqual(tree.root.left.left.key, 4)
        self.assertEqual(tree.root.left.right.key, 5)
        self.assertIsNone(tree.root.right.right)
        self.assertIsNone(tree.root.right.left)
