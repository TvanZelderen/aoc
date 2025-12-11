EXAMPLE_INPUT = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".strip()

def parse_grid(data: str):
    return [[char for char in line] for line in data.splitlines()]

def compass_search(grid, r, c):
    directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    rolls = 0
    for direction in directions:
        x, y = direction
        try:
            if r+x == -1 or c+y == -1:
                continue
            if grid[r+x][c+y] == "@" :
                rolls += 1
        except IndexError:
            pass
    # print(f"Standby, we are checking. {r},{c}: {rolls}")
    return rolls

def part1(data: str):
    """Solution for part 1."""
    total = 0
    grid = parse_grid(data)
    marks = []
    for x, r in enumerate(grid):
        for y, c in enumerate(r):
            if c == "@":
                if compass_search(grid, x, y) < 4:
                    total += 1
                    marks.append((x, y))
    # for mark in marks:
    #     grid[mark[0]][mark[1]] = "x"
    # for row in grid:\
    #     print(row)
    return total

def part2(data: str):
    """Solution for part 2."""
    total = 0
    sweep_total = 1
    sweep = 0
    grid = parse_grid(data)
    marks = []
    while sweep_total > 0:
        sweep_total = 0
        for x, r in enumerate(grid):
            for y, c in enumerate(r):
                if c == "@":
                    if compass_search(grid, x, y) < 4:
                        sweep_total += 1
                        marks.append((x, y))
        # print(f"For sweep {sweep}, {sweep_total} rolls were removed")
        sweep += 1
        total += sweep_total
        for mark in marks:
            grid[mark[0]][mark[1]] = "."
        # for row in grid:
        #     print(row)
    return total