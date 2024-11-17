EXAMPLE_INPUT = """
1000
2000

3000
4000

5000
6000
""".strip()

def parse_input(data: str) -> list:
    """Parse input string into desired format."""
    return [int(x) for x in data.split("\n") if x.strip()]

def part1(data: str):
    """Solution for part 1."""
    numbers = parse_input(data)
    return None

def part2(data: str):
    """Solution for part 2."""
    numbers = parse_input(data)
    return None