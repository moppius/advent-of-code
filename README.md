# 👨‍💻🎄 Advent of Code
Repository for Advent of Code challenges - https://adventofcode.com/

# Prerequisites

- Some version of Python 3, probably

# How to run

All challenges are implemented as test-driven methods, and each day's challenge is a submodule that runs tests to check solution validity, then runs the code on the challenge input, which is usually stored in an *input.txt* file in that day's folder.

- To run all challenges for a given year, just run `python advent-of-code.py --year 2019` in the root of wherever you checked out this repository.
- To run a specific challenge, run `python advent-of-code.py --year 2020 --day 2` to run the 2020 Day 2 challenge, for example.

If everything passes and runs, the solution output for the given challenge(s) will be printed to standard output.
