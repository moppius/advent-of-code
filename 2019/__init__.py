"""Advent of Code 2019 module."""


from argparse import ArgumentParser
from importlib import import_module
from os import listdir, path
from unittest import TestLoader, TextTestRunner


TEST_CLASS_NAME = "ChallengeTests"
RUN_METHOD_NAME = "run_challenge"


def main(args=None):
    """Parse arguments and run challenges."""

    parser = ArgumentParser(description="Run Advent of Code 2019 challenges.")
    parser.add_argument("-d", "--day", help="run a specific day's challenge")
    args = parser.parse_args(args)
    run_challenges(args.day)


def run_challenges(only_day=None):
    """Run all challenges if `only_latest` is False, otherwise run the latest day's challenge."""

    days = [obj for obj in listdir(path.dirname(__file__)) if obj.startswith("day_")]
    found_day = False
    for day in days:
        if only_day is not None:
            if int(day.split("_")[1]) == int(only_day):
                found_day = True
                _run_challenge(day)
                break
        else:
            _run_challenge(day)
    if only_day is not None and not found_day:
        print(f"Error: Failed to find module for day {only_day}!")


def _run_challenge(day):
    """Run the challenge for a given day."""

    name = f"Day {day.split('_')[1]}"
    print(f"\n\n{name}")
    if __name__ == "__main__":
        module = import_module(f"{day}.{day}", ".")
    else:
        module = import_module(f".{day}.{day}", "2019")
    method = getattr(module, RUN_METHOD_NAME, None)
    if method is None:
        print(f"Error: {name} has no '{RUN_METHOD_NAME}' method!")
        return False
    if not _run_tests(module):
        return False
    return method()


def _run_tests(module):
    """Look for unit tests in `module` and run them if found."""

    tests = getattr(module, TEST_CLASS_NAME, None)
    if not tests:
        print("----------------------------------------------------------------------")
        print("\tNo tests implemented!\n")
        return True

    suite = TestLoader().loadTestsFromTestCase(tests)
    result = TextTestRunner(verbosity=0).run(suite)
    if result.errors:
        print(f"\tErrors during test run!\n")
        return False
    elif result.failures:
        print(f"\tError: {len(result.failures)} tests failed!\n")
        return False
    print("\tAll tests passed!\n")
    return True


if __name__ == "__main__":
    main()
