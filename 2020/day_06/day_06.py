"""Day 6 challenge for Advent of Code 2020 - https://adventofcode.com/2020/day/6"""

from os import path
from unittest import TestCase


class ChallengeTests(TestCase):
    def test_part_1(self):
        self.assertEqual(_sum_group_answers("test_input.txt"), 11)

    def test_part_2(self):
        self.assertEqual(_sum_group_answers("test_input.txt", part=2), 6)


def _sum_group_answers(input_filename, part=1):
    input_file_path = path.join(path.dirname(__file__), input_filename)
    with open(input_file_path, 'r') as input_file:
        responses = input_file.read().split('\n\n')
    result = 0
    for response in responses:
        if part == 2:
            result += _sum_group_part_2(response)
        else:
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


def _sum_group_part_2(response):
    result = 0
    lines = response.strip().split('\n')
    num_guests = len(lines)
    done_chars = []
    stripped_response = "".join(response.split())
    for char in stripped_response:
        if char not in done_chars and response.count(char) == num_guests:
            result += 1
            done_chars.append(char)
    return result


def run_challenge():
    part_one_solution = _sum_group_answers("input.txt")
    print(f"\tPart one solution: {part_one_solution}")

    part_two_solution = _sum_group_answers("input.txt", part=2)
    print(f"\tPart two solution: {part_two_solution}")
