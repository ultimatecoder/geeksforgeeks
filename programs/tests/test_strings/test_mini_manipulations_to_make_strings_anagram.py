#! /usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase

from strings.mini_manipulations_to_make_strings_anagram import (
    calculate_different_characters
)


class TestMiniManipulationOfStrings(TestCase):

    def test_calculate_different_characters_with_valid_inputs(self):
        sample_inputs_and_expected_answers = (
            ("aba", "baa", 0),
            ("ddck", "cedk", 1),
            ("cat", "tab", 1),
            ("", "", 0)
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
