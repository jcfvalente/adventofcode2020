from adventofcode.day12 import solve_part_one
from adventofcode.day12 import solve_part_two


def test_part_one():
    puzzle = ["F10",
              "N3",
              "F7",
              "R90",
              "F11"]
    assert solve_part_one(puzzle) == 25


def test_part_two():
    puzzle = ["F10",
              "N3",
              "F7",
              "R90",
              "F11"]
    assert solve_part_two(puzzle) == 286
