#! /usr/bin/env python

import unittest

from linkedlist import count_nodes_of_linked_list


class TestNode(unittest.TestCase):

    def setUp(self):
        self.data = 4
        self.node = count_nodes_of_linked_list.Node(self.data)

    def test_node_is_inialized_appropriately(self):
        self.assertEqual(self.node.data, self.data)
        self.assertIsNone(self.node.next)

    def test_node_maintains_next_attribute(self):
        next_node = count_nodes_of_linked_list.Node(self.data+1)
        self.node.next = next_node

        self.assertEqual(self.node.data, self.data)
        self.assertEqual(self.node.next.data, self.data+1)



class TestLinkedList(unittest.TestCase):


    def _adds(self, linkedlist, number_of_nodes):
        for iteration in range(number_of_nodes):
            linkedlist.add(iteration)

    def setUp(self):
        self.linkedlist = count_nodes_of_linked_list.LinkedList()

    def test_inital_data(self):
        self.assertIsNone(self.linkedlist.start)
        self.assertIsNone(self.linkedlist.head)

    def test_length_is_calculated_correct(self):
        number_of_nodes = 4
        self._adds(self.linkedlist, number_of_nodes)
        self.assertEqual(len(self.linkedlist), number_of_nodes)

    def test_add(self):
        data = 23
        _node = self.linkedlist.add(data)
        self.assertIs(self.linkedlist.start, _node)
        self.assertIs(self.linkedlist.head, _node)
        self.assertIs(self.linkedlist.start, self.linkedlist.head)
        self.assertEqual(self.linkedlist.start.data, data)
        self.assertEqual(self.linkedlist.head.data, data)
        self.assertIsNone(self.linkedlist.start.next)
        self.assertIsNone(self.linkedlist.head.next)

        data = 44
        _node = self.linkedlist.add(data)
        self.assertIs(self.linkedlist.head, _node)
        self.assertEqual(self.linkedlist.head.data, data)
        self.assertIsNone(self.linkedlist.head.next)

        self.assertIsNot(self.linkedlist.start, _node)
        self.assertIs(self.linkedlist.start.next, self.linkedlist.head)
        self.assertIs(self.linkedlist.start.next, _node)

        data = -1
        _node = self.linkedlist.add(data)
        self.assertIs(self.linkedlist.head, _node)
        self.assertIs(self.linkedlist.head.data, data)
        self.assertIsNone(self.linkedlist.head.next)

        self.assertIs(self.linkedlist.start.next.next, _node)
        self.assertIs(self.linkedlist.start.next.next, self.linkedlist.head)
        self.assertEqual(self.linkedlist.start.next.next.data, data)
