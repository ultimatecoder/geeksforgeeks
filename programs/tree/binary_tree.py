#! /usr/bin/env python
"""Binary Tree

Collection of Classes giving functionality to use Binary Tree data structure.
"""

from queue import queue
from tree import node


class Tree:
    """Binary Tree

    If the 'root' attribute is empty then the tree is empty.
    """

    def __init__(self, root_key=None):
        """Creates an instance of Binary tree

        Arguments:
            * root_key: Value of key for root of the tree
        """
        if root_key is not None:
            self.root = node.Node(root_key)
        else:
            self.root = None

    def find(self, key):
        """Returns an instance of Node having specific key value

        Arguments:
            * key : A value of key which will be searched inside the tree.
        Returns:
            Intance of `Node` having `key` as the given argument of the key.
        Raises:
            `KeyError` if given value of the Key is not found in the tree.
        """
        if self.root is not None:
            _queue = queue.Queue()
            _queue.enqueue(self.root)

            while len(_queue) != 0:
                node = _queue.dequeue()
                if node.key == key:
                    return node
                if node.right is not None:
                    _queue.enqueue(node.right)
                if node.left is not None:
                    _queue.enqueue(node.left)
            raise KeyError(f"{key} not found in Tree.")
        else:
            raise KeyError("The tree is empty")

    def insert_left_child(self, parent_key, key):
        """Adds Left child element

        Arguments:
            * parent_key : Value of key under which this will be added as the
                           left child
            * key        : Value of key which will be added as the child


        Raises:
            `KeyError` if given value for `parent_key` is not found in the
            tree.

        Returns:
            Instance of Node added as the children

        """
        parent_node = self.find(parent_key)
        parent_node.left = node.Node(key)
        return parent_node.left

    def insert_right_child(self, parent_key, key):
        """Adds Right child element

        Arguments:
            * parent_key : Value of key under which this key will be added as
                           the right child.
            * key        : Value of key which will be added as the right child
                           of the parent key.

        Raises:
            `KeyError` if the given value for `prarent_key` is not found in the
            tree.

        Returns:
            Instance of Node added as the children
        """
        parent_node = self.find(parent_key)
        parent_node.right = node.Node(key)
        return parent_node.right

    @property
    def leaves(self):
        """Returns collection of leaves of the tree

        Example
        Below is the given tree
                30
            20          40
        10      5   3       4

        Then this method will return [10, 5, 3, 4] values.
        """
        if self.root is None:
            return []
        else:
            leaves = []
            _queue = queue.Queue()
            _queue.enqueue(self.root)

            while len(_queue) != 0:
                node = _queue.dequeue()
                if (node.left is None) and (node.right is None):
                    leaves.append(node.key)
                if node.left is not None:
                    _queue.enqueue(node.left)
                if node.right is not None:
                    _queue.enqueue(node.right)
            return leaves
