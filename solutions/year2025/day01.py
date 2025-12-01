EXAMPLE_INPUT = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""".strip()

pos = 50

def part1(data: str, pos: int = 50):
    lines = data.splitlines()
    password = 0
    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        if direction == "L":
            pos -= distance
        elif direction == "R":
            pos += distance
        else:
            print("whoah")

        pos = pos % 100

        if pos == 0:
            password += 1

        # print(f"The dial is rotated {direction}{distance} to point at {pos}")
    return password

def part2(data: str, pos: int = 50):
    lines = data.splitlines()
    crossing_right = 0
    crossing_left = 0
    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        if direction == "L":
            crossing_left += abs((pos - distance) // 100)
            pos_after = (pos - distance) % 100
            if pos == 0 and pos_after > 0:
                crossing_left -= 1
            elif pos > 0 and pos_after == 0:
                crossing_left += 1
            pos = pos_after
        elif direction == "R":
            crossing_right += (pos + distance) // 100
            pos = (pos + distance) % 100
        else:
            print("whoah")

    return crossing_right + crossing_left, crossing_right, crossing_left

