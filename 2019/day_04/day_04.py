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

    def test_part2(self):
        """Test part two example values."""

        self.assertTrue(_valid_password(112233, part_two=True))
        self.assertFalse(_valid_password(123444, part_two=True))
        self.assertTrue(_valid_password(111122, part_two=True))


def _valid_password(password, part_two=False):
    password_string = str(password)
    if len(password_string) != 6:
        return False
    matching_groups = {}
    for i in range(5):
        int_a = int(password_string[i])
        int_b = int(password_string[i+1])
        if int_a > int_b:
            return False
        if int_a == int_b:
            if int_a not in matching_groups.keys():
                matching_groups[int_a] = 2
            else:
                matching_groups[int_a] += 1
    has_double = False
    for key in matching_groups:
        if part_two:
            if matching_groups[key] == 2:
                has_double = True
        else:
            if matching_groups[key] >= 2:
                has_double = True
    return has_double


def run_challenge():
    """Run the challenge."""

    part_one_solution = 0
    part_two_solution = 0

    for password in range(PASSWORD_RANGE[0], PASSWORD_RANGE[1]):
        if _valid_password(password):
            part_one_solution += 1
        if _valid_password(password, part_two=True):
            part_two_solution += 1

    print(f"\tPart one solution: {part_one_solution}")
    print(f"\tPart two solution: {part_two_solution}")
