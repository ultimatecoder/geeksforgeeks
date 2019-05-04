#! /usr/bin/env python


class MinHeap:
    """Minimum Heap

    Implementation of Heap data structure. It maintains the smallest element at
    root. Then the second minimum value will be at left child of the root. The
    last element is the highest element from the elements entered. This data
    structure is using List for storing elements.

    Source: Chapter 6 Heapsort, Introduction to Algorithms, 3rd edition.
    """

    def __init__(self):
        # NOTE: The first element is gap filler. The source algorithm is based
        # on storage indexed from 1 not 0. I am filling the 0th position of my
        # linked list to match whatever the source implementation is doing.
        self._elements = [None]
        self._size = 0

    @property
    def _heap_size(self):
        return len(self._elements) - 1

    def insert(self, key):
        """Adds the key to the heap

        This method finds the position in which all the left side of the
        elements are less than it and all the right side elements are greater
        than it.

        This method combines MIN-HEAP-INSERT and HEAP-INCREASE-KEY operation
        described at Introduction to Algorithm book chapter 6.
        """
        self._elements.append(key)
        index= self._heap_size
        parent = self._parent(index)
        while (
            (
                index > 1
            ) and (
                self._elements[index] < self._elements[self._parent(index)]
            )
        ):
            self._exchange(index, self._parent(index))
            index = self._parent(index)

    def pop(self):
        """Removes the minimum element from the heap"""
        minimum = self._elements[1]
        self._elements[1] = self._elements[self._heap_size]
        del self._elements[self._heap_size]
        self._min_heapify(1)
        return minimum


    def _parent(self, index):
        """Returns a parent of given Index"""
        return index//2

    def _left(self, index):
        """Returns a left children of the given Index value"""
        return 2*index

    def _right(self, index):
        """Returns right children element of the given index"""
        return (2*index) + 1

    def _exchange(self, position_1, position_2):
        tmp = self._elements[position_2]
        self._elements[position_2] = self._elements[position_1]
        self._elements[position_1] = tmp

    def _min_heapify(self, index):
        """Constructs a Heap for minimum value"""
        left = self._left(index)
        right = self._right(index)
        if ((left <= self._heap_size) and (
                self._elements[left] < self._elements[index])
        ):
            minimum = left
        else:
            minimum = index
        if ((right <= self._heap_size) and (
                self._elements[right] < self._elements[minimum])
        ):
            minimum = right

        if minimum != index:
            self._exchange(index, minimum)
            self._min_heapify(minimum)
