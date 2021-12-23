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

    def test_part_2(self):
        self.assertEqual(_solve_life_support(self.test_input), 230)


def _count_ones(input_values):
    length = len(input_values[0])
    count_ones = [0 for _ in range(length)]
    for val in input_values:
        for i in range(length):
            if val[i] == "1":
                count_ones[i] += 1
    return count_ones


def _solve_power_consumption(input_values):
    count_ones = _count_ones(input_values)
    half_total = len(input_values) / 2
    gamma_rate = ""
    epsilon_rate = ""
    length = len(input_values[0])
    for i in range(length):
        gamma_rate += "0" if count_ones[i] >= half_total else "1"
        epsilon_rate += "0" if count_ones[i] < half_total else "1"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def _filter_list(input_values, most_common=True):
    filtered_list = []
    filtered_list.extend(input_values)
    length = len(filtered_list[0])
    for i in range(length):
        half_total = len(filtered_list) / 2
        count_ones = _count_ones(filtered_list)
        keep_val = "1" if count_ones[i] >= half_total else "0"
        if not most_common:
            keep_val = "1" if count_ones[i] < half_total else "0"
        start = len(filtered_list) - 1
        for k in range(start, -1, -1):
            if len(filtered_list) == 1:
                break
            if filtered_list[k][i] != keep_val:
                filtered_list.pop(k)
        if len(filtered_list) == 1:
            break
    return int(filtered_list[0], 2)


def _solve_life_support(input_values):
    oxygen_generator = _filter_list(input_values, most_common=True)
    co2_scrubber = _filter_list(input_values, most_common=False)
    return oxygen_generator * co2_scrubber


def run_challenge():
    input_file_path = path.join(path.dirname(__file__), "input.txt")
    with open(input_file_path, 'r') as input_file:
        input_values = [val.strip() for val in input_file]

    part_one_solution = _solve_power_consumption(input_values)
    print(f"\tPart one solution: {part_one_solution}")

    part_two_solution = _solve_life_support(input_values)
    print(f"\tPart two solution: {part_two_solution}")
