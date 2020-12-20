from adventofcode.day14 import solve_part_one
from adventofcode.day14 import solve_part_two


def test_part_one():
    puzzle = ["mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
              "mem[8] = 11",
              "mem[7] = 101",
              "mem[8] = 0"]
    assert solve_part_one(puzzle) == 165


def test_part_two():
    puzzle = ["mask = 000000000000000000000000000000X1001X",
              "mem[42] = 100",
              "mask = 00000000000000000000000000000000X0XX",
              "mem[26] = 1"]
    assert solve_part_two(puzzle) == 208

