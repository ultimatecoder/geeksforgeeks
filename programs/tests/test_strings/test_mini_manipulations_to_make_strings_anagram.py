#! /usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase

from strings.mini_manipulations_to_make_strings_anagram import (
    calculate_different_characters, Bin
)


class TestMiniManipulationOfStrings(TestCase):

    def test_calculate_different_characters_with_valid_inputs(self):
        sample_inputs_and_expected_answers = (
            ("aba", "baa", 0),
            ("ddck", "cedk", 1),
            ("cat", "tab", 1),
            ("", "", 0),
            ("cccab", "absss", 3)
        )
        for sequence_1, sequence_2, expected_answer in (
            sample_inputs_and_expected_answers
        ):
            with self.subTest(
                sequence_1=sequence_1, sequence_2=sequence_2,
                expected_answer=expected_answer
            ):
                result = calculate_different_characters(
                    sequence_1, sequence_2
                )
                self.assertEqual(result, expected_answer)


class TestBin(TestCase):

    def setUp(self):
        self.bin = Bin()

    def test_add(self):
        sample_characters = [
            'a', 'b', 'a', 'c', 'd', 'q', 'r'
        ]
        for character in sample_characters:
            with self.subTest(character=character):
                self.bin.add(character)
        self.assertEqual(len(self.bin), len(sample_characters))

    def test_remove(self):
        sample_characters = [
            'b', 'c', 'a', 'b', 'a', 'c', 'd', 'q', 'r'
        ]
        for character in sample_characters:
            with self.subTest(character=character):
                self.bin.add(character)

        for character in sample_characters:
            with self.subTest(character=character):
                self.bin.remove(character)
        self.assertEqual(len(self.bin), 0)
