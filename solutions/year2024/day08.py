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
    rows = len(data)
    cols = len(data[0])

    antennas = {}

    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if char != ".":
                if char not in antennas: antennas[char] = []
                antennas[char].append((r, c))

    antinodes = set()

    for char, antenna in antennas.items():
        for i in range(len(antenna)):
            for j in range(i + 1, len(antenna)):
                r1, c1 = antenna[i]
                r2, c2 = antenna[j]
                # print(char, antenna[i], antenna[j], (r1 + (r1 - r2), c1 + (c1 - c2)), (r2 - (r1 - r2), c2 - (c1 - c2)))
                antinodes.add((r1 + (r1 - r2), c1 + (c1 - c2)))
                antinodes.add((r2 - (r1 - r2), c2 - (c1 - c2)))
    
    return len([(r, c) for r, c in antinodes if 0 <= r < rows and 0 <= c < cols])


def part2(data: str):
    """Solution for part 2."""
    data = [line for line in data.splitlines()]
    rows = len(data)
    cols = len(data[0])

    antennas = {}

    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if char != ".":
                if char not in antennas: antennas[char] = []
                antennas[char].append((r, c))

    antinodes = set()

    for char, antenna in antennas.items():
        for i in range(len(antenna)):
            for j in range(i + 1, len(antenna)):
                r1, c1 = antenna[i]
                r2, c2 = antenna[j]
                # print(char, antenna[i], antenna[j], (r1 + (r1 - r2), c1 + (c1 - c2)), (r2 - (r1 - r2), c2 - (c1 - c2)))
                dr = (r1 - r2)
                dc = (c1 - c2)
                multiplier = max(rows, cols)
                for mult in range(multiplier):
                    antinodes.add((r1 + mult * dr, c1 + mult * dc))
                    antinodes.add((r2 - mult * dr, c2 - mult * dc))
    
    return len([(r, c) for r, c in antinodes if 0 <= r < rows and 0 <= c < cols])