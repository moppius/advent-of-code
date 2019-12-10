"""Day 10 challenge for Advent of Code 2019 - https://adventofcode.com/2019/day/10"""

from os import path
from unittest import TestCase


class ChallengeTests(TestCase):
    """Tests for day 10."""

    def test_part1(self):
        """Test part one example values."""
        tests = [
            ("test1_data.txt", (3, 4), 8),
            ("test2_data.txt", (5, 8), 33),
            ("test3_data.txt", (1, 2), 35),
            ("test4_data.txt", (6, 3), 41),
            ("test5_data.txt", (11, 13), 210),
        ]
        for test in tests:
            print(f"\nTESTING: {test[0]}")
            asteroid = AsteroidMap(test[0]).find_best_asteroid()
            self.assertEqual(asteroid.coords, test[1])
            self.assertEqual(asteroid.visible_count, test[2])


def greatest_common_divisor(x, y):
    """Returns the greatest common divisor of a and b."""
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x


class Asteroid:
    """An asteroid."""

    def __init__(self, x, y):
        self.coords = (x, y)
        self.visible_count = 0

    def update_visibility(self, asteroids):
        """Calculate the number of asteroids visible from this location."""
        steps = []
        distances = []
        for asteroid in asteroids:
            if asteroid.coords == self.coords:
                continue
            # Find the step pattern from self to asteroid as the smallest integer of x and y
            step = [asteroid.coords[0] - self.coords[0], asteroid.coords[1] - self.coords[1]]
            distance = abs(step[0]) + abs(step[1])
            divisor = abs(greatest_common_divisor(step[0], step[1]))
            step[0] = step[0] / divisor
            step[1] = step[1] / divisor
            steps.append(step)
            distances.append(distance)

        for i, step in enumerate(steps):
            is_visible = True
            for j, other_step in enumerate(steps):
                if i == j:
                    continue
                if other_step == step:
                    if distances[j] < distances[i]:
                        is_visible = False
            if is_visible:
                self.visible_count += 1


class AsteroidMap:
    """A map of asteroids."""

    def __init__(self, input_filename):
        self.asteroids = []
        self.map_maxs = [0, 0]
        self._read_file(input_filename)

    def _read_file(self, input_filename):
        input_file = path.join(path.dirname(__file__), input_filename)
        with open(input_file, 'r') as data:
            y = 0
            for line in data:
                x = 0
                for char in line:
                    if char == "#":
                        self.asteroids.append(Asteroid(x, y))
                    x += 1
                self.map_maxs[0] = x
                y += 1
            self.map_maxs[1] = y

    def find_best_asteroid(self):
        """Returns the `Asteroid` object from which most other asteroids can be seen."""
        best_asteroid = None
        for asteroid in self.asteroids:
            asteroid.update_visibility(self.asteroids)
            if not best_asteroid or asteroid.visible_count > best_asteroid.visible_count:
                best_asteroid = asteroid
        return best_asteroid


def run_challenge():
    """Run the challenge."""

    part_one_solution = AsteroidMap("input.txt").find_best_asteroid().visible_count
    print(f"\tPart one solution: {part_one_solution}")
