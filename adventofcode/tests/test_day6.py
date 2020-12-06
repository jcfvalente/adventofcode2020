from adventofcode.day6 import solve_part_one
from adventofcode.day6 import solve_part_two


def test_part_one():
    puzzle_input = ["abc",
                    "",
                    "a",
                    "b",
                    "c",
                    "",
                    "ab",
                    "ac",
                    "",
                    "a",
                    "a",
                    "a",
                    "a",
                    "",
                    "b",
                    ""]
    assert solve_part_one(puzzle_input) == 11


def test_part_two():
    puzzle_input = ["abc",
                    "",
                    "a",
                    "b",
                    "c",
                    "",
                    "ab",
                    "ac",
                    "",
                    "a",
                    "a",
                    "a",
                    "a",
                    "",
                    "b",
                    ""]
    assert solve_part_two(puzzle_input) == 6
