#! /usr/bin/env python
"""Collection of classes for Binary Search Tree"""

from tree import node
from queue import queue


class Tree:
    """Use this class to implement Binary Search Tree

    Duplicates
        This tree allows duplicates by storing a count at Node instance.
    """

    def __init__(self):
        self.root = None

    def insert(self, key):
        """Adds key to the Tree

        Arguments:
            * key : Key is the value which will be added to the Tree.

        Return:
            Created instance of Node for the given key value
        """
        if self.root is None:
            self.root = node.Node(key)
        else:
            _queue = queue.Queue()
            _queue.enqueue(self.root)

            while len(_queue) != 0:
                _node = _queue.dequeue()
                if key > _node.key:
                    if _node.right is None:
                        _node.right = node.Node(key)
                    else:
                        _queue.enqueue(_node.right)
                elif key < _node.key:
                    if _node.left is None:
                        _node.left = node.Node(key)
                    else:
                        _queue.enqueue(_node.left)
                else:
                    _node.count += 1


    @property
    def leaves(self):
        """Returns collection of leaves of Tree.

        Returns:
            List of keys of all the leaf nodes of the Tree.
        """
        leaves = []
        if self.root is not None:
            _queue = queue.Queue()
            _queue.enqueue(self.root)

            while len(_queue) != 0:
                _node = _queue.dequeue()
                if (_node.right is None) and (_node.left is None):
                    for _ in range(_node.count):
                        leaves.append(_node.key)
                else:
                    if _node.right is not None:
                        _queue.enqueue(_node.right)
                    if _node.left is not None:
                        _queue.enqueue(_node.left)
        return leaves
