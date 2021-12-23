"""Day 3 challenge for Advent of Code 2021 - https://adventofcode.com/2021/day/3"""

from os import path
from unittest import TestCase


class ChallengeTests(TestCase):
    test_input = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]

    def test_part_1(self):
        self.assertEqual(_solve_power_consumption(self.test_input), 198)


def _solve_power_consumption(input_values):
    length = len(input_values[0])
    count_ones = [0 for _ in range(length)]
    print(count_ones)
    for val in input_values:
        for i in range(length):
            if val[i] == "1":
                count_ones[i] += 1

    half_total = len(input_values) / 2
    gamma_rate = ""
    epsilon_rate = ""
    for i in range(length):
        gamma_rate += "0" if count_ones[i] >= half_total else "1"
        epsilon_rate += "0" if count_ones[i] < half_total else "1"
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def run_challenge():
    input_file_path = path.join(path.dirname(__file__), "input.txt")
    with open(input_file_path, 'r') as input_file:
        input_values = [val.strip() for val in input_file]

    part_one_solution = _solve_power_consumption(input_values)
    print(f"\tPart one solution: {part_one_solution}")
