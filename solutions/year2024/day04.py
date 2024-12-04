EXAMPLE_INPUT = """
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
""".strip()

def parse_grid(data: str):
    return [[char for char in line] for line in data.splitlines()]

def compass_search(grid, r, c):
    directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    xmas = 0
    for direction in directions:
        x, y = direction
        try:
            if grid[r+x][c+y] != "M":
                continue
            if grid[r+2*x][c+2*y] != "A":
                continue
            if grid[r+3*x][c+3*y] != "S":
                continue
            if r+3*x < 0 or c+3*y < 0:
                continue
            xmas += 1
        except IndexError:
            pass
    return xmas
            

def part1(data: str):
    """Solution for part 1."""
    grid = parse_grid(data)
    xmas = 0
    for x, r in enumerate(grid):
        for y, c in enumerate(r):
            if c == "X":
                xmas += compass_search(grid, x, y)
    return xmas

def part2(data: str):
    """Solution for part 2."""
    grid = parse_grid(data)
    xmas = 0
    directions = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
    for x, r in enumerate(grid):
        for y, c in enumerate(r):
            if c == "A":
                valid = 0
                for direction in directions:
                    a, b = direction
                    try:
                        if (x+a or y+b or x-a or y-b) <= 0:
                            continue
                        if grid[x+a][y+b] == "M" and grid[x-a][y-b] == "S":
                            valid += 1
                    except IndexError:
                        pass
                if valid == 2:
                    xmas += 1
    return xmas