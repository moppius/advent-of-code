"""Day 4 challenge for Advent of Code 2020 - https://adventofcode.com/2020/day/4"""

from os import path
from unittest import TestCase


class ChallengeTests(TestCase):
    test_input = """
        ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm

        iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
        hcl:#cfa07d byr:1929

        hcl:#ae17e1 iyr:2013
        eyr:2024
        ecl:brn pid:760753108 byr:1931
        hgt:179cm

        hcl:#cfa07d eyr:2025 pid:166559648
        iyr:2011 ecl:brn hgt:59in
    """

    def test_part_1(self):
        self.assertEqual(_count_valid_passports(self.test_input, ["cid"]), 2)


class Passport:
    ALL_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

    def __init__(self, *args):
        self.fields = {}
        fields = args[0].split()
        for field in fields:
            pair = field.split(":")
            self.fields[pair[0]] = pair[1]

    def is_valid(self, optional_fields, part_2_validation):
        for field in self.ALL_FIELDS:
            if field not in optional_fields and field not in self.fields:
                return False
            if part_2_validation and field not in optional_fields and not self.is_valid_field(field):
                return False
        return True

    def is_valid_field(self, field):
        if field is 'byr':
            int_field = int(self.fields[field])
            return int_field >= 1920 and int_field <= 2002
        elif field is 'iyr':
            int_field = int(self.fields[field])
            return int_field >= 2010 and int_field <= 2020
        elif field is 'eyr':
            int_field = int(self.fields[field])
            return int_field >= 2020 and int_field <= 2030
        elif field is 'hgt':
            height = self.fields[field]
            if height.endswith('cm'):
                val = int(height[:-2])
                return val >= 150 and val <= 193
            elif height.endswith('in'):
                val = int(height[:-2])
                return val >= 59 and val <= 76
            return False
        elif field is 'hcl':
            color = self.fields[field]
            return len(color) == 7 and color[0] == '#'
        elif field is 'ecl':
            return self.fields[field] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif field is 'pid':
            return len(self.fields[field]) == 9
        print(f"Failed to find field '{field}'!")
        return False


def _count_valid_passports(input_string, optional_fields, part_2_validation=False):
    strings = input_string.split("\n\n")
    num_valid = 0
    for string in strings:
        passport = Passport(string)
        if passport.is_valid(optional_fields, part_2_validation):
            num_valid += 1
    return num_valid


def run_challenge():
    input_file_path = path.join(path.dirname(__file__), "input.txt")
    with open(input_file_path, 'r') as input_file:
        input_string = input_file.read()

    part_one_solution = _count_valid_passports(input_string, ["cid"])
    print(f"\tPart one solution: {part_one_solution}")

    part_two_solution = _count_valid_passports(input_string, ["cid"], True)
    print(f"\tPart two solution: {part_two_solution}")
