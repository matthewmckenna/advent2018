#!/usr/bin/env python
"""
Day 02 of Advent of Code 2018.
"""
from collections import Counter
import itertools
from typing import Iterator, Tuple

from aoc_utils import read_strings_from_file


def count_valid_strings(strings: Iterator[str]) -> int:
    """count strings which contain two or three of the same letters"""
    # initialise a counter for strings with letters occuring
    # two or three times
    c = Counter({'two': 0, 'three': 0})

    for s in strings:
        counts = set(Counter(s).values())
        if 2 in counts:
            c['two'] += 1
        if 3 in counts:
            c['three'] += 1

    return c['two'] * c['three']


def find_common_letters(strings: Iterator[str]) -> str:
    """find the strings which differ by a single character"""
    # initialise s to a blank string
    s = ''

    for pair in itertools.combinations(strings, 2):
        diffs = count_differences(pair)

        if diffs == 1:
            s = ''.join(common_letters(pair))

    return s


def count_differences(pair: Tuple[str, ...]) -> int:
    """count the differences between a pair of strings"""
    diffs = 0
    for l1, l2 in zip(*pair):
        if l1 != l2:
            diffs += 1
    return diffs


def common_letters(pair: Tuple[str, ...]) -> Iterator[str]:
    """construct a string from the common letters in a tuple"""
    for l1, l2 in zip(*pair):
        if l1 == l2:
            yield l1


if __name__ == '__main__':
    strings = read_strings_from_file('data/day02.txt')
    checksum = count_valid_strings(strings)
    print(f'checksum is: {checksum}')

    # read the data again, as the iterator is exhausted above
    strings = read_strings_from_file('data/day02.txt')
    letters = find_common_letters(strings)
    print(f'common letters between IDs: {letters}')
