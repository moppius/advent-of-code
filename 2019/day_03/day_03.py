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


class WireSection():
    """Class that represents a section of wire."""

    def __init__(self, start, direction, length):
        self.start = start.copy()
        if direction == "U":
            start[1] += length
        elif direction == "D":
            start[1] -= length
        elif direction == "L":
            start[0] -= length
        elif direction == "R":
            start[0] += length
        self.end = start.copy()

        # Reverse order
        if direction in ["D", "L"]:
            temp = self.start
            self.start = self.end
            self.end = temp

    def __repr__(self):
        return f"Wire section starting at {self.start} and ending at {self.end}"


class WireIntersector():
    """Class for finding closest Manhattan distance of crossing wires from a common center."""

    def __init__(self, wires):
        self.wire1 = self._process_wire(wires[0])
        self.wire2 = self._process_wire(wires[1])

    @staticmethod
    def _process_wire(wire):
        result = {"horizontal": [], "vertical": []}
        start = [0, 0]
        for section in wire:
            direction = section[0]
            if direction not in ["U", "D", "L", "R"]:
                print(f"Error: Invalid direction '{direction}'")
                return None
            length = int(section[1:])
            angle = "vertical" if direction in ["U", "D"] else "horizontal"
            result[angle].append(WireSection(start, direction, length))
        return result

    def get_nearest_result(self):
        """Return the nearest crossing result's Manhattan distance from center."""
        crossings = []
        for wires in [(self.wire1, self.wire2), (self.wire2, self.wire1)]:
            for horizontal in wires[0]["horizontal"]:
                for vertical in wires[1]["vertical"]:
                    test1 = vertical.start[0] > horizontal.start[0] and vertical.end[0] < horizontal.end[0]
                    test2 = vertical.start[1] < horizontal.start[1] and vertical.end[1] > horizontal.start[1]
                    if test1 and test2:
                        crossings.append([abs(vertical.start[0]), abs(horizontal.start[1])])
        shortest = None
        for crossing in crossings:
            distance = crossing[0] + crossing[1]
            if shortest is None or distance < shortest:
                shortest = distance
        return shortest


def run_challenge():
    """Run the challenge."""

    part_one_solution = WireIntersector(WIRE_PATH).get_nearest_result()
    print(f"\tPart one solution: {part_one_solution}")
