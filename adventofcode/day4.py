from adventofcode.inputs import reader
import re


def solve_part_one(puzzle: list) -> int:
    valid_passports = 0
    passport = ""
    for entry in puzzle:
        if str(entry):
            passport = passport + entry + " "
            continue

        passport_fields = passport.rsplit()
        if len(passport_fields) == 8:
            # Automatically valid, has the necessary number of fields
            valid_passports += 1
            passport = ""
            continue

        if has_all_mandatory_fields(passport_fields):
            valid_passports += 1

        passport = ""
    return valid_passports


def solve_part_two(puzzle: list) -> int:
    valid_passports = 0
    passport = ""
    for entry in puzzle:
        if str(entry):
            passport = passport + entry + " "
            continue

        passport_fields = passport.rsplit()
        passport_valid = has_all_mandatory_fields(passport_fields)
        if not passport_valid:
            passport = ""
            continue

        # Field validation
        for field in passport_fields:
            split_field = field.split(":")
            if not is_field_valid(split_field):
                passport_valid = False
                break

        if passport_valid:
            valid_passports += 1

        passport = ""
    return valid_passports


def has_all_mandatory_fields(passport_fields: list) -> bool:
    mandatory_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    passport_fields_tags = [s.split(":")[0] for s in passport_fields]
    for mandatory_field in mandatory_keys:
        if mandatory_field not in passport_fields_tags:
            return False
    return True


def is_field_valid(field: list) -> bool:
    byr_pattern = re.compile("\\b(19[2-9][0-9]|200[0-2])\\b")
    iyr_pattern = re.compile("\\b(20([1][0-9]|20))\\b")
    eyr_pattern = re.compile("\\b(20([2][0-9]|30))\\b")
    height_pattern = re.compile("\\b(1([5-8][0-9]|[9][0-3])cm)|((59|6[0-9]|7[0-6])in)\\b")
    hair_color_pattern = re.compile("#[0-9a-f]{6}")
    eye_color_pattern = re.compile("amb|blu|brn|gry|grn|hzl|oth")
    passport_id_pattern = re.compile("\\b\\d{9}?\\b")

    if field[0] == "byr":
        return byr_pattern.search(field[1]) is not None
    if field[0] == "iyr":
        return iyr_pattern.search(field[1]) is not None
    if field[0] == "eyr":
        return eyr_pattern.search(field[1]) is not None
    if field[0] == "hgt":
        return height_pattern.search(field[1]) is not None
    if field[0] == "hcl":
        return hair_color_pattern.search(field[1]) is not None
    if field[0] == "ecl":
        return eye_color_pattern.search(field[1]) is not None
    if field[0] == "pid":
        return passport_id_pattern.search(field[1]) is not None
    if field[0] == "cid":
        return True

    return True


if __name__ == '__main__':
    puzzle_input = reader.read_file('adventofcode/inputs/day4.txt')
    solve_part_one(puzzle_input)
    solve_part_two(puzzle_input)
