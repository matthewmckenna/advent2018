#!/usr/bin/env python
"""
Day 01 of Advent of Code 2018.
"""
from itertools import accumulate, chain, repeat
from typing import List

from aoc_utils import comma_separated_str_to_int_iterator, txt_to_numbers


def frequency_changes(fname: str) -> int:
    data = txt_to_numbers(fname)
    return sum(data)


def repeat_frequencies(data: List[int]) -> int:
    seen = set()
    # we start off at zero
    seen.add(0)

    for frequency in accumulate(chain.from_iterable(repeat(data))):
        if frequency in seen:
            break
        seen.add(frequency)

    return frequency


if __name__ == '__main__':
    fname = 'data/day01.txt'

    final_frequency = frequency_changes(fname)
    print(f'final frequency: {final_frequency}')

    # test inputs
    inputs_expected = [
        ('+1, -1', 0),
        ('+3, +3, +4, -2, -4', 10),
        ('-6, +3, +8, +5, -6', 5),
        ('+7, +7, -2, -7, -4', 14),
    ]
    for input_, expected in inputs_expected:
        data = list(comma_separated_str_to_int_iterator(input_))
        first_repeat = repeat_frequencies(data)
        assert first_repeat == expected

    data = txt_to_numbers(fname)
    first_repeat = repeat_frequencies(data)
    print(f'first repeated frequency: {first_repeat}')
