"""Day 2 challenge for Advent of Code 2019 - https://adventofcode.com/2019/day/2"""

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
            ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
            ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
            ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
            ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
        ]
        for test in tests:
            self.assertEqual(_get_opcode_result(test[0]), test[1])


def _get_opcode_result(opcodes):
    result = opcodes.copy()
    for i in range(0, len(result), 4):
        opcode = result[i]
        if opcode == 1:
            result[result[i+3]] = result[result[i+1]] + result[result[i+2]]
        elif opcode == 2:
            result[result[i+3]] = result[result[i+1]] * result[result[i+2]]
        elif opcode == 99:
            break
        else:
            print(f"Error: Encountered unexpected opcode {opcodes[i]}")
            return None
    return result


def _find_output_from_values(noun, verb):
    opcodes = OPCODES.copy()
    opcodes[1] = noun
    opcodes[2] = verb
    return _get_opcode_result(opcodes)


def _brute_force_find():
    required_result = 19690720
    for noun in range(0, 99):
        for verb in range(0, 99):
            if _find_output_from_values(noun, verb)[0] == required_result:
                #print(f"Found required result {required_result} where noun = {noun}, verb = {verb}")
                return 100 * noun + verb
    print(f"Error: Failed to find required result: {required_result}")
    return None


def run_challenge():
    """Run the challenge."""

    part_one_solution = _find_output_from_values(12, 2)[0]
    print(f"\tPart one solution: {part_one_solution}")

    part_two_solution = _brute_force_find()
    print(f"\tPart two solution: {part_two_solution}")
