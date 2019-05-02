#! /usr/bin/env python

import unittest

from tree import node


class TestNode(unittest.TestCase):

    def test_node_initialize_appropriately(self):
        root_key = 3
        root = node.Node(root_key)

        self.assertEqual(root.key, root_key)
        self.assertIsNone(root.right)
        self.assertIsNone(root.left)

        root_right_key = 4

        root.right = node.Node(root_right_key)

        self.assertEqual(root.right.key, root_right_key)
        self.assertIsNone(root.right.left)
        self.assertIsNone(root.right.right)
        self.assertIsNone(root.left)

        root_left_key = 5

        root.left = node.Node(root_left_key)

        self.assertEqual(root.left.key, root_left_key)
        self.assertEqual(root.right.key, root_right_key)

        self.assertIsNone(root.left.right)
        self.assertIsNone(root.left.left)

        self.assertIsNone(root.right.right)
        self.assertIsNone(root.right.left)
