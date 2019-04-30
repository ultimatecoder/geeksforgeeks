#! /usr/bin/env python

from collections import defaultdict


class Queue:

    def __init__(self):
        self._elements = []
        self._frequency = defaultdict(int)

    def enqueue(self, element):
        """Add an item element to rear of Queue"""
        self._elements.append(element)
        self._frequency[element] += 1

    def dequeue(self):
        """Remove an item from the front of Queue"""
        element = self._elements[0]
        del self._elements[0]
        return element

    def __len__(self):
        """Returns number of elements in Queue"""
        return len(self._elements)

    def front(self):
        """Finds front item"""
        return self._elements[0]

    def reverse(self, number_of_elements):
        """Reverse the expected number of elements of Queue"""
        size = len(self)
        stack = []
        elements = []
        for _ in range(number_of_elements):
            stack.append(self.dequeue())

        for _ in range(number_of_elements):
            elements.append(stack.pop())

        for _ in range(number_of_elements, size):
            elements.append(self.dequeue())
        self._elements = elements

    def frequency(self, element):
        """Returns frequency of given element at Queue"""
        if element in self._frequency:
            return self._frequency[element]
        else:
            return 0
