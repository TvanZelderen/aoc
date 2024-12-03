import re

EXAMPLE_INPUT = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""".strip()

def parse_lines(data: str):
    return data.replace("\n", "")

def part1(data: str):
    """Solution for part 1."""
    data = parse_lines(data)
    pattern = re.compile(r"mul\(\d+,\d+\)")
    list_of_muls = pattern.findall(data)
    sum = 0
    for line in list_of_muls:
        a, b = (int(''.join(filter(str.isdigit, part.strip()))) for part in line.split(','))
        sum += a*b
    return sum

def part2(data: str):
    """Solution for part 2."""
    data = parse_lines(data)
    pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")
    list_of_muls = pattern.findall(data)
    sum = 0
    execute = True
    for line in list_of_muls:
        if line == "do()":
            execute = True
            continue
        if line == "don't()":
            execute = False
            continue
        if execute:
            a, b = (int(''.join(filter(str.isdigit, part.strip()))) for part in line.split(','))
            sum += a*b
    return sum