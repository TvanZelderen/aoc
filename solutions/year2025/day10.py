EXAMPLE_INPUT = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""".strip()

import re
from itertools import combinations

def flip_switches(code, buttons):
    rack = [False]*len(code)
    for button in buttons:
        for d in button:
            rack[d] = not rack[d]
    return rack == code

def part1(data: str):
    """Solution for part 1."""
    data = [line for line in data.splitlines()]
    presses = 0
    for line in data:
        code = re.search(r'\[([.#]+)\]', line).group(1)
        code = list(map(lambda x: x == "#", code))
        buttons_re = re.findall(r'\(([^)]+)\)', line)
        buttons = [[int(digit) for digit in button.split(",")] for button in buttons_re]

        solved = False
        depth = 1
        while not solved:
            button_combinations = combinations(buttons, depth)
            for comb in button_combinations:
                if flip_switches(code, comb):
                    presses += depth
                    solved = True
                    # print(f"Solved {code}, {depth}")
                    break
            depth += 1
            # print(f"We are going deeper: {depth}")

    return presses

def part2(data: str):
    """Solution for part 2."""
    data = [line for line in data.splitlines()] 
    return None 