from adventofcode.day13 import solve_part_one
from adventofcode.day13 import solve_part_two


def test_part_one():
    puzzle = ["939",
              "7,13,x,x,59,x,31,19"]
    assert solve_part_one(puzzle) == 295


def test_part_two():
    puzzle = ["939",
              "7,13,x,x,59,x,31,19"]
    assert solve_part_two(puzzle) == 1068781
    puzzle = ["x",
              "17,x,13,19"]
    assert solve_part_two(puzzle) == 3417
    puzzle = ["x",
              "67,7,59,61"]
    assert solve_part_two(puzzle) == 754018
    puzzle = ["x",
              "67,x,7,59,61"]
    assert solve_part_two(puzzle) == 779210
    puzzle = ["x",
              "67,7,x,59,61"]
    assert solve_part_two(puzzle) == 1261476
    puzzle = ["x",
              "1789,37,47,1889"]
    assert solve_part_two(puzzle) == 1202161486
