#! /usr/bin/env python
"""
Problem

    Given an integer K and a queue of integers, we need to reverse the order of
    the first K elements of the queue, leaving the other elements in the same
    relative order.

    Only following standard operations are allowed on queue.

        * enqueue(x): Add an item x to rear of queue.
        * dequeue(): Removes an item from front of queue.
        * size(): Returns number of elements in queue.
        * front(): Finds front item.

    Input format:

        First line consists of T test cases. First line of every test case
        consists of 2 integers, N and K, denoting number of elements and number
        of elements to be reversed respectively. Second line of every test case
        consists of elements of array.

    Output format:

        For each testcase, in a new line, print the modified queue.

    Your task:

        Since this is a function problem, you don't need to take inputs. Just
        complete the provided functions.

    Constrains:

        1 <= T <= 100
        1 <= N <= 1000
        1 <= K <= N

    Example

        Input

            1
            5 3
            1 2 3 4 5

        Output

            3 2 1 4 5
"""

class Queue:

    def __init__(self):
        self._elements = []

    def enqueue(self, x):
        """Add an item x to rear of queue"""
        self._elements.append(x)

    def dequeue(self):
        """Remove an item from the front of queue"""
        element = self._elements[0]
        del self._elements[0]
        return element

    def size(self):
        """Returns number of elements in queue"""
        return len(self._elements)

    def front(self):
        """Finds front item"""
        return self._elements[0]

    def reverse(self, number_of_elements):
        """Reverse the expected number of elements of queue"""
        size = self.size()
        stack = []
        elements = []
        for _ in range(number_of_elements):
            stack.append(self.dequeue())

        for _ in range(number_of_elements):
            elements.append(stack.pop())

        for _ in range(number_of_elements, size):
            elements.append(self.dequeue())
        self._elements = elements


def validate(value, constraint):
    """Raises 'ValidationError` value is violating constraint"""
    if not constraint(value):
        raise ValueError(
            f"The value {value} is wrong against given constraints"
        )
    return True


if __name__ == "__main__":
    number_of_test_cases = int(input(''))
    validate(
        number_of_test_cases,
        lambda n: (n >= 1) and (n <= 100)
    )

    for _ in range(number_of_test_cases):
        length_of_elements, elements_to_reverse = input('').split(' ')

        length_of_elements = int(length_of_elements)
        validate(
            length_of_elements,
            lambda n: (n >= 1) and (n <= 1000)
        )

        elements_to_reverse = int(elements_to_reverse)
        validate(
            elements_to_reverse,
            lambda n: (n >= 1) and (n <= length_of_elements)
        )
        elements = input('').split(' ')
        elements = map(int, elements)

        queue = Queue()
        for element in elements:
            queue.enqueue(element)
        queue.reverse(elements_to_reverse)
        output = []
        for _ in range(queue.size()):
            output.append(str(queue.dequeue()))
        print(' '.join(output))
