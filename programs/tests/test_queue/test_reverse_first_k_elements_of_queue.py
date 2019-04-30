#! /usr/bin/env python

import unittest

from queue import reverse_first_k_elements_of_queue


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = reverse_first_k_elements_of_queue.Queue()

    def test_enqueue_with_one_element(self):
        element = 4
        self.queue.enqueue(element)
        self.assertEqual(self.queue.front(), element)
        self.assertEqual(self.queue.size(), 1)

    def test_enqueue_with_multiple_elements(self):
        elements = [1, 4, 5]
        for element in elements:
            with self.subTest(element=element):
                self.queue.enqueue(element)

        for element in elements:
            with self.subTest(element=element):
                self.assertEqual(self.queue.dequeue(), element)

    def test_size(self):
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size(), 1)

        self.queue.enqueue(4)
        self.assertEqual(self.queue.size(), 2)

        self.queue.enqueue(6)
        self.assertEqual(self.queue.size(), 3)

        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 2)

        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 1)

    def test_dequeue_with_single_element(self):
        element = 4
        self.queue.enqueue(element)
        self.assertEqual(self.queue.dequeue(), element)

    def test_dequeue_with_multiple_elements(self):
        elements = [1, 3, 5]

        for element in elements:
            self.queue.enqueue(element)

        for element in elements:
            self.assertEqual(self.queue.dequeue(), element)

    def test_front_with_single_element(self):
        element = 4
        self.queue.enqueue(element)

        self.assertEqual(self.queue.front(), element)

    def test_front_with_multiple_elements(self):
        elements = [1, 3, 4]

        for element in elements:
            self.queue.enqueue(element)
            self.assertEqual(self.queue.front(), elements[0])

    def test_reverse(self):
        elements = list(range(1, 6))
        expected_elements = elements[2::-1] + elements[3:]
        for element in elements:
            with self.subTest(element=element):
                self.queue.enqueue(element)

        self.queue.reverse(3)
        for expected_element in expected_elements:
            with self.subTest(element=element):
                self.assertEqual(
                    self.queue.dequeue(), expected_element
                )
