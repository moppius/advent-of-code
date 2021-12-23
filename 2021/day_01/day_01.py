"""Day 1 challenge for Advent of Code 2021 - https://adventofcode.com/2021/day/1"""

from os import path
from unittest import TestCase


class ChallengeTests(TestCase):
    test_input = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]

    def test_part_1(self):
        self.assertEqual(_solve_depth(self.test_input), 7)

    def test_part_2(self):
        self.assertEqual(_solve_depth_averaged(self.test_input), 5)


def _solve_depth(input_values):
    count = 0
    prev_depth = None
    for depth in input_values:
        if prev_depth is not None:
            if depth - prev_depth > 0:
                count += 1
        prev_depth = depth
    return count


def _solve_depth_averaged(input_values):
    count = 0
    depths = []
    prev_depth_sum = None
    for depth in input_values:
        depths.insert(0, depth)
        depth_sum = 0
        for depth_val in depths:
            depth_sum += depth_val
        if len(depths) == 3:
            if prev_depth_sum is not None:
                if depth_sum > prev_depth_sum:
                    count += 1
            prev_depth_sum = depth_sum
            depths.pop()
    return count


def run_challenge():
    input_file_path = path.join(path.dirname(__file__), "input.txt")
    with open(input_file_path, 'r') as input_file:
        input_values = [int(val) for val in input_file]

    part_one_solution = _solve_depth(input_values)
    print(f"\tPart one solution: {part_one_solution}")

    part_two_solution = _solve_depth_averaged(input_values)
    print(f"\tPart two solution: {part_two_solution}")
