from adventofcode.inputs import reader


def solve_part_one(puzzle: list) -> int:
    ship_position = {
        "x": 0,
        "y": 0,
        "direction": "E"
    }

    left_turn = "ENWS"
    right_turn = "ESWN"

    for instruction in puzzle:
        if instruction[0] == "N":
            ship_position["y"] += int(instruction[1::])
            continue
        if instruction[0] == "S":
            ship_position["y"] -= int(instruction[1::])
            continue
        if instruction[0] == "E":
            ship_position["x"] += int(instruction[1::])
            continue
        if instruction[0] == "W":
            ship_position["x"] -= int(instruction[1::])
            continue
        if instruction[0] == "F":
            if ship_position["direction"] == "N":
                ship_position["y"] += int(instruction[1::])
                continue
            if ship_position["direction"] == "S":
                ship_position["y"] -= int(instruction[1::])
                continue
            if ship_position["direction"] == "E":
                ship_position["x"] += int(instruction[1::])
                continue
            if ship_position["direction"] == "W":
                ship_position["x"] -= int(instruction[1::])
                continue
        # Direction of the ship
        turns = int(instruction[1::]) / 90
        if instruction[0] == "L":
            future_direction = left_turn.find(ship_position["direction"]) + turns
            if future_direction > len(left_turn) - 1:
                future_direction = future_direction - len(left_turn)
            ship_position["direction"] = left_turn[int(future_direction)]

            continue
        if instruction[0] == "R":
            future_direction = right_turn.find(ship_position["direction"]) + turns
            if future_direction > len(right_turn) - 1:
                future_direction = future_direction - len(right_turn)
            ship_position["direction"] = right_turn[int(future_direction)]

            continue

    return abs(ship_position["x"]) + abs(ship_position["y"])


def solve_part_two(puzzle: list) -> int:
    ship = {
        "x": 0,
        "y": 0
    }
    # The waypoint's position is always relative to the ship
    # e.g the waypoint's (0,0) is always the ship's current position
    waypoint = {
        "x": 10,
        "y": 1
    }

    for instruction in puzzle:
        if instruction[0] == "N":
            waypoint["y"] += int(instruction[1::])
            continue
        if instruction[0] == "S":
            waypoint["y"] -= int(instruction[1::])
            continue
        if instruction[0] == "E":
            waypoint["x"] += int(instruction[1::])
            continue
        if instruction[0] == "W":
            waypoint["x"] -= int(instruction[1::])
            continue
        if instruction[0] == "F":
            # Move the ship
            value = int(instruction[1::])
            ship["x"] += value * waypoint["x"]
            ship["y"] += value * waypoint["y"]

        # Direction of the waypoint
        turns = int(instruction[1::]) / 90
        if instruction[0] == "L":
            if turns > 4:
                turns = turns - 4
            if turns == 1:
                temp = waypoint["x"]
                waypoint["x"] = waypoint["y"] * -1
                waypoint["y"] = temp
            elif turns == 2:
                waypoint["x"] = waypoint["x"] * -1
                waypoint["y"] = waypoint["y"] * -1
            elif turns == 3:
                temp = waypoint["x"]
                waypoint["x"] = waypoint["y"]
                waypoint["y"] = temp * -1
            elif turns == 4:
                continue
            continue
        if instruction[0] == "R":
            if turns > 4:
                turns = turns - 4
            if turns == 1:
                temp = waypoint["x"]
                waypoint["x"] = waypoint["y"]
                waypoint["y"] = temp * -1
            elif turns == 2:
                waypoint["x"] = waypoint["x"] * -1
                waypoint["y"] = waypoint["y"] * -1
            elif turns == 3:
                temp = waypoint["x"]
                waypoint["x"] = waypoint["y"] * -1
                waypoint["y"] = temp
            elif turns == 4:
                continue

    return abs(ship["x"]) + abs(ship["y"])


if __name__ == '__main__':
    puzzle_input = reader.read_file('adventofcode/inputs/day12.txt')
    solve_part_one(puzzle_input)
    solve_part_two(puzzle_input)
