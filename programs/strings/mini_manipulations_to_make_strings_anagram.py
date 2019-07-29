#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Problem

    Given two strings in lowercase, your task is to find minimum number of
    manipulations required to make two strings anagram without deleting any
    character. If two strings contains same data set in any order than strings
    are called Anagrams.

Input

    The first line of input contains an integer 'T' denoting the number of test
    cases. For each test case, first line of each test case contains an integer
    'N', denoting the size of the string, next line contains 'two strings' to
    make them anagrams.

Output

    Output the minimum number of manipulations required to make two strings
    anagram. If two strings are anagram return 0.

Example 1

    Input

        s1 = "aba"
        s2 = "baa"

    Output

        0

    Explanation

        Both string contains identical characters.

Example 2

    Input

        s1 = "ddck"
        s2 = "cedk"

    Output

        2

    Explanation

        Here, we need to change two characters in either of the strings to make
        them identical. We can change 'd' and 'f' in s1 or 'e' and 'k' in s2.

Constraints

    * 1 <= T <= 100
    * 1 <= length of string <= 10^3
"""
from collections import defaultdict


class Bin:

    def __init__(self):
        self._character_table = defaultdict(int)

    def add(self, character: str) -> None:
        """Adds a character to a bin"""
        self._character_table[character] += 1

    def remove(self, character: str) -> None:
        """Takes given character out from bin.

        If given character is not present, it will raise a KeyError.
        """
        if character not in self._character_table:
            raise KeyError(f"Given {character} is not present in Bin.")
        self._character_table[character] -= 1
        if self._character_table[character] == 0:
            del self._character_table[character]

    def __len__(self) -> int:
        length = 0
        for key, value in self._character_table.items():
            length += value
        return length


def calculate_different_characters(sequence_1: str, sequence_2: str) -> int:
    """Calculate different characters

    This method calculates number of characters that can be changed at any
    string (not deleted) to make both strings one of an anagram sequences of
    each other.

    This function expects that length of given strings are same. If length of
    two string is not similar then this will raise a `ValueError` exception.

    This method also assumes that characters in given string are only in small
    case.

    Example

        >>>calculate_different_characters("abwwcq", "aeevqq")
        >>>4

    """
    _bin = Bin()
    different_characters = 0
    for character in sequence_1:
        _bin.add(character)
    for character in sequence_2:
        try:
            _bin.remove(character)
        except KeyError:
            different_characters += 1
    return different_characters