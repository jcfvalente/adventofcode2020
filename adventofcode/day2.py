from adventofcode.inputs import reader


def solve_part_one(puzzle: list) -> int:
    valid_passwords = 0
    for entry in puzzle:
        tokens = entry.split(' ')
        num_valid_chars = tokens[2].count(tokens[1][:1])

        # Validate
        valid_criteria = tokens[0].split('-')
        if int(valid_criteria[0]) <= num_valid_chars <= int(valid_criteria[1]):
            valid_passwords += 1
    return valid_passwords


def solve_part_two(puzzle: list) -> int:
    valid_passwords = 0
    for entry in puzzle:
        tokens = entry.split(' ')
        position_tokens = tokens[0].split('-')
        password = tokens[2]
        char = tokens[1][:1]
        if password[int(position_tokens[0]) - 1] == char:
            if password[int(position_tokens[1]) - 1] != char:
                valid_passwords += 1
        else:
            if password[int(position_tokens[1]) - 1] == char:
                valid_passwords += 1

    return valid_passwords


if __name__ == '__main__':
    puzzle_input = reader.read_file('adventofcode/inputs/day2.txt')
    solve_part_one(puzzle_input)
    solve_part_two(puzzle_input)
