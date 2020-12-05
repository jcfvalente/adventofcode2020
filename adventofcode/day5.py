from adventofcode.inputs import reader
import math


def solve_part_one(ticket_list: list) -> int:
    highest_seat_id = 0
    for ticket in ticket_list:
        seat_id = get_seat_id(ticket)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id
    return highest_seat_id


def solve_part_two(ticket_list: list) -> int:
    all_seat_ids = []
    for ticket in ticket_list:
        all_seat_ids.append(get_seat_id(ticket))

    all_seat_ids.sort()
    for pos in range(0, len(all_seat_ids)):
        if pos == 0:
            continue
        if all_seat_ids[pos] - all_seat_ids[pos - 1] >= 2:
            return all_seat_ids[pos] - 1


def get_seat_id(ticket: str) -> int:
    lower_bound = 0
    top_bound = 127
    left_bound = 0
    right_bound = 7
    for pos in range(0, len(ticket)):
        if pos <= 6:
            if ticket[pos] == "F":  # top_bound goes down
                top_bound -= (top_bound - lower_bound) / 2
                top_bound = math.floor(top_bound)
            else:  # lower_bound goes up
                lower_bound += (top_bound - lower_bound) / 2
                lower_bound = math.ceil(lower_bound)
        elif pos >= 7:
            if ticket[pos] == "R":  # left_bound goes up
                left_bound += (right_bound - left_bound) / 2
                left_bound = math.ceil(left_bound)
            else:  # right_bound comes down
                right_bound -= (right_bound - left_bound) / 2
                right_bound = math.floor(right_bound)
    return top_bound * 8 + left_bound


if __name__ == '__main__':
    puzzle_input = reader.read_file('adventofcode/inputs/day5.txt')
    solve_part_one(puzzle_input)
    solve_part_two(puzzle_input)
