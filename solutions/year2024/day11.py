EXAMPLE_INPUT = """
0 1 10 99 999
""".strip()

from functools import cache
from collections import Counter
from collections import defaultdict

def blink(data: tuple):
    inserted = False
    for i, number in enumerate(data):
        if inserted:
            inserted = False
            continue
        if number == 0:
            data[i] = 1
            # print(data)
        elif len(str(number)) % 2 == 0:
            fh = int(str(number)[:int(len(str(number))/2)])
            sh = int(str(number)[int(len(str(number))/2):])
            # print(length, fh, sh)
            data[i] = fh
            data.insert(i+1, sh)
            inserted = True
        else:
            data[i] = number * 2024
    # print(data)
    return data

@cache
def cached_blink(number: int) -> tuple[int]:
    result = []
    if number == 0:
        result.append(1)
    elif len(str(number)) % 2 == 0:
        fh = int(str(number)[:int(len(str(number))/2)])
        sh = int(str(number)[int(len(str(number))/2):])
        result.append(fh)
        result.append(sh)
    else:
        result.append(number * 2024)
    return tuple(result)

def part1(data: str):
    """Solution for part 1."""
    data = [int(x) for x in data.split()]
    for _ in range(25):
        blink(data)
    return len(data)

def part2(data: str):
    """Solution for part 2."""
    data = [int(x) for x in data.split()]
    data = Counter(data)
    for i in range(25):
        blinked = defaultdict(int)
        for number, amount in data.items():
            for x in cached_blink(number):
                blinked[x] += amount
        data = blinked
        # print(f"{i+1}/75, keys: {len(data.keys())}, longest: {max(data.keys())}")
    return sum(data.values())