from pathlib import Path

EXAMPLE_INPUT = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip()

def parse_lines(data: str):
    return [line for line in data.splitlines()]

def part1(data: str):
    """Solution for part 1."""
    data = parse_lines(data)
    area_height = len(data)
    area_width = len(data[0])
    guard_pos = []
    guard_running = True
    guard_direction = -1 + 0j
    positions = set()
    for row, line in enumerate(data):
        for col, c in enumerate(line):
            if c == "^":
                guard_pos = row + col*1j
    while guard_running:
        positions.add((guard_pos))
        next_position = guard_pos + guard_direction
        # print(guard_pos, next_position)
        if not 0 < guard_pos.real < area_width:
            guard_running = False
        if not 0 < guard_pos.imag < area_height:
            guard_running = False
        try:
            if data[int(next_position.real)][int(next_position.imag)] == "#":
                # print("Found #, turning")
                guard_direction *= -1j
                next_position = guard_pos + guard_direction
        except IndexError:
            guard_running = False
        guard_pos = next_position
    return len(positions)




def part2(data: str):
    """Solution for part 2."""
    data = parse_lines(data)
    area_height = len(data)
    area_width = len(data[0])
    obstacles = set()
    potential_obstacles = set()
    loops = set()
    guard_pos_start = 0
    for row, line in enumerate(data):
        for col, c in enumerate(line):
            if c == "^":
                guard_pos_start = row + col*1j
                continue
            if c == "#":
                obstacles.add((row, col))
            else:
                potential_obstacles.add((row, col))

    for row, col in potential_obstacles:
        guard_pos = guard_pos_start
        guard_running = True
        guard_direction = -1 + 0j
        positions = set()
        
        while guard_running:
            next_position = guard_pos + guard_direction
            if (guard_pos, guard_direction) in positions:
                # if row == 25 and col == 23:
                #     print(f"Back again, {guard_pos},{guard_direction}")
                loops.add((row, col))
                break
            positions.add((guard_pos, guard_direction))
            if not 0 < guard_pos.real < area_height:
                break
            if not 0 < guard_pos.imag < area_width:
                break
            # try:
            if ((next_position.real, next_position.imag) in obstacles) or (next_position.real == row and next_position.imag == col):
                guard_direction *= -1j
                next_position = guard_pos + guard_direction
            if ((next_position.real, next_position.imag) in obstacles) or (next_position.real == row and next_position.imag == col):
                guard_direction *= -1j
                next_position = guard_pos + guard_direction
            # except IndexError:
            #     guard_running = False
            guard_pos = next_position
    return len(loops)