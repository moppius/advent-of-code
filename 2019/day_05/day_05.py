"""Day 5 challenge for Advent of Code 2019 - https://adventofcode.com/2019/day/5"""

from os import path
from unittest import TestCase


INPUT_FILE = path.join(path.dirname(__file__), "input.txt")
with open(INPUT_FILE, 'r') as fp:
    OPCODES = [int(op) for op in fp.readline().split(",")]


class ChallengeTests(TestCase):
    """Tests for day 2."""

    def test_part1(self):
        """Test part one example values."""

        tests = [
            ([3, 0, 4, 0, 99], [0, 0, 4, 0, 99]),
            ([1101, 100, -1, 4, 0], [1101, 100, -1, 4, 99]),
            ([1002, 4, 3, 4, 33], [1002, 4, 3, 4, 99]),
        ]

        for test in tests:
            self.assertEqual(_get_opcode_result(test[0])[0], test[1])


def _get_opcode_result(opcodes, input_val=0):
    result = opcodes.copy()
    i = 0
    output_val = 0
    while i < len(result):
        opcode = result[i]
        modes = []
        if opcode > 99:
            op_str = str(opcode)
            modes = [int(op_str[-int(o) - 1]) for o in range(2, len(op_str))]
            opcode = int(op_str[-2:])
        for m in range(1, 4):
            if len(modes) < m:
                modes.append(0)

        jump = 2 if opcode in [3, 4] else 4

        if opcode == 1:
            val_a = result[result[i+1]] if modes[0] == 0 else result[i+1]
            val_b = result[result[i+2]] if modes[1] == 0 else result[i+2]
            result[result[i+3]] = val_a + val_b
        elif opcode == 2:
            val_a = result[result[i+1]] if modes[0] == 0 else result[i+1]
            val_b = result[result[i+2]] if modes[1] == 0 else result[i+2]
            result[result[i+3]] = val_a * val_b
        elif opcode == 3:
            index = result[i+1]
            result[index] = input_val
        elif opcode == 4:
            output_val = result[result[i+1]] if modes[0] == 0 else result[i+1]
        elif opcode == 99:
            break
        else:
            print(f"Error: Encountered unexpected opcode {opcode}")
            return None
        i += jump
    return result, output_val


def _run_diagnostic(input_val):
    return _get_opcode_result(OPCODES, input_val)


def run_challenge():
    """Run the challenge."""

    part_one_solution = _run_diagnostic(1)[1]
    print(f"\tPart one solution: {part_one_solution}")
