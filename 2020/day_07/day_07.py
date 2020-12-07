"""Day 7 challenge for Advent of Code 2020 - https://adventofcode.com/2020/day/7"""

from os import path
from unittest import TestCase


class ChallengeTests(TestCase):
    def test_part_1(self):
        self.assertEqual(_get_num_bags_containing("test_input.txt", "shiny", "gold"), 4)


class Bag:
    def __init__(self, line):
        tokens = line.split("bags contain")
        self.style = tokens[0].split()[0]
        self.color = tokens[0].split()[1]
        self.contains = {}
        if len(tokens) > 1 and "no other" not in tokens[1]:
            contains_bags = tokens[1].split(",")
            for contains_bag in contains_bags:
                tokens = contains_bag.split()
                self.contains[f"{tokens[1]} {tokens[2]}"] = int(tokens[0])

    def can_contain(self, bag):
        if f"{bag.style} {bag.color}" in self.contains:
            return True
        return False

    def __repr__(self):
        cont_str = "contains no other bags"
        if self.contains:
            cont_str = "contains"
            for bag in self.contains:
                count = self.contains[bag]
                cont_str += f" {count} {bag},"
        return f"{self.style} {self.color}: {cont_str}."


def _get_num_bags_containing(input_filename, bag_style, bag_color):
    input_file_path = path.join(path.dirname(__file__), input_filename)
    with open(input_file_path, 'r') as input_file:
        bags = [Bag(line) for line in input_file.readlines()]
    all_bags = bags.copy()
    goal_bag = Bag(f"{bag_style} {bag_color}")
    remaining_bags = bags.copy()
    max_count = 1000
    count = 0
    can_contain_bags = []
    while remaining_bags:
        for bag in all_bags:
            if bag in remaining_bags:
                if bag.can_contain(goal_bag):
                    if bag not in can_contain_bags:
                        can_contain_bags.append(bag)
                    remaining_bags.remove(bag)
                elif not bag.contains:
                    remaining_bags.remove(bag)
                else:
                    for inner_bag in can_contain_bags:
                        if bag.can_contain(inner_bag) and bag in remaining_bags:
                            remaining_bags.remove(bag)
                            if bag not in can_contain_bags:
                                can_contain_bags.append(bag)

        count += 1
        if count > max_count:
            break
    return len(can_contain_bags)


def run_challenge():
    part_one_solution = _get_num_bags_containing("input.txt", "shiny", "gold")
    print(f"\tPart one solution: {part_one_solution}")
