"""Day 3 challenge for Advent of Code 2020 - https://adventofcode.com/2020/day/3"""

from os import path
from unittest import TestCase


_STEPS = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]


class ChallengeTests(TestCase):
    test_input = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#"
    ]

    def test_part_1(self):
        self.assertEqual(_count_trees(self.test_input, 3, 1), 7)

    def test_part_2(self):
        self.assertEqual(_count_trees_part2(self.test_input, _STEPS), 336)


def _count_trees_part2(lines, steps):
    result = None
    for step in steps:
        num = _count_trees(lines, step[0], step[1])
        if not result:
            result = num
        else:
            result *= num
    return result


def _count_trees(lines, right, down):
    if not down or down < 1:
        return 0
    row = 0
    column = 0
    num_trees = 0
    max_rows = len(lines) - 1
    while row < max_rows:
        row += down
        column += right
        mod_column = column % len(lines[row])
        if lines[row][mod_column] == "#":
            num_trees += 1
    return num_trees


def run_challenge():
    input_file_path = path.join(path.dirname(__file__), "input.txt")
    with open(input_file_path, 'r') as input_file:
        input_values = [val.strip() for val in input_file]

    part_one_solution = _count_trees(input_values, 3, 1)
    print(f"\tPart one solution: {part_one_solution}")

    part_two_solution = _count_trees_part2(input_values, _STEPS)
    print(f"\tPart two solution: {part_two_solution}")
