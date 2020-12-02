from adventofcode.day1 import solve_part_one
from adventofcode.day1 import solve_part_two


def test_part_one():
    puzzle = ["1721", "979", "366", "299", "675", "1456"]
    assert solve_part_one(puzzle) == 514579


def test_part_two():
    puzzle = ["1721", "979", "366", "299", "675", "1456"]
    assert solve_part_two(puzzle) == 241861950
