"""Day 1 challenge for Advent of Code 2019 - https://adventofcode.com/2019/day/1"""

from math import floor
from os import path
import unittest


class TestFuelCalculation(unittest.TestCase):
    def test_fuel(self):
        _tests = [
            (12, 2),
            (14, 2),
            (1969, 654),
            (100756, 33583),
        ]
        for test in _tests:
            self.assertEqual(_get_fuel_for_mass(test[0]), test[1])


def _get_fuel_for_mass(mass):
    return floor(mass / 3) - 2


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFuelCalculation)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if len(result.failures):
        print(f"{len(result.failures)} tests failed!")
    else:
        print(f"All tests passed!")
        input_file = path.join(path.dirname(__file__), "input.txt")
        total_fuel = 0
        with open(input_file, 'r') as input:
            mass = input.readline()
            while mass:
                total_fuel += _get_fuel_for_mass(int(mass))
                mass = input.readline()

        print(f"Total mass: {total_fuel}")
