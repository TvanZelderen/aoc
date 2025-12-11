EXAMPLE_INPUT = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".strip()

def swap_index(items, value, insert):
    index = items.index(value)
    items[index:index+1] = insert
    return items

def swap_dict_index(items, value, insert):
    amount = items[value]
    l, r = insert
    if l in items:
        items[l] += amount
    else:
        items[l] = amount
    if r in items:
        items[r] += amount
    else:
        items[r] = amount
    items.pop(value)
    return items

def part1(data: str):
    """Solution for part 1."""
    data = [line for line in data.splitlines()]
    beams = set()
    splits = 0
    for row in data:
        # print(row)
        for i, c in enumerate(row):
            if c == "S":
                beams.add(i)
                # print(f"Start found at {i}")
            if c == "^" and i in beams:
                # print("Crossing found!")
                # print(beams)
                beams = swap_index(list(beams), i, (i-1, i+1))
                beams = set(beams)
                splits += 1

        # print(beams)
    return splits

def part2(data: str):
    """Solution for part 2."""
    data = [line for line in data.splitlines()]
    beams = {}
    for row in data:
        for i, c in enumerate(row):
            if c == "S":
                beams[i] = 1
            if c == "^" and i in beams:
                beams = swap_dict_index(beams, i, (i-1, i+1))
    return sum(beams.values())