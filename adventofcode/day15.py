def solve_part_one(puzzle: list) -> int:
    turn = 1
    numbers = []
    while turn <= 2020:
        if turn <= len(puzzle):
            numbers.append(puzzle[turn - 1])
            turn += 1
            continue
        # We finished the initial list. Look at the last number
        last_num = numbers[-1]
        if last_num in numbers[:len(numbers) - 1]:
            previous_turn = find_index(numbers[:len(numbers) - 1], last_num)
            numbers.append(turn - 1 - previous_turn)
        else:
            numbers.append(0)
        turn += 1
    return numbers[-1]


def find_index(numbers: list, number_to_find: int) -> int:
    index = 0
    for pos in range(0, len(numbers)):
        if number_to_find == numbers[pos]:
            index = pos
    return index + 1


def solve_part_two(puzzle: list) -> int:
    turn = 1
    numbers = []

    mem_helper = {}
    while turn <= 30000000:
        if turn <= len(puzzle):
            numbers.append(puzzle[turn - 1])
            if turn < len(puzzle):
                mem_helper[puzzle[turn - 1]] = turn
            turn += 1
            continue
        # We finished the initial list. Look at the last number
        last_num = numbers[-1]

        if last_num in mem_helper:
            numbers.append(turn - 1 - mem_helper[last_num])
            mem_helper[last_num] = turn - 1
        else:
            numbers.append(0)
            mem_helper[last_num] = turn - 1
        turn += 1

    return numbers[-1]


if __name__ == '__main__':
    puzzle_input = [15, 12, 0, 14, 3, 1]
    solve_part_one(puzzle_input)
    solve_part_two(puzzle_input)
