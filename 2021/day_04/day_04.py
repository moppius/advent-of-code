"""Day 4 challenge for Advent of Code 2021 - https://adventofcode.com/2021/day/4"""

from os import path
from unittest import TestCase


class ChallengeTests(TestCase):
    _test_input = """
        7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

        22 13 17 11  0
        8  2 23  4 24
        21  9 14 16  7
        6 10  3 18  5
        1 12 20 15 19

        3 15  0  2 22
        9 18 13 17  5
        19  8  7 25 23
        20 11 10 24  4
        14 21 16 12  6

        14 21 17 24  4
        10 16 15  9 19
        18  8 23 26 20
        22 11 13  6  5
        2  0 12  3  7
        """

    def test_part_1(self):
        self.assertEqual(_solve_bingo(self._test_input), 4512)

    def test_part_2(self):
        self.assertEqual(_solve_bingo_lowest(self._test_input), 1924)


class BingoCard():
    def __init__(self, string):
        lines = string.split("\n")
        self._numbers = []
        for line in lines:
            self._numbers.extend([int(num) for num in line.strip().split()])
        self._matched_numbers = [False for _ in self._numbers]

    def check_number(self, number):
        if number in self._numbers:
            index = self._numbers.index(number)
            self._matched_numbers[index] = True
        return self.has_won

    @property
    def has_won(self):
        for i in range(0, 25, 5):
            won_row = True
            for n in range(5):
                if not self._matched_numbers[i + n]:
                    won_row = False
            if won_row:
                return True

        for i in range(5):
            won_column = True
            for n in range(5):
                if not self._matched_numbers[i + n * 5]:
                    won_column = False
            if won_column:
                return True

        return False

    @property
    def sum_of_unmarked_numbers(self):
        total = 0
        i = 0
        for number in self._numbers:
            if not self._matched_numbers[i]:
                total += number
            i += 1
        return total


def _solve_bingo(input_string):
    strings = input_string.split("\n\n")
    numbers = [int(val) for val in strings.pop(0).strip().split(",")]
    bingo_cards = [BingoCard(string) for string in strings]
    winning_card = None
    last_number = None
    for number in numbers:
        if winning_card:
            break
        last_number = number
        for bingo_card in bingo_cards:
            if bingo_card.check_number(number):
                winning_card = bingo_card
            if winning_card:
                break

    if not winning_card:
        print("Failed to find a winning bingo card!")
        return 0
    else:
        return last_number * winning_card.sum_of_unmarked_numbers


def _solve_bingo_lowest(input_string):
    strings = input_string.split("\n\n")
    numbers = [int(val) for val in strings.pop(0).strip().split(",")]
    bingo_cards = [BingoCard(string) for string in strings]
    winning_cards = []
    last_number = None
    for number in numbers:
        if not bingo_cards:
            break
        last_number = number
        start = len(bingo_cards)
        for i in range(start, 0, -1):
            if bingo_cards[i - 1].check_number(number):
                winning_cards.append(bingo_cards.pop(i - 1))
            if not bingo_cards:
                break

    if bingo_cards:
        print("Failed to find a lowest scoring bingo card!")
        return 0
    else:
        return last_number * winning_cards[-1].sum_of_unmarked_numbers


def run_challenge():
    input_file_path = path.join(path.dirname(__file__), "input.txt")
    with open(input_file_path, 'r') as input_file:
        input_values = input_file.read()

    part_one_solution = _solve_bingo(input_values)
    print(f"\tPart one solution: {part_one_solution}")

    part_two_solution = _solve_bingo_lowest(input_values)
    print(f"\tPart two solution: {part_two_solution}")
