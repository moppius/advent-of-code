"""Day 6 challenge for Advent of Code 2019 - https://adventofcode.com/2019/day/6"""

from os import path
from unittest import TestCase


class ChallengeTests(TestCase):
    """Tests for day 2."""

    def test_part1(self):
        """Test part one example values."""

        tests = [
            ("test_1_input.txt", 42),
        ]

        for test in tests:
            self.assertEqual(_get_orbit_count(_read_orbits(test[0])), test[1])


class SpaceObject():
    """An object in space which may orbit something, and has child objects which orbit it."""

    def __init__(self, name, parent_id=None):
        self.name = name
        self.parent_id = parent_id

    def __eq__(self, other):
        return self.name == other.name

    def get_orbits(self, space_objects, start_count):
        """Returns the number of direct & indirect orbits from this space object."""
        if self.parent_id is None:
            return start_count
        start_count += 1
        return space_objects[self.parent_id].get_orbits(space_objects, start_count)


def _get_orbit_count(orbit_list):
    space_objects = []
    for orbit in orbit_list:
        obj1 = SpaceObject(orbit[0])
        if obj1 not in space_objects:
            space_objects.append(obj1)

        parent_id = space_objects.index(obj1)
        obj2 = SpaceObject(orbit[1], parent_id=parent_id)
        if obj2 not in space_objects:
            space_objects.append(obj2)
        else:
            space_objects[space_objects.index(obj2)].parent_id = parent_id

    total_orbits = 0
    for space_object in space_objects:
        total_orbits += space_object.get_orbits(space_objects, 0)
    return total_orbits


def _read_orbits(filename):
    input_file = path.join(path.dirname(__file__), filename)
    orbits = []
    with open(input_file, 'r') as lines:
        orbits = [(orbit[0], orbit[1]) for orbit in [line.strip().split(")") for line in lines]]
    return orbits


def run_challenge():
    """Run the challenge."""

    part_one_solution = _get_orbit_count(_read_orbits("input.txt"))
    print(f"\tPart one solution: {part_one_solution}")
