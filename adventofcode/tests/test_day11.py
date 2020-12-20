from adventofcode.day11 import solve_part_one
from adventofcode.day11 import solve_part_two


def test_part_one():
    puzzle = ["L.LL.LL.LL",
              "LLLLLLL.LL",
              "L.L.L..L..",
              "LLLL.LL.LL",
              "L.LL.LL.LL",
              "L.LLLLL.LL",
              "..L.L.....",
              "LLLLLLLLLL",
              "L.LLLLLL.L",
              "L.LLLLL.LL"]
    assert solve_part_one(puzzle) == 37


def test_part_two():
    puzzle = ["L.LL.LL.LL",
              "LLLLLLL.LL",
              "L.L.L..L..",
              "LLLL.LL.LL",
              "L.LL.LL.LL",
              "L.LLLLL.LL",
              "..L.L.....",
              "LLLLLLLLLL",
              "L.LLLLLL.L",
              "L.LLLLL.LL"]
    assert solve_part_two(puzzle) == 26
