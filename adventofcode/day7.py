from adventofcode.inputs import reader
import re


def solve_part_one(puzzle: list) -> int:
    my_bag = "shiny gold"
    bag_colour_matcher = re.compile("((?:\\w+\\s){1,2})(?:bags|bag)")
    rules = {}

    for line in puzzle:
        matches = bag_colour_matcher.findall(line)
        matches = [aux.strip() for aux in matches]
        # Transform into dict
        for pos in range(0, len(matches)):
            if pos == 0:
                rules[matches[pos]] = []
                continue
            rules[matches[0]].append(matches[pos])

    # Go and try to find all matches for my bag
    bags_allowed = []
    bags_to_search = []

    # First search direct matches
    for key, values in rules.items():
        if key == my_bag:
            continue
        if my_bag in values:
            bags_allowed.append(key)
            bags_to_search.append(key)
            continue
    # Continue to search, keep adding potential lookups into the list
    while len(bags_to_search) > 0:
        for bag in bags_to_search:
            for key, values in rules.items():
                if bag in values:
                    bags_allowed.append(key)
                    bags_to_search.append(key)
            bags_to_search.remove(bag)

    return len(set(bags_allowed))


def solve_part_two(puzzle: list) -> int:
    my_bag = "shiny gold"
    bag_colour_matcher = re.compile("(((?:\\w+\\s){1,2})(?:bags|bag))|((\\d\\s)((?:\\w+\\s){1,2})(?:bags|bag))")
    rules = {}

    for line in puzzle:
        matches = bag_colour_matcher.findall(line)  # This is now list of tuples due to regex changes
        for pos in range(0, len(matches)):
            sanitized_bag = matches[0][1].strip()
            if pos == 0:
                rules[sanitized_bag] = []
                continue
            rules[sanitized_bag].append(matches[pos][2])

    result = calculate_required_bags(rules, my_bag)
    return result


def calculate_required_bags(rules: dict, colour_to_search: list) -> int:
    total = 0
    for requirement in rules[colour_to_search]:
        if not requirement:
            return total
        amount = int(requirement[0])
        colour = requirement[2:len(requirement) - 4].strip()
        total += amount + (amount * calculate_required_bags(rules, colour))
    return total


if __name__ == '__main__':
    puzzle_input = reader.read_file('adventofcode/inputs/day7.txt')
    solve_part_one(puzzle_input)
    solve_part_two(puzzle_input)
