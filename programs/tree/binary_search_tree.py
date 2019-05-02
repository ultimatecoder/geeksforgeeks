#! /usr/bin/env python
"""Collection of classes for Binary Search Tree"""


class Node:
    """Responsible for strong key

    Stores value of Key, a reference to its left child and right child
    """

    def __init__(self, key):
        """Creates an instance of the Node

        Arguments:
            * key : A value of key to be store in the node
        """
        self.key = key
        self.left = None
        self.right = None


class Tree:
    """Use this class to implement Binary Search Tree"""

    def __init__(self):
        self.root = None

    def insert(self, key):
        """Adds key to the Tree

        Arguments:
            * key : Key is the value which will be added to the Tree.

        Return:
            Created instance of Node for the given key value
        """
        pass

    def leaves(self):
        """Returns collection of leaves of Tree.

        Returns:
            List of keys of all the leaf nodes of the Tree.
        """
        pass
