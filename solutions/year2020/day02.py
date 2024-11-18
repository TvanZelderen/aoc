from utils import common_functions

EXAMPLE_INPUT = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
""".strip()

# Expected results for example input
EXAMPLE_RESULT_1 = 2  # Replace with actual expected result
EXAMPLE_RESULT_2 = 1  # Replace with actual expected result when implementing part 2

def parse_input(data: str):
    """Parse input string into desired format."""
    results = []
    for line in data.splitlines():
        instructions, password = line.strip().split(":")
        values, key = instructions.strip().split(" ")
        min_val, max_val = map(int, values.split("-"))
        results.append((min_val, max_val, key.strip(), password.strip()))
    return results

def part1(data: str):
    """Solution for part 1."""
    valid_passwords = 0
    passwords = parse_input(data)
    for min_val, max_val, key, password in passwords:
        letter_count = common_functions.letter_count(password)
        if letter_count.get(key) == None:
             continue
        if int(letter_count.get(key)) >= min_val and int(letter_count.get(key)) <= max_val:
            valid_passwords += 1
    return valid_passwords

def part2(data: str):
    """Solution for part 2."""
    valid_passwords = 0
    passwords = parse_input(data)
    for min_val, max_val, key, password in passwords:
        # print(min_val, max_val, key, password, len(password))
        # print(password[min_val-1], password[max_val-1])
        if len(password) < min_val:
            continue
        if len(password) < max_val:
            if password[min_val-1] == key:
                valid_passwords += 1
                # print("Valid, longer")
        if password[min_val-1] == key and password[max_val-1] != key:
            valid_passwords += 1
            # print("Valid")
        if password[min_val-1] != key and password[max_val-1] == key:
            valid_passwords += 1
            # print("Valid")
    return valid_passwords
    # return None