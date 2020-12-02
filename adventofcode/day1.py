from adventofcode.inputs import reader


def solve_part_one(puzzle: list) -> int:
    puzzle = convert_and_sort(puzzle)
    left_side = 0
    right_side = len(puzzle) - 1
    while left_side < right_side:
        if puzzle[left_side] + puzzle[right_side] > 2020:
            right_side -= 1
        elif puzzle[left_side] + puzzle[right_side] < 2020:
            left_side += 1
        else:
            break
    return puzzle[left_side] * puzzle[right_side]


def solve_part_two(puzzle: list) -> int:
    puzzle = convert_and_sort(puzzle)
    left_side = 0
    mid_point = left_side + 1
    right_side = len(puzzle) - 1
    while left_side < right_side:
        if puzzle[left_side] + puzzle[right_side] + puzzle[mid_point] > 2020:
            right_side -= 1
        elif puzzle[left_side] + puzzle[right_side] + puzzle[mid_point] < 2020:
            if mid_point - left_side == 1:
                mid_point += 1
            else:
                left_side += 1
        else:
            break
    return puzzle[left_side] * puzzle[right_side] * puzzle[mid_point]


def convert_and_sort(str_input: list) -> list:
    # Convert and sort the input first
    int_input = [int(i) for i in str_input]
    int_input.sort()
    return int_input


if __name__ == '__main__':
    puzzle_input = reader.read_file('adventofcode/inputs/day1.txt')
    solution_one = solve_part_one(puzzle_input)
    solution_two = solve_part_two(puzzle_input)

