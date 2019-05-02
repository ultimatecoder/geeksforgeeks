#! /usr/bin/env python


class Node:
    """Binary Tree Node

    Node is responsible for storing the key and remember left child and right
    child and its parent node.

    Each element in Binary tree is presented as the Node.
    Value of Left child or Right child can be empty or instance of other Node.
    """

    def __init__(self, key, parent=None):
        """Takes key to be store in a Node"""
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None
