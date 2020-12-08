from adventofcode.day8 import solve_part_one
from adventofcode.day8 import solve_part_two


def test_part_one():
    puzzle_input = ["nop +0",
                    "acc +1",
                    "jmp +4",
                    "acc +3",
                    "jmp -3",
                    "acc -99",
                    "acc +1",
                    "jmp -4",
                    "acc +6"]
    assert solve_part_one(puzzle_input) == 5


def test_part_two():
    puzzle_input = ["nop +0",
                    "acc +1",
                    "jmp +4",
                    "acc +3",
                    "jmp -3",
                    "acc -99",
                    "acc +1",
                    "jmp -4",
                    "acc +6"]
    assert solve_part_two(puzzle_input) == 8
