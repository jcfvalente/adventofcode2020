from adventofcode.inputs import reader


def solve_part_one(puzzle: list) -> int:
    group_answer = ""
    num_of_answers = 0
    for answer in puzzle:
        if str(answer):
            group_answer = group_answer + str(answer)
            continue
        num_of_answers += len(set(group_answer))
        group_answer = ""
    return num_of_answers


def solve_part_two(puzzle: list) -> int:
    group_answer = ""
    num_of_answers = 0
    for answer in puzzle:
        if str(answer):
            group_answer = group_answer + str(answer) + " "
            continue

        separate_answers = group_answer.rsplit(" ")

        if len(separate_answers) == 2:  # Just one person answering
            num_of_answers += len(separate_answers[0])
            group_answer = ""
            continue

        # More than 1 person answering
        mem = {}
        for individual_answer in separate_answers:
            for char in individual_answer:
                if char in mem:
                    mem[char] += 1
                else:
                    mem[char] = 1

        persons = len(separate_answers) - 1
        for key in mem:
            if mem[key] == persons:
                num_of_answers += 1

        mem.clear()
        group_answer = ""
    return num_of_answers


if __name__ == '__main__':
    puzzle_input = reader.read_file("adventofcode/inputs/day6.txt")
    solve_part_one(puzzle_input)
    solve_part_two(puzzle_input)
