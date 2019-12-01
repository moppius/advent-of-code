"""Day 1 challenge for Avent of Code 2019 - https://adventofcode.com/2019/day/1"""

from math import floor
from os import path


def _get_fuel_for_mass(mass):
    return floor(mass / 3) - 2


_tests = [
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583),
]
_num_tests_passed = 0
for test in _tests:
    fuel = _get_fuel_for_mass(test[0])
    if fuel == test[1]:
        _num_tests_passed += 1
    else:
        print(f"Test failed for mass {test[0]}: Expected {test[1]}, got {fuel}")

if _num_tests_passed == len(_tests):
    print(f"All {_num_tests_passed} tests passed!")

    input_file = path.join(path.dirname(__file__), "input.txt")
    total_fuel = 0
    with open(input_file, 'r') as input:
        mass = input.readline()
        while mass:
            total_fuel += _get_fuel_for_mass(int(mass))
            mass = input.readline()

    print(f"Total mass: {total_fuel}")
