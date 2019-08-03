#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from trie import insert_and_search


class TestNode:

    def test_init(self):
        node = insert_and_search.Node()
        self.assertTrue(
            hasattr(node, "children")
        )
        self.assertDictEqual(
            self.node.children, {}
        )


class TestTrie:

    def setUp(self):
        self.trie = insert_and_search.Trie()

    def test_insert(self):
        pass


class TestIsWordPresent(unittest.TestCase):

    def test_is_word_present(self):
        sample_inputs_and_expected_answer = (
            ("This is a word present in all direction", "a", True),
            ("", "a", False),
            ("", "", False),
            ("Ahmed shah is good person", "", False),
            ("text is nice thing", "is", True),
            ("the a there answer any by bye their", "the", True),
            ("the", "the", True),
            ("Was there anything related to me?", "was", False),
        )

        for text, word, expected_answer in sample_inputs_and_expected_answer:
            self.assertEqual(
                insert_and_search.is_word_present(text, word),
                expected_answer
            )
