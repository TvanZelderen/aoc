EXAMPLE_INPUT = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""".strip()

def parse_blocks(data: str) -> list[list[str]]:
    """Parse input separated by blank lines.
    Example input:
    block1 line1
    block1 line2

    block2 line1
    """
    return [block.splitlines() for block in data.split('\n\n')]

def part1(data: str):
    """Solution for part 1."""
    data = parse_blocks(data)
    fresh_list = []
    for i, block in enumerate(data):
        if i == 0: # ranges
            for nums in block:
                l, r = map(int, nums.split("-"))
                fresh_list.append((l, r))
        elif i == 1: # ingredients
            total = 0
            for num in block:
                for fresh in fresh_list:
                    # print(fresh[0], int(num), fresh[1])
                    if fresh[0] <= int(num) <= fresh[1]:
                        total += 1
                        break
    return total

def add_range(ranges, new_range):
    new_start, new_end = new_range
    merged = [new_start, new_end]
    remaining = []
    
    for r in ranges:
        if new_start > r[1] or new_end < r[0]:
            remaining.append(r)

        else:
            # Overlap or adjacent, merge
            merged[0] = min(merged[0], r[0])
            merged[1] = max(merged[1], r[1])
    
    remaining.append(merged)
    return remaining
    

def part2(data: str):
    """Solution for part 2."""
    data = parse_blocks(data)
    ranges = []
    for i, block in enumerate(data):
        if i == 0: # ranges
            for nums in block:
                l, r = map(int, nums.split("-"))
                ranges = add_range(ranges, (l, r))

    total = sum((end + 1) - start for start, end in ranges)
    return total