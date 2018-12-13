"""
utility functions for Advent of Code 2018.
"""
from typing import Iterator, List


def txt_to_numbers(fname: str) -> List[int]:
    """read `fname` and return a list of numbers"""
    with open(fname, 'rt') as f:
        data = [int(number) for number in f]

    return data


def comma_separated_str_to_int_iterator(s: str) -> Iterator[int]:
    """turn a comma separated string of numbers into an iterable of ints"""
    for number in s.replace(',', '').split():
        yield int(number)


def read_strings_from_file(fname: str) -> Iterator[str]:
    """read a file and yield strings from it"""
    with open(fname, 'rt') as f:
        for line in f:
            yield line.strip()
