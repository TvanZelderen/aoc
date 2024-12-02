EXAMPLE_INPUT = """
FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
""".strip()

# Expected results for example input
EXAMPLE_RESULT_1 = 820  # Replace with actual expected result
EXAMPLE_RESULT_2 = 2000  # Replace with actual expected result when implementing part 2

def parse_input(data: str) -> list:
    """Parse input string into desired format."""
    return [x for x in data.splitlines()]

def split_list(unsplit_list: list) -> tuple:
    half = len(unsplit_list) // 2
    return unsplit_list[:half], unsplit_list[half:]
    

def find_row(seat: str) -> int:
    rows = [i for i in range(128)]
    for c in seat[:7]:
        if c == "F": # Take the lower half
            rows = split_list(rows)[0]
        if c == "B": # Take the upper half
            rows = split_list(rows)[1]
    return rows[0]

def find_column(seat: str) -> int:
    columns = [i for i in range(8)]
    for c in seat[7:]:
        if c == "L": # Take the lower half
            columns = split_list(columns)[0]
        if c == "R": # Take the upper half
            columns = split_list(columns)[1]
    return columns[0]

def find_seat_id(row: int, column: int) -> int:
    return row * 8 + column

def part1(data: str):
    """Solution for part 1."""
    highest_id = 0
    boarding_passes = parse_input(data)
    bsp = []
    for seats in boarding_passes:
        row = find_row(seats)
        column = find_column(seats)
        seat_id = find_seat_id(row, column)
        bsp.append([row, column, seat_id])
        # print(row, column, seat_id)
        if seat_id > highest_id:
            highest_id = seat_id
    # print(bsp)
    return highest_id

def part2(data: str):
    """Solution for part 2."""
    boarding_passes = parse_input(data)
    bsp = {}
    for seats in boarding_passes:
        row = find_row(seats)
        column = find_column(seats)
        seat_id = find_seat_id(row, column)
        bsp[seat_id] = (row)

    print(len(list(bsp.values())))

    

    for row in range(128):
        for rows in bsp.values():
            if row != rows:
                continue
            else:
                print(row, rows)
    
    return None