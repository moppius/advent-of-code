"""Day 6 challenge for Advent of Code 2019 - https://adventofcode.com/2019/day/6"""

from os import path
from unittest import TestCase


class ChallengeTests(TestCase):
    """Tests for day 6."""

    def test_part1(self):
        """Test part one example values."""

        tests = [
            ("test_1_input.txt", 42),
        ]

        for test in tests:
            self.assertEqual(_get_orbit_count(_read_orbits(test[0])), test[1])

    def test_part2(self):
        """Test part two example values."""

        tests = [
            ("test_2_input.txt", 4),
        ]

        for test in tests:
            self.assertEqual(_get_min_transfer_count(_read_orbits(test[0])), test[1])


class SpaceObject():
    """An object in space which may orbit something, and has child objects which orbit it."""

    def __init__(self, name, parent_id=None):
        self.name = name
        self.parent_id = parent_id

    def __eq__(self, other):
        return self.name == other.name

    def get_parent_ids(self, space_objects, parent_ids):
        """Fills the `parent_ids` list with all parents."""
        if self.parent_id is None:
            return
        parent_ids.append(self.parent_id)
        space_objects[self.parent_id].get_parent_ids(space_objects, parent_ids)


def _build_space_objects(orbit_list):
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
    return space_objects


def _get_orbit_count(orbit_list):
    space_objects = _build_space_objects(orbit_list)
    total_orbits = 0
    for space_object in space_objects:
        parent_ids = []
        space_object.get_parent_ids(space_objects, parent_ids)
        total_orbits += len(parent_ids)
    return total_orbits


def _get_min_transfer_count(orbit_list):
    space_objects = _build_space_objects(orbit_list)
    start_parent_ids = []
    end_parent_ids = []
    for space_object in space_objects:
        if space_object.name == "YOU":
            space_object.get_parent_ids(space_objects, start_parent_ids)
        if space_object.name == "SAN":
            space_object.get_parent_ids(space_objects, end_parent_ids)

    smallest_distance = None
    for i, start_id in enumerate(start_parent_ids):
        for j, end_id in enumerate(end_parent_ids):
            if start_id == end_id:
                this_distance = i + j
                if smallest_distance is None or this_distance < smallest_distance:
                    smallest_distance = this_distance

    return smallest_distance


def _read_orbits(filename):
    input_file = path.join(path.dirname(__file__), filename)
    orbits = []
    with open(input_file, 'r') as lines:
        orbits = [(orbit[0], orbit[1]) for orbit in [line.strip().split(")") for line in lines]]
    return orbits


def run_challenge():
    """Run the challenge."""

    orbits = _read_orbits("input.txt")
    part_one_solution = _get_orbit_count(orbits)
    print(f"\tPart one solution: {part_one_solution}")
    part_two_solution = _get_min_transfer_count(orbits)
    print(f"\tPart two solution: {part_two_solution}")
