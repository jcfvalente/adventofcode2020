from adventofcode.inputs import reader


def solve_part_one(puzzle: list, preamble: int) -> int:
    puzzle = [int(i) for i in puzzle]
    lower_index = 0
    upper_index = preamble
    left_helper = 0
    right_helper = preamble - 1

    while left_helper < right_helper:
        puzzle_sliced = puzzle[lower_index:upper_index]
        puzzle_sliced.sort()
        if puzzle_sliced[left_helper] + puzzle_sliced[right_helper] > puzzle[upper_index]:
            right_helper -= 1
            continue
        if puzzle_sliced[left_helper] + puzzle_sliced[right_helper] < puzzle[upper_index]:
            left_helper += 1
            continue
        if puzzle_sliced[left_helper] + puzzle_sliced[right_helper] == puzzle[upper_index]:
            upper_index += 1
            lower_index += 1
            left_helper = 0
            right_helper = preamble - 1

    return puzzle[upper_index]


def solve_part_two(puzzle: list, sum_goal: int) -> int:
    puzzle = [int(i) for i in puzzle]

    for contiguous_range in range(2, len(puzzle) - 1):
        lower_index = 0
        upper_index = contiguous_range
        while upper_index <= len(puzzle):
            set_of_puzzle = puzzle[lower_index:upper_index]
            if sum(set_of_puzzle) == sum_goal:
                set_of_puzzle.sort()
                return set_of_puzzle[0] + set_of_puzzle[len(set_of_puzzle) - 1]
            lower_index += 1
            upper_index += 1
    return 0


if __name__ == '__main__':
    puzzle_input = reader.read_file('adventofcode/inputs/day9.txt')
    solve_part_one(puzzle_input, 25)
    solve_part_two(puzzle_input, 756008079)
