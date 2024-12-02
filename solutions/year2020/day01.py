EXAMPLE_INPUT = """
1721
979
366
299
675
1456
""".strip()

from itertools import combinations

# Expected results for example input
EXAMPLE_RESULT_1 = 514579  # Replace with actual expected result
EXAMPLE_RESULT_2 = 241861950  # Replace with actual expected result when implementing part 2

def parse_input(data: str) -> list:
    """Parse input string into desired format."""
    return [int(x) for x in data.splitlines()]

def part1(data: str):
    """Solution for part 1."""
    numbers = parse_input(data)
    combs = list(combinations(numbers, 2))
    for a, b in combs:
        if a + b == 2020:
            return a * b

def part2(data: str):
    """Solution for part 2."""
    numbers = parse_input(data)
    combs = list(combinations(numbers, 3))
    for a, b, c in combs:
        if a + b + c == 2020:
            return a * b * c