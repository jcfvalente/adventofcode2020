from adventofcode.inputs import reader


def solve_part_one(puzzle: list) -> int:
    accumulator = 0
    executed_instructions_index = []
    current_index = 0

    while current_index not in executed_instructions_index:  # While we don't repeat an instruction
        executed_instructions_index.append(current_index)
        split_instruction = puzzle[current_index].split(" ")

        if split_instruction[0] == "nop":
            current_index += 1
            continue
        if split_instruction[0] == "jmp":
            current_index += int(split_instruction[1])
            continue
        if split_instruction[0] == "acc":
            current_index += 1
            accumulator += int(split_instruction[1])

    return accumulator


def solve_part_two(puzzle: list) -> int:
    accumulator = 0
    executed_instructions_index = []
    current_index = 0

    instructions_map = {
        "jmp_instructions_index": [],
        "nop_instructions_index": []
    }

    # Save the position of all the jmp and nop instructions
    while current_index not in executed_instructions_index:
        executed_instructions_index.append(current_index)
        split_instruction = puzzle[current_index].split(" ")

        if split_instruction[0] == "nop":
            instructions_map["nop_instructions_index"].append(current_index)
            current_index += 1
            continue
        if split_instruction[0] == "jmp":
            instructions_map["jmp_instructions_index"].append(current_index)
            current_index += int(split_instruction[1])
            continue
        if split_instruction[0] == "acc":
            current_index += 1

    # Let's go through all of the instructions for both jmp and nop and try to replace just one instruction and see
    # if we ever reach the end of the instruction set
    for index_list in instructions_map:
        for index in instructions_map[index_list]:
            accumulator = 0
            current_index = 0
            executed_instructions_index = []

            while current_index not in executed_instructions_index:
                if current_index == len(puzzle):
                    # We're trying to execute next instruction after the last one, so we've reached the end here
                    return accumulator

                executed_instructions_index.append(current_index)
                split_instruction = puzzle[current_index].split(" ")

                # Go through all the same instructions again, and replace the one we're looking for
                if current_index == index:
                    if index_list == "jmp_instructions_index":
                        split_instruction[0] = "nop"
                    else:
                        split_instruction[0] = "jmp"

                if split_instruction[0] == "nop":
                    current_index += 1
                    continue
                if split_instruction[0] == "jmp":
                    current_index += int(split_instruction[1])
                    continue
                if split_instruction[0] == "acc":
                    current_index += 1
                    accumulator += int(split_instruction[1])

    return accumulator


if __name__ == '__main__':
    puzzle_input = reader.read_file('adventofcode/inputs/day8.txt')
    solve_part_one(puzzle_input)
    solve_part_two(puzzle_input)
