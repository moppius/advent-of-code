"""Day 3 challenge for Advent of Code 2019 - https://adventofcode.com/2019/day/3"""

from os import path
from unittest import TestCase


INPUT_FILE = path.join(path.dirname(__file__), "input.txt")
with open(INPUT_FILE, 'r') as fp:
    WIRE_PATH = [wire for wire in [line.strip().split(",") for line in fp]]


class ChallengeTests(TestCase):
    """Tests for day 2."""

    def test_part1(self):
        """Test part one example values."""
        tests = [
            ([
                ["R8", "U5", "L5", "D3"],
                ["U7", "R6", "D4", "L4"]
            ], 6),
            ([
                ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
                ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
            ], 159),
            ([
                ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"],
                ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]
            ], 135)
        ]
        for test in tests:
            self.assertEqual(WireIntersector(test[0]).get_nearest_result(), test[1])


class WireIntersector():
    """Class for finding closest Manhattan distance of crossing wires from a common center."""

    def __init__(self, wires):
        pass

    def get_nearest_result(self):
        """Return the nearest crossing result's Manhattan distance from center."""
        return 0


def run_challenge():
    """Run the challenge."""

    part_one_solution = WireIntersector(WIRE_PATH).get_nearest_result()
    print(f"\tPart one solution: {part_one_solution}")
