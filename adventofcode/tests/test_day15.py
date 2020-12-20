from adventofcode.day15 import solve_part_one
from adventofcode.day15 import solve_part_two


def test_part_one():
    puzzle = [0, 3, 6]
    assert solve_part_one(puzzle) == 436
    puzzle = [1, 3, 2]
    assert solve_part_one(puzzle) == 1
    puzzle = [2, 1, 3]
    assert solve_part_one(puzzle) == 10
    puzzle = [1, 2, 3]
    assert solve_part_one(puzzle) == 27
    puzzle = [2, 3, 1]
    assert solve_part_one(puzzle) == 78
    puzzle = [3, 1, 2]
    assert solve_part_one(puzzle) == 1836


def test_part_two():
    puzzle = [0, 3, 6]
    assert solve_part_two(puzzle) == 175594
    puzzle = [1, 3, 2]
    assert solve_part_two(puzzle) == 2578
    puzzle = [2, 1, 3]
    assert solve_part_two(puzzle) == 3544142
    puzzle = [1, 2, 3]
    assert solve_part_two(puzzle) == 261214
    puzzle = [2, 3, 1]
    assert solve_part_two(puzzle) == 6895259
    puzzle = [3, 2, 1]
    assert solve_part_two(puzzle) == 18
    puzzle = [3, 1, 2]
    assert solve_part_two(puzzle) == 362

