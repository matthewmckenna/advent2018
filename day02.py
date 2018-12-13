#!/usr/bin/env python
"""
Day 02 of Advent of Code 2018.
"""
from collections import Counter
from typing import Iterator

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


if __name__ == '__main__':
    strings = read_strings_from_file('data/day02.txt')
    checksum = count_valid_strings(strings)
    print(f'checksum is: {checksum}')
