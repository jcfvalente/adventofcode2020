from adventofcode.inputs import reader
import math


def solve_part_one(puzzle: list) -> int:
    depart_time = int(puzzle[0])
    bus_ids = puzzle[1].split(",")
    bus_ids = [int(i) if i.isdigit() else 0 for i in bus_ids]
    depart_time_bus_schedule = {}

    for bus in bus_ids:
        if bus == 0:
            continue
        # Find the next time the bus comes after our departure time
        next_bus = math.ceil(depart_time / bus)
        depart_time_bus_schedule[bus] = next_bus * bus

    earliest_bus = 0
    for key, value in depart_time_bus_schedule.items():
        if earliest_bus == 0:
            earliest_bus = key
            continue
        if value - depart_time < depart_time_bus_schedule[earliest_bus] - depart_time:
            earliest_bus = key

    return (depart_time_bus_schedule[earliest_bus] - depart_time) * earliest_bus


def solve_part_two(puzzle: list) -> int:
    # Application of the Chinese Remainder Theorem
    bus_ids = puzzle[1].split(",")
    bus_ids = [int(i) if i.isdigit() else 0 for i in bus_ids]

    timestamps_to_leave = {}
    current_delay = 0
    n_max = 1
    # Find the time to leave related to t (t represents a certain time that bus_id[0] leaves)
    for pos in range(0, len(bus_ids)):
        if pos == 0:
            timestamps_to_leave[bus_ids[pos]] = 0
            current_delay += 1
            n_max = n_max * bus_ids[pos]
            continue
        if bus_ids[pos] == 0:
            current_delay += 1
            continue
        timestamps_to_leave[bus_ids[pos]] = bus_ids[pos] - current_delay
        current_delay += 1
        n_max = n_max * bus_ids[pos]

    ns_map = {}
    for key, value in timestamps_to_leave.items():
        ns_map[key] = calculate_ns(timestamps_to_leave, key)

    # Find the number to multiply value by so that the remainder is 1.
    # Update the product directly into the ns_map
    for key, value in ns_map.items():
        if value % key == 1:
            continue
        i = 2
        while True:
            value_temp = value * i
            if value_temp % key == 1:
                # i is the number to multiply by
                break
            i += 1
        ns_map[key] = value * i

    sum_value = 0
    for time in timestamps_to_leave:
        print(timestamps_to_leave[time] * ns_map[time])
        sum_value = sum_value + (timestamps_to_leave[time] * ns_map[time])

    return sum_value % n_max


def calculate_ns(timestamps_map: dict, key_to_calc: int) -> int:
    num = 1
    for key, value in timestamps_map.items():
        if key == key_to_calc:
            continue
        num = num * key
    return num


if __name__ == '__main__':
    puzzle_input = reader.read_file('adventofcode/inputs/day13.txt')
    solve_part_one(puzzle_input)
    solve_part_two(puzzle_input)
