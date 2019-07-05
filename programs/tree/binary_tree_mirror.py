#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Problem

    Given a binary tree, modify it to its mirror view.


Example 1


    Source tree:

            5

        6           9

    7       8           10

    Mirror tree:

            5

        9           6

    10          8       7


Example 2

    Source tree:

              1

        3           2

                5       4

    Mirror tree:

              1

        2           3

    4       5

Problem link

    https://practice.geeksforgeeks.org/problems/construct-mirror-tree
"""


def mirror_tree(root):
    """Modifies existing tree as if its mirrow view

    This method will exchange each child element to match a mirrow view of
    binary tree.
    """
    if root == None:
        return
    root.left, root.right = root.right, root.left
    mirror_tree(root.left)
    mirror_tree(root.right)
