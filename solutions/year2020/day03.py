from utils import common_functions
import numpy as np

EXAMPLE_INPUT = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".strip()

# Expected results for example input
EXAMPLE_RESULT_1 = 7  # Replace with actual expected result
EXAMPLE_RESULT_2 = 336  # Replace with actual expected result when implementing part 2

# def parse_input(data: str) -> list:
#     """Parse input string into desired format."""
#     return [int(x) for x in data.splitlines()]

def part1(data: str):
    """Solution for part 1."""
    grid = common_functions.parse_grid(data)
    y_pos = 0
    trees = 0
    for row in grid:
        if row[y_pos] == "#":
            trees += 1
        y_pos += 3
        if y_pos >= len(row):
            y_pos -= len(row)
    return trees

def part2(data: str):
    """Solution for part 2."""
    grid = common_functions.parse_grid(data)
    routes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    outcomes = []
    odd = False
    for right, down in routes:
        y_pos = 0
        trees = 0
        for i, row in enumerate(grid):
            if down == 2:
                if odd:
                    odd = not(odd)
                    continue
                else:
                    odd = not(odd)
            if row[y_pos] == "#":
                trees += 1
            y_pos += right
            if y_pos >= len(row):
                y_pos = y_pos % len(row)
        outcomes.append(trees)
    print(outcomes)
    return np.prod(outcomes)