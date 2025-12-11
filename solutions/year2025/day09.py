EXAMPLE_INPUT = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".strip()

from collections import defaultdict

def part1(data: str):
    """Solution for part 1."""
    data = [line for line in data.splitlines()]
    rectangles = []
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            ax, ay = map(int, data[i].split(","))
            bx, by = map(int, data[j].split(","))
            size = (abs(ax-bx)+1) * (abs(ay-by)+1)
            rectangles.append(size)

    rectangles.sort(reverse=True)
    return rectangles[0]

def is_green(point, vertical_walls_by_bucket, horizontal_walls_by_bucket):
    px, py = point
    
    # Check horizontal walls (only relevant buckets)
    py_bucket = py // 1000
    for wy, (x_min, x_max) in horizontal_walls_by_bucket[py_bucket]:
        if wy == py and x_min <= px <= x_max:
            return True
    
    # Check if on vertical wall (only relevant bucket)
    px_bucket = px // 1000
    for wx, (y_min, y_max) in vertical_walls_by_bucket[px_bucket]:
        if wx == px and y_min <= py <= y_max:
            return True
    
    # Ray casting: check ALL buckets to the right of px
    walls_crossed = 0
    for bucket in vertical_walls_by_bucket:
        if bucket >= px_bucket:  # Only check buckets at or to the right
            for wx, (y_min, y_max) in vertical_walls_by_bucket[bucket]:
                if wx > px and y_min <= py < y_max:
                    walls_crossed += 1
    
    return walls_crossed % 2 == 1

def part2(data: str):
    """Solution for part 2."""
    # print("Starting part 2...")
    data = [line for line in data.splitlines()]
    vertical_walls = defaultdict(list)
    horizontal_walls = defaultdict(list)
    # Pair each point with the next (wrapping around to start)
    for (ax, ay), (bx, by) in zip(
        [tuple(map(int, point.split(","))) for point in data],
        [tuple(map(int, point.split(","))) for point in data[1:] + data[:1]]
    ):
        if ax == bx: # Vertical line
            bucket = ax // 1000
            vertical_walls[bucket].append((ax, (min(ay, by), max(ay, by)))) # x, y_min - y_max
        if ay == by: # Horizontal line
            bucket = ay // 1000
            horizontal_walls[bucket].append((ay, (min(ax, bx), max(ax, bx)))) # y, x_min - x_max

    
    # print("Walls created...")
    rectangles = []
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            ax, ay = map(int, data[i].split(","))
            bx, by = map(int, data[j].split(","))
            size = (abs(ax-bx)+1) * (abs(ay-by)+1)
            rectangles.append((size, (ax, ay), (bx, by)))

    rectangles.sort(reverse=True) # Let's run this from largest to smallest
    # print("Rectangles created and sorted...")
    # print(f"There are {len(rectangles)} rectangles")

    for i, rectangle in enumerate(rectangles):
        if i < 49200:
            continue
        # if i % 10 == 0:
        #     print(f"i: {i}")
        # print(f"Checking rectangle {rectangle}")
        size, (ax, ay), (bx, by) = rectangle
        min_x, max_x = min(ax, bx), max(ax, bx)
        min_y, max_y = min(ay, by), max(ay, by)

        # Top and bottom edges
        valid = True
        for x in range(min_x, max_x + 1):
            # print(f"x: {x}")
            if not is_green((x, min_y), vertical_walls, horizontal_walls):
                valid = False
                break
            if not is_green((x, max_y), vertical_walls, horizontal_walls):
                valid = False
                break

        # Left and right edges (excluding corners to avoid double-checking)
        for y in range(min_y + 1, max_y):
            # print(f"y: {y}")
            if not is_green((min_x, y), vertical_walls, horizontal_walls):
                valid = False
                break
            if not is_green((max_x, y), vertical_walls, horizontal_walls):
                valid = False
                break
        
        if valid:
            return size
        
    return "That didn't work"