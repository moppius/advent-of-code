"""Day 4 challenge for Advent of Code 2019 - https://adventofcode.com/2019/day/4"""

from unittest import TestCase


PASSWORD_RANGE = (272091, 815432)


class ChallengeTests(TestCase):
    """Tests for day 2."""

    def test_part1(self):
        """Test part one example values."""

        self.assertTrue(_valid_password(111111))
        self.assertFalse(_valid_password(223450))
        self.assertFalse(_valid_password(123789))


def _valid_password(password):
    password_string = str(password)
    if len(password_string) != 6:
        return False
    has_double = False
    for i in range(5):
        int_a = int(password_string[i])
        int_b = int(password_string[i+1])
        if int_a > int_b:
            return False
        if int_a == int_b:
            has_double = True
    return has_double


def run_challenge():
    """Run the challenge."""

    part_one_solution = 0
    for password in range(PASSWORD_RANGE[0], PASSWORD_RANGE[1]):
        if _valid_password(password):
            part_one_solution += 1
    print(f"\tPart one solution: {part_one_solution}")
