from adventofcode.day9 import solve_part_one
from adventofcode.day9 import solve_part_two


def test_part_one():
    puzzle_input = ["35",
                    "20",
                    "15",
                    "25",
                    "47",
                    "40",
                    "62",
                    "55",
                    "65",
                    "95",
                    "102",
                    "117",
                    "150",
                    "182",
                    "127",
                    "219",
                    "299",
                    "277",
                    "309",
                    "576"]
    assert solve_part_one(puzzle_input, 5) == 127


def test_part_two():
    puzzle_input = ["35",
                    "20",
                    "15",
                    "25",
                    "47",
                    "40",
                    "62",
                    "55",
                    "65",
                    "95",
                    "102",
                    "117",
                    "150",
                    "182",
                    "127",
                    "219",
                    "299",
                    "277",
                    "309",
                    "576"]
    assert solve_part_two(puzzle_input, 127) == 62
