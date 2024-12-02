EXAMPLE_INPUT = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip()

# Expected results for example input
EXAMPLE_RESULT_1 = 2  # Replace with actual expected result
EXAMPLE_RESULT_2 = 4  # Replace with actual expected result when implementing part 2

def parse_input(data: str) -> list:
    """Parse input string into desired format."""
    return [[int(x) for x in line.split()] for line in data.splitlines()]

from itertools import pairwise

def check_safe(line: list[int]) -> bool:
    if not(line == sorted(line) or line[::-1] == sorted(line)):
        return False
    if not(all((1 <= abs(a - b) <= 3) for a, b in pairwise(line))):
        return False
    return True
    

def part1(data: str):
    """Solution for part 1."""
    lines = parse_input(data)
    safe_lines = 0
    for line in lines:
        if check_safe(line):
            safe_lines += 1
    return safe_lines

def part2(data: str):
    """Solution for part 2."""
    lines = parse_input(data)
    safe_lines = 0
    for line in lines:
        #Slicing to skip one index
        if any(check_safe(line[:i] + line[i + 1 :]) for i in range(len(line))):
            safe_lines += 1
    return safe_lines

