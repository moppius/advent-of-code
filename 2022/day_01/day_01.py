"""Day 1 challenge for Advent of Code 2022 - https://adventofcode.com/2022/day/1"""

from os import path
from unittest import TestCase


class ChallengeTests(TestCase):
    def test_part_1(self):
        self.assertEqual(max(_get_input("test_input.txt")), 24000)

    def test_part_2(self):
        self.assertEqual(_get_top_sum(_get_input("test_input.txt")), 45000)



def _get_input(file_name="input.txt"):
    result = []
    input_file_path = path.join(path.dirname(__file__), file_name)
    with open(input_file_path) as input_file:
        index = 0
        for line in input_file.readlines():
            line = line.strip()
            if len(result) == index:
                result.append(int(line))
            elif not line:
                index += 1
            else:
                result[index] += int(line)
    return result


def _get_top_sum(values, top=3):
    result = 0
    for i in range(top):
        top_val = max(values)
        result += top_val
        values.remove(top_val)
    return result


def run_challenge():
    part_one_solution = max(_get_input())
    print(f"\tPart one solution: {part_one_solution}")

    part_one_solution = _get_top_sum(_get_input())
    print(f"\tPart one solution: {part_one_solution}")
