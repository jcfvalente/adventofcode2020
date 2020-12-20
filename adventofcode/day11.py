from adventofcode.inputs import reader
import copy


def solve_part_one(seats_map: list) -> int:
    seats_stable = False
    aux_seats_map = []
    seats_map = [list(row) for row in seats_map]

    while not seats_stable:  # Keeping doing this while the seats change
        internal_stable = True
        if aux_seats_map:
            seats_map = copy.deepcopy(aux_seats_map)
        else:
            aux_seats_map = copy.deepcopy(seats_map)

        for row in range(0, len(seats_map)):  # each row
            for seat_position in range(0, len(seats_map[row])):  # each set
                if seats_map[row][seat_position] == ".":
                    continue

                occupied = 0
                # North
                if row - 1 >= 0:
                    # N
                    if seats_map[row - 1][seat_position] == "#":
                        occupied += 1
                    # NE
                    if seat_position - 1 >= 0:
                        if seats_map[row - 1][seat_position - 1] == "#":
                            occupied += 1
                    # NW
                    if seat_position + 1 < len(seats_map[row]):
                        if seats_map[row - 1][seat_position + 1] == "#":
                            occupied += 1
                # South
                if row + 1 < len(seats_map):
                    # S
                    if seats_map[row + 1][seat_position] == "#":
                        occupied += 1
                    # SE
                    if seat_position - 1 >= 0:
                        if seats_map[row + 1][seat_position - 1] == "#":
                            occupied += 1
                    # NW
                    if seat_position + 1 < len(seats_map[row]):
                        if seats_map[row + 1][seat_position + 1] == "#":
                            occupied += 1
                # East
                if seat_position - 1 >= 0:
                    if seats_map[row][seat_position - 1] == "#":
                        occupied += 1
                # West
                if seat_position + 1 < len(seats_map[row]):
                    if seats_map[row][seat_position + 1] == "#":
                        occupied += 1

                # Update setting status
                if seats_map[row][seat_position] == "L" and occupied == 0:
                    aux_seats_map[row][seat_position] = "#"
                    internal_stable = False
                    continue
                if seats_map[row][seat_position] == "#" and occupied >= 4:
                    aux_seats_map[row][seat_position] = "L"
                    internal_stable = False
                    continue
        if internal_stable:
            # If we get here it means no seats have changed, it's stable
            seats_map = aux_seats_map
            seats_stable = True

    return count_occupied_seats(seats_map)


def solve_part_two(seats_map: list) -> int:
    seats_stable = False
    aux_seats_map = []
    seats_map = [list(row) for row in seats_map]

    while not seats_stable:  # Keeping doing this while the seats change
        internal_stable = True
        if aux_seats_map:
            seats_map = copy.deepcopy(aux_seats_map)
        else:
            aux_seats_map = copy.deepcopy(seats_map)

        for row in range(0, len(seats_map)):
            for seat_position in range(0, len(seats_map[row])):
                if seats_map[row][seat_position] == ".":
                    continue

                occupied = 0
                # North
                if row - 1 >= 0:
                    # N
                    first_try = row - 1
                    while first_try >= 0:
                        if seats_map[first_try][seat_position] != ".":
                            if seats_map[first_try][seat_position] == "#":
                                occupied += 1
                                break
                            else:
                                break
                        first_try -= 1
                    # NE
                    if seat_position - 1 >= 0:
                        up_try = row - 1
                        left_try = seat_position - 1
                        while up_try >= 0 and left_try >= 0:
                            if seats_map[up_try][left_try] != ".":
                                if seats_map[up_try][left_try] == "#":
                                    occupied += 1
                                    break
                                else:
                                    break
                            up_try -= 1
                            left_try -= 1
                    # NW
                    if seat_position + 1 < len(seats_map[row]):
                        up_try = row - 1
                        right_try = seat_position + 1
                        while up_try >= 0 and right_try < len(seats_map[row]):
                            if seats_map[up_try][right_try] != ".":
                                if seats_map[up_try][right_try] == "#":
                                    occupied += 1
                                    break
                                else:
                                    break
                            up_try -= 1
                            right_try += 1

                # South
                if row + 1 < len(seats_map):
                    # S
                    first_try = row + 1
                    while first_try < len(seats_map):
                        if seats_map[first_try][seat_position] != ".":
                            if seats_map[first_try][seat_position] == "#":
                                occupied += 1
                                break
                            else:
                                break
                        first_try += 1
                    # SE
                    if seat_position - 1 >= 0:
                        down_try = row + 1
                        left_try = seat_position - 1
                        while down_try < len(seats_map) and left_try >= 0:
                            if seats_map[down_try][left_try] != ".":
                                if seats_map[down_try][left_try] == "#":
                                    occupied += 1
                                    break
                                else:
                                    break
                            down_try += 1
                            left_try -= 1
                    # SW
                    if seat_position + 1 < len(seats_map[row]):
                        down_try = row + 1
                        right_try = seat_position + 1
                        while down_try < len(seats_map) and right_try < len(seats_map[row]):
                            if seats_map[down_try][right_try] != ".":
                                if seats_map[down_try][right_try] == "#":
                                    occupied += 1
                                    break
                                else:
                                    break
                            down_try += 1
                            right_try += 1
                # East
                left_first_try = seat_position - 1
                while left_first_try >= 0:
                    if seats_map[row][left_first_try] == "#":
                        occupied += 1
                        break
                    elif seats_map[row][left_first_try] == "L":
                        break
                    left_first_try -= 1
                # West
                right_first_try = seat_position + 1
                while right_first_try < len(seats_map[row]):
                    if seats_map[row][right_first_try] == "#":
                        occupied += 1
                        break
                    elif seats_map[row][right_first_try] == "L":
                        break
                    right_first_try += 1

                # Update setting status
                if seats_map[row][seat_position] == "L" and occupied == 0:
                    aux_seats_map[row][seat_position] = "#"
                    internal_stable = False
                    continue
                if seats_map[row][seat_position] == "#" and occupied >= 5:
                    aux_seats_map[row][seat_position] = "L"
                    internal_stable = False
                    continue
        if internal_stable:
            # If we get here it means no seats have changed, it's stable
            seats_map = aux_seats_map
            seats_stable = True

    # Count the seats
    return count_occupied_seats(seats_map)


def count_occupied_seats(puzzle: list) -> int:
    occupied_seats = 0
    for row in puzzle:
        for seat in row:
            if seat == "#":
                occupied_seats += 1
    return occupied_seats


if __name__ == '__main__':
    puzzle_input = reader.read_file('adventofcode/inputs/day11.txt')
    solve_part_one(puzzle_input)
    solve_part_two(puzzle_input)
