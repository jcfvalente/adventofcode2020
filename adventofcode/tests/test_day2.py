from adventofcode.day2 import solve_part_one
from adventofcode.day2 import solve_part_two


def test_part_one():
    puzzle = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    assert solve_part_one(puzzle) == 2


def test_part_two():
    puzzle = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    assert solve_part_two(puzzle) == 1
