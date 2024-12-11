from collections import defaultdict
from itertools import combinations

EXAMPLE_INPUT = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".strip()

def part1(data: str):
    """Solution for part 1."""
    data = [line for line in data.splitlines()]
    frequencies = defaultdict(list)
    values = set()
    height = len(data)
    width = len(data[0])
    nodes = set()
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char != ".":
                frequencies[char].append([row, col])
                values.add((row, col))
    for key, value in frequencies.items():
        for a, b in combinations(value, 2):
            x_diff = b[0] - a[0]
            y_diff = b[1] - a[1]
            node_1 = (a[0] - x_diff, a[1] - y_diff)
            node_2 = (b[0] + x_diff, b[1] + y_diff)
            # print(node_1, node_2)
            if (node_1 not in values) and 0 <= node_1[0] < height and 0 <= node_1[1] < width:
                # print(f"Added node 1 {node_1}, {key}")
                nodes.add((node_1, key))
            if (node_2 not in values) and 0 <= node_2[0] < height and 0 <= node_2[1] < width:
                # print(f"Added node 2 {node_2}, {key}")
                nodes.add((node_2, key))
    return len(nodes), nodes


def part2(data: str):
    """Solution for part 2."""
    data = [line for line in data.splitlines()] 
    return None 