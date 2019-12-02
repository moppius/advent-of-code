"""Day 1 challenge for Advent of Code 2019 - https://adventofcode.com/2019/day/1"""

from math import floor
from os import path
import unittest


class TestFuelCalculation(unittest.TestCase):
    """Tests for day 1."""

    def test_fuel(self):
        """Test part one example values."""
        tests = [
            (12, 2),
            (14, 2),
            (1969, 654),
            (100756, 33583),
        ]
        for test in tests:
            self.assertEqual(_get_fuel_for_mass(test[0], recursive=False), test[1])

    def test_fuel_recursive(self):
        """Test part two example values."""
        tests = [
            (14, 2),
            (1969, 966),
            (100756, 50346),
        ]
        for test in tests:
            self.assertEqual(_get_fuel_for_mass(test[0]), test[1])


def _get_fuel_for_mass(mass, recursive=True):
    fuel = floor(mass / 3) - 2
    if recursive and fuel > 0:
        fuel_mass = _get_fuel_for_mass(fuel)
        if fuel_mass > 0:
            fuel += fuel_mass
    return fuel


if __name__ == '__main__':
    SUITE = unittest.TestLoader().loadTestsFromTestCase(TestFuelCalculation)
    RESULT = unittest.TextTestRunner(verbosity=2).run(SUITE)
    if RESULT.failures:
        print(f"{len(RESULT.failures)} tests failed!")
    else:
        print(f"All tests passed!")

        INPUT_FILE = path.join(path.dirname(__file__), "input.txt")
        with open(INPUT_FILE, 'r') as fp:
            MASSES = [int(mass) for mass in fp]

        PART_ONE_SOLUTION = sum([_get_fuel_for_mass(mass, recursive=False) for mass in MASSES])
        print(f"Part one solution: {PART_ONE_SOLUTION}")

        PART_TWO_SOLUTION = sum([_get_fuel_for_mass(mass) for mass in MASSES])
        print(f"Part two solution: {PART_TWO_SOLUTION}")
