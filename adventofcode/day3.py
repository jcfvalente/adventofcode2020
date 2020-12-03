from adventofcode.inputs import reader


def solve_part_one(puzzle: list, right_increment: int) -> int:
    max_row_size = len(puzzle[0])
    current_position = 0
    trees = 0
    first_line = True
    for line in puzzle:
        if first_line:
            first_line = False
            current_position += right_increment
            continue
        if current_position >= len(line):
            current_position -= max_row_size
        if line[current_position] == "#":
            trees += 1
        current_position += right_increment

    return trees


def solve_part_two(puzzle: list) -> int:
    first_slope = solve_part_one(puzzle, 1)
    second_slope = solve_part_one(puzzle, 3)
    third_slope = solve_part_one(puzzle, 5)
    fourth_slope = solve_part_one(puzzle, 7)
    # We now need to jump down 2 at a time
    new_puzzle = puzzle[::2]
    fifth_slope = solve_part_one(new_puzzle, 1)
    return first_slope * second_slope * third_slope * fourth_slope * fifth_slope


if __name__ == '__main__':
    puzzle_input = reader.read_file('adventofcode/inputs/day3.txt')
    solve_part_one(puzzle_input, 3)
    solve_part_two(puzzle_input)
