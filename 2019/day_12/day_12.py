"""Day 12 challenge for Advent of Code 2019 - https://adventofcode.com/2019/day/12"""

from os import path
from re import split
from unittest import TestCase


class ChallengeTests(TestCase):
    """Tests for day 12."""

    def test_part1(self):
        """Test part one example values."""
        test = {
            "data": [
                "<x=-8, y=-10, z=0>",
                "<x=5, y=5, z=10>",
                "<x=2, y=-7, z=3>",
                "<x=9, y=-8, z=-3>",
            ],
            "result": 1940,
        }
        sim = MoonSimulation(test["data"])
        self.assertEqual(sim.simulate(100), test["result"])


class Moon:
    """That's no moon..."""

    def __init__(self, location):
        self.x, self.y, self.z = self._parse(location)
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0

    def update_velocity(self, other_moon):
        """Update the velocity of this moon relative to `other_moon`."""
        if other_moon.x != self.x:
            self.vel_x += 1 if other_moon.x > self.x else -1
        if other_moon.y != self.y:
            self.vel_y += 1 if other_moon.y > self.y else -1
        if other_moon.z != self.z:
            self.vel_z += 1 if other_moon.z > self.z else -1

    def apply_velocity(self):
        """Apply velocity and modify this moon's location."""
        self.x += self.vel_x
        self.y += self.vel_y
        self.z += self.vel_z

    @property
    def potential_energy(self):
        """Potential energy of this moon."""
        return abs(self.x) + abs(self.y) + abs(self.z)

    @property
    def kinetic_energy(self):
        """Kinetic energy of this moon."""
        return abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z)

    @property
    def total_energy(self):
        """Total energy of this moon."""
        return self.potential_energy * self.kinetic_energy

    @staticmethod
    def _parse(location):
        tokens = [int(token) for token in split(' |=|,|[a-z]|<|>', location) if token]
        return tokens[0], tokens[1], tokens[2]

    def __repr__(self):
        return f"Moon at ({self.x}, {self.y}, {self.z})"


class MoonSimulation:
    """Simulate moon orbits."""

    def __init__(self, moon_data):
        self.moons = [Moon(data) for data in moon_data]
        self.step = 0

    def simulate(self, steps):
        """Step the simulation for `steps` iterations."""
        while self.step < steps:
            for moon in self.moons:
                for other_moon in self.moons:
                    if moon != other_moon:
                        moon.update_velocity(other_moon)
            for moon in self.moons:
                moon.apply_velocity()
            self.step += 1

        return sum([moon.total_energy for moon in self.moons])


def run_challenge():
    """Run the challenge."""

    input_file = path.join(path.dirname(__file__), "input.txt")
    with open(input_file, 'r') as data:
        moon_data = [line.strip() for line in data]
    sim = MoonSimulation(moon_data)
    part_one_solution = sim.simulate(1000)
    print(f"\tPart one solution: {part_one_solution}")
