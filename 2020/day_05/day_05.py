"""Day 5 challenge for Advent of Code 2020 - https://adventofcode.com/2020/day/5"""

from os import path
from unittest import TestCase


class ChallengeTests(TestCase):
    test_input = {
        "BFFFBBFRRR": [70, 7, 567],
        "FFFBBBFRRR": [14, 7, 119],
        "BBFFBBFRLL": [102, 4, 820]
    }

    def test_part_1(self):
        for pass_id in self.test_input:
            results = self.test_input[pass_id]
            boarding_pass = BoardingPass(pass_id)
            self.assertEqual(boarding_pass.row, results[0])
            self.assertEqual(boarding_pass.column, results[1])
            self.assertEqual(boarding_pass.seat_id, results[2])


class BoardingPass:
    def __init__(self, pass_id):
        self.id = pass_id

    @property
    def row(self):
        return self._bsp(self.id[:7], 'B')

    @property
    def column(self):
        return self._bsp(self.id[-3:], 'R')

    @property
    def seat_id(self):
        return self.row * 8 + self.column

    @staticmethod
    def _bsp(string, back_char):
        result = 0
        step = pow(2, len(string) - 1)
        for char in string:
            if char is back_char:
                result += step
            step /= 2
        return int(result)


def _get_highest_seat_id(pass_ids):
    highest_id = 0
    for pass_id in pass_ids:
        boarding_pass = BoardingPass(pass_id)
        if boarding_pass.seat_id > highest_id:
            highest_id = boarding_pass.seat_id
    return highest_id


def run_challenge():
    input_file_path = path.join(path.dirname(__file__), "input.txt")
    with open(input_file_path, 'r') as input_file:
        pass_ids = input_file.readlines()

    part_one_solution = _get_highest_seat_id(pass_ids)
    print(f"\tPart one solution: {part_one_solution}")
