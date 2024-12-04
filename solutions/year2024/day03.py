import re

EXAMPLE_INPUT = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""".strip()

def parse_lines(data: str):
    return data.replace("\n", "")

def part1(data: str):
    """Solution for part 1."""
    data = parse_lines(data)
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    return sum(int(match[0]) * int(match[1]) for match in re.findall(pattern, data))

def part2(data: str):
    """Solution for part 2."""
    data = parse_lines(data)
    pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")
    sum = 0
    execute = True
    for match in pattern.findall(data):
        if match == "do()":
            execute = True
        elif match == "don't()":
            execute = False
        elif execute:
            x, y = map(int, match[4:-1].split(","))
            sum += x * y
    return sum