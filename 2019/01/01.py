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
            self.assertEqual(_get_fuel_for_mass(test[0], recursive=False), test[1])

    def test_fuel_recursive(self):
        _tests = [
            (14, 2),
            (1969, 966),
            (100756, 50346),
        ]
        for test in _tests:
            self.assertEqual(_get_fuel_for_mass(test[0]), test[1])


def _get_fuel_for_mass(mass, recursive=True):
    fuel = floor(mass / 3) - 2
    if recursive and fuel > 0:
        fuel_mass = _get_fuel_for_mass(fuel)
        if fuel_mass > 0:
            fuel += fuel_mass
    return fuel


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFuelCalculation)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if len(result.failures):
        print(f"{len(result.failures)} tests failed!")
    else:
        print(f"All tests passed!")
        input_file = path.join(path.dirname(__file__), "input.txt")
        masses = []
        with open(input_file, 'r') as input:
            mass = input.readline()
            while mass:
                masses.append(int(mass))
                mass = input.readline()

        part_one_solution = sum([_get_fuel_for_mass(mass, recursive=False) for mass in masses])
        print(f"Part one solution: {part_one_solution}")
        
        part_two_solution = sum([_get_fuel_for_mass(mass) for mass in masses])
        print(f"Part two solution: {part_two_solution}")
