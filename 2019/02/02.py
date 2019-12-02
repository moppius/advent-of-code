"""Day 2 challenge for Advent of Code 2019 - https://adventofcode.com/2019/day/2"""

from math import floor
from os import path
import unittest


class TestDay2(unittest.TestCase):
    def test_part1(self):
        tests = [
            ([1,0,0,0,99], [2,0,0,0,99]),
            ([2,3,0,3,99], [2,3,0,6,99]),
            ([2,4,4,5,99,0], [2,4,4,5,99,9801]),
            ([1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99]),
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


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDay2)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.failures:
        print(f"{len(result.failures)} tests failed!")
    else:
        print(f"All tests passed!")
        input_file = path.join(path.dirname(__file__), "input.txt")
        with open(input_file, 'r') as input:
            opcodes = [int(op) for op in input.readline().split(",")]
        # Puzzle dictates that we need to replace these values from the input!
        opcodes[1] = 12
        opcodes[2] = 2
        part_one_solution = _get_opcode_result(opcodes)[0]
        print(f"Day 02: Part one solution: {part_one_solution}")
