"""
utility functions for Advent of Code 2018.
"""
from typing import List


def txt_to_numbers(fname: str) -> List[int]:
    """read `fname` and return a list of numbers"""
    with open(fname, 'rt') as f:
        data = [int(number) for number in f]

    return data
