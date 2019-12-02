"""Advent of Code 2019 module."""


from importlib import import_module
from os import listdir, path
from unittest import TestLoader, TextTestRunner


TEST_CLASS_NAME = "ChallengeTests"
RUN_METHOD_NAME = "run_challenge"


def run_challenges():
    """Run all challenges."""

    for obj in listdir(path.dirname(__file__)):
        if obj.startswith("day_"):
            run_challenge(obj)


def run_challenge(day):
    """Run the challenge for a given day."""

    name = f"Day {day.split('_')[1]}"
    print(f"\n\n{name}")
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
    if result.failures:
        print(f"\tError: {len(result.failures)} tests failed!\n")
        return False
    print("\tAll tests passed!\n")
    return True


if __name__ == "__main__":
    run_challenges()
