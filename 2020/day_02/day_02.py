"""Day 2 challenge for Advent of Code 2020 - https://adventofcode.com/2020/day/2"""

from os import path
from unittest import TestCase


class ChallengeTests(TestCase):
    test_input = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc"
    ]

    def test_part_1(self):
        self.assertEqual(_num_valid_passwords(self.test_input, _parse_password), 2)

    def test_part_2(self):
        self.assertEqual(_num_valid_passwords(self.test_input, _parse_password_part_2), 1)


def _parse_password(line):
    tokens = line.split(" ")
    min_max = tokens[0].split("-")
    num_letters = tokens[2].count(tokens[1][0])
    return num_letters >= int(min_max[0]) and num_letters <= int(min_max[1])


def _parse_password_part_2(line):
    tokens = line.split(" ")
    nums = tokens[0].split("-")
    p1 = int(nums[0]) - 1
    p2 = int(nums[1]) - 1
    letter = tokens[1][0]
    pw = tokens[2]
    return not (pw[p1] == letter and pw[p2] == letter) and not (pw[p1] != letter and pw[p2] != letter)


def _num_valid_passwords(input_values, function):
    count = 0
    for line in input_values:
        if function(line):
            count += 1
    return count


def run_challenge():
    input_file_path = path.join(path.dirname(__file__), "input.txt")
    with open(input_file_path, 'r') as input_file:
        input_values = [val for val in input_file]

    part_one_solution = _num_valid_passwords(input_values, _parse_password)
    print(f"\tPart one solution: {part_one_solution}")

    part_two_solution = _num_valid_passwords(input_values, _parse_password_part_2)
    print(f"\tPart two solution: {part_two_solution}")
