from adventofcode.inputs import reader
import re
from itertools import product


mask_pattern = re.compile("(?:mask = )(.*)")
memory_pattern = re.compile("\[(\\d+)\](?: = )(\\d+)")


def solve_part_one(puzzle: list) -> int:
    mask_map = {}
    memory_map = {}

    for instruction_position in range(0, len(puzzle)):
        mask_match = mask_pattern.findall(puzzle[instruction_position])
        if mask_match:
            # This is a mask
            mask_map.clear()
            for char_pos in range(0, len(mask_match[0])):
                if mask_match[0][char_pos] == "X":
                    continue
                mask_map[char_pos] = mask_match[0][char_pos]
            continue

        # Transform into bits, apply the mask
        matches = memory_pattern.findall(puzzle[instruction_position])
        memory_location = int(matches[0][0])
        memory_value = int(matches[0][1])
        memory_value_as_bits = list("{:036b}".format(memory_value))

        for key in mask_map:
            memory_value_as_bits[key] = mask_map[key]

        # Convert back and save
        memory_value_as_bits = "".join(memory_value_as_bits)
        memory_map[memory_location] = int(memory_value_as_bits, 2)

    return sum(memory_map.values())


def solve_part_two(puzzle: list) -> int:
    # We still write the value to mem, but now it's written to multiple mem values
    mask_map = {}
    memory_map = {}

    for instruction_position in range(0, len(puzzle)):
        x_count = 0
        x_location = []
        mask_match = mask_pattern.findall(puzzle[instruction_position])
        if mask_match:
            # This is a mask
            mask_map.clear()
            for char_pos in range(0, len(mask_match[0])):
                mask_map[char_pos] = mask_match[0][char_pos]
            continue

        # Transform into bits, apply the mask
        matches = memory_pattern.findall(puzzle[instruction_position])
        memory_location = int(matches[0][0])
        memory_value = int(matches[0][1])
        memory_location_as_bits = list("{:036b}".format(memory_location))

        for pos in range(0, len(mask_map)):
            if mask_map[pos] == "0":
                continue
            else:
                if mask_map[pos] == "X":
                    x_location.append(pos)
                    x_count += 1
                memory_location_as_bits[pos] = mask_map[pos]

        # Need to calculate all possible memory locations by finding all combination of x
        possible_combinations = product(range(2), repeat=x_count)
        for combination in possible_combinations:
            i = 0
            for location in x_location:
                memory_location_as_bits[location] = str(combination[i])
                i += 1
            # Calculate this memory, write value to it
            memory_location_as_bits_temp = "".join(memory_location_as_bits)
            memory_map[memory_location_as_bits_temp] = memory_value

    return sum(memory_map.values())


if __name__ == '__main__':
    puzzle_input = reader.read_file('adventofcode/inputs/day14.txt')
    solve_part_one(puzzle_input)
    solve_part_two(puzzle_input)
