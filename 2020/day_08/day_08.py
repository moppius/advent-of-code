"""Day 8 challenge for Advent of Code 2020 - https://adventofcode.com/2020/day/8"""

from os import path
from unittest import TestCase


class ChallengeTests(TestCase):
    def test_part_1(self):
        console = HandheldGameConsole("test_input.txt")
        console.run(1)
        self.assertEqual(console.accumulator, 5)


class HandheldGameConsole:
    def __init__(self, input_filename):
        input_file_path = path.join(path.dirname(__file__), input_filename)
        with open(input_file_path, 'r') as input_file:
            self.code = [self._get_code(line) for line in input_file.readlines()]
        self.current_instruction = 0
        self.accumulator = 0
        self.run_loops = 0

    def run(self, num_loops):
        run_instructions = []
        while True:
            if self.current_instruction in run_instructions:
                self.run_loops += 1
                if self.run_loops >= num_loops:
                    break
            else:
                run_instructions.append(self.current_instruction)

            curr_op = self.code[self.current_instruction]

            if curr_op[0] == 'nop':
                self.current_instruction += 1
            elif curr_op[0] == 'acc':
                self.current_instruction += 1
                self.accumulator += curr_op[1]
            elif curr_op[0] == 'jmp':
                self.current_instruction += curr_op[1]
            else:
                print(f"Unexpected instruction '{curr_op[0]}'")

    @staticmethod
    def _get_code(line):
        tokens = line.split()
        return (tokens[0], int(tokens[1]))


def run_challenge():
    console = HandheldGameConsole("input.txt")
    console.run(1)
    print(f"\tPart one solution: {console.accumulator}")
