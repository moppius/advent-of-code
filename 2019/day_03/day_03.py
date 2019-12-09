"""Day 3 challenge for Advent of Code 2019 - https://adventofcode.com/2019/day/3"""

from os import path
from unittest import TestCase


INPUT_FILE = path.join(path.dirname(__file__), "input.txt")
with open(INPUT_FILE, 'r') as fp:
    WIRE_PATH = [wire for wire in [line.strip().split(",") for line in fp]]


class ChallengeTests(TestCase):
    """Tests for day 3."""

    def test_part1_and_part2(self):
        """Test part one and part two example values."""
        tests = [
            ([
                ["R8", "U5", "L5", "D3"],
                ["U7", "R6", "D4", "L4"]
            ], 6, 30),
            ([
                ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
                ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
            ], 159, 610),
            ([
                ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"],
                ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]
            ], 135, 410)
        ]
        for test in tests:
            manhattan_distance, best_step = WireIntersector(test[0]).get_nearest_result()
            self.assertEqual(manhattan_distance, test[1])
            self.assertEqual(best_step, test[2])


class WireSection():
    """Class that represents a section of wire."""

    def __init__(self, start, direction, length):
        self.direction = direction
        self.length = length
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
        result = []
        start = [0, 0]
        for section in wire:
            direction = section[0]
            if direction not in ["U", "D", "L", "R"]:
                print(f"Error: Invalid direction '{direction}'")
                return None
            length = int(section[1:])
            result.append(WireSection(start, direction, length))
        return result

    @staticmethod
    def _get_best_step(wire1, wire2, crossing):
        result = 0
        for wire in [wire1, wire2]:
            for section in wire:
                crosses_horizontally = (
                    section.start[0] == section.end[0]
                    and section.start[0] == crossing[0]
                    and crossing[1] in range(section.start[1], section.end[1])
                )
                crosses_vertically = (
                    section.start[1] == section.end[1]
                    and section.start[1] == crossing[1]
                    and crossing[0] in range(section.start[0], section.end[0])
                )
                if crosses_horizontally:
                    if section.direction == "U":
                        result += abs(crossing[1] - section.start[1])
                    else:
                        result += abs(section.end[1] - crossing[1])
                    break
                elif crosses_vertically:
                    if section.direction == "R":
                        result += abs(crossing[0] - section.start[0])
                    else:
                        result += abs(section.end[0] - crossing[0])
                    break
                result += section.length
        return result

    def get_nearest_result(self):
        """Return the nearest crossing result's Manhattan distance from center."""
        crossings = []
        best_step = None
        for wire1_section in self.wire1:
            for wire2_section in self.wire2:
                test1 = wire1_section.start[0] > wire2_section.start[0] and wire1_section.end[0] < wire2_section.end[0]
                test2 = wire1_section.start[1] < wire2_section.start[1] and wire1_section.end[1] > wire2_section.start[1]
                if test1 and test2:
                    crossing = [wire1_section.start[0], wire2_section.start[1]]
                    crossings.append(crossing)
                    this_step = self._get_best_step(self.wire1, self.wire2, crossing)
                    if best_step is None or this_step < best_step:
                        best_step = this_step

                test3 = wire2_section.start[0] > wire1_section.start[0] and wire2_section.end[0] < wire1_section.end[0]
                test4 = wire2_section.start[1] < wire1_section.start[1] and wire2_section.end[1] > wire1_section.start[1]
                if test3 and test4:
                    crossing = [wire2_section.start[0], wire1_section.start[1]]
                    crossings.append(crossing)
                    this_step = self._get_best_step(self.wire2, self.wire1, crossing)
                    if best_step is None or this_step < best_step:
                        best_step = this_step

        manhattan_distance = None
        for crossing in crossings:
            distance = abs(crossing[0]) + abs(crossing[1])
            if manhattan_distance is None or distance < manhattan_distance:
                manhattan_distance = distance
        return manhattan_distance, best_step


def run_challenge():
    """Run the challenge."""

    part_one_solution = WireIntersector(WIRE_PATH).get_nearest_result()
    print(f"\tPart one solution: {part_one_solution}")
