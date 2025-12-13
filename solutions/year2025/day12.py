EXAMPLE_INPUT = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
""".strip()

def part1(data: str):
    """Solution for part 1."""
    blocks = [block.splitlines() for block in data.split('\n\n')]
    shapes = blocks[:-1]
    problems = blocks[-1]

    fits = 0
    for problem in problems:
        region, quantities = problem.split(":")
        quantities = list(map(int, quantities.split()))
        width, height = map(int, region.split("x"))
        avail_area = width * height
        req_area = quantities[4] // 2 * 16 + quantities[4] % 2 * 9 + sum(9*x for x in quantities[:4]) + quantities[-1] * 9
        if avail_area >= req_area:
            fits += 1
    return fits

def part2(data: str):
    """Solution for part 2."""
    data = [line for line in data.splitlines()] 
    return None 