#! /usr/bin/env python
"""
Problem

    Given a singly linked list. The task is to find the length of linked list,
    where length is defined as number of nodes in the linked list.

Input

    First line of input contains number of testcases T. For each testcase,
    first line of input contains number of nodes N, to be inserted into the
    linked list and next line contains data of N nodes.

Output

    There will be a single line of output for each testcase, which contains
    length of the linked list.

Constraints

    1 <= T <= 30
    1 <= N <= 100
    1 <= value <= 10^3

User task

    Your task is to complete the given function `getCount()`, which takes head
    reference as argument and should return the length of the linked list.

Example

    Input

        2
        5
        12345
        7
        2467510

    Output

        5
        7
"""
class LinkedList:

    def __init__(self):
        self.start = None
        self.head = None
        self._length = 0

    def add(self, data):
        node = Node(data)
        self._length += 1

        if self.start is None:
            self.start = node
            self.head = node
        else:
            self.head.next = node
            self.head = node
        return node

    def __len__(self):
        return self._length


class Node:
    """Linedlist Node"""

    start = None

    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    number_of_testcases = int(input(''))

    for _ in range(number_of_testcases):
        linkedlist = LinkedList()
        number_of_nodes = input('')
        node_data = input('').split(' ')
        for data in node_data:
            linkedlist.add(data)
        print(len(linkedlist))
