"""Day 2 challenge for Advent of Code 2021 - https://adventofcode.com/2021/day/2"""

from os import path
from unittest import TestCase


class ChallengeTests(TestCase):
    test_input = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]

    def test_part_1(self):
        self.assertEqual(_solve_movement(self.test_input), 150)

    def test_part_2(self):
        self.assertEqual(_solve_movement(self.test_input, with_aim=True), 900)


def _solve_movement(input_values, with_aim=False):
    horizontal = 0
    depth = 0
    aim = 0
    inputs = [val.split() for val in input_values]
    for direction, amount in inputs:
        amount = int(amount)
        if direction == "forward":
            horizontal += amount
            if with_aim:
                depth += amount * aim
        elif direction == "up":
            if not with_aim:
                depth -= amount
            aim -= amount
        elif direction == "down":
            if not with_aim:
                depth += amount
            aim += amount
        else:
            print(f"Unexpected direction '{direction}'")
    return horizontal * depth


def run_challenge():
    input_file_path = path.join(path.dirname(__file__), "input.txt")
    with open(input_file_path, 'r') as input_file:
        input_values = [val for val in input_file]

    part_one_solution = _solve_movement(input_values)
    print(f"\tPart one solution: {part_one_solution}")

    part_two_solution = _solve_movement(input_values, with_aim=True)
    print(f"\tPart two solution: {part_two_solution}")
