#!/usr/bin/env python
"""
Day 01 of Advent of Code 2018.
"""
from aoc_utils import txt_to_numbers


def frequency_changes():
    data = txt_to_numbers('data/day01.txt')
    print(sum(data))


if __name__ == '__main__':
    frequency_changes()
