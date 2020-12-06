"""Day 6 challenge for Advent of Code 2020 - https://adventofcode.com/2020/day/6"""

from os import path
from unittest import TestCase


class ChallengeTests(TestCase):
    def test_part_1(self):
        self.assertEqual(_sum_group_answers("test_input.txt"), 11)


def _sum_group_answers(input_filename):
    input_file_path = path.join(path.dirname(__file__), input_filename)
    with open(input_file_path, 'r') as input_file:
        responses = input_file.read().split('\n\n')
    result = 0
    for response in responses:
        result += _sum_group(response)
    return result


def _sum_group(response):
    result = ""
    lines = response.split('\n')
    for line in lines:
        for char in line:
            if char not in result:
                result += char
    return len(result)


def run_challenge():
    part_one_solution = _sum_group_answers("input.txt")
    print(f"\tPart one solution: {part_one_solution}")
