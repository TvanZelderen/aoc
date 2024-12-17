from itertools import groupby

EXAMPLE_INPUT = """
2333133121414131402
""".strip()

def part1(data: str):
    """Solution for part 1."""
    data = [int(x) for x in data]
    blocks = data[::2]
    ids = [id for id in range(len(blocks))]
    empty = data[1::2]
    # print(blocks, ids, empty)
    array = []
    empties = []
    for i, id in enumerate(ids):
        array.extend([id] * blocks[i])
        empties.extend([0] * blocks[i])
        try:
            empties.extend([1] * empty[i])
        except IndexError:
            pass

    print(array)
    print(empties)

    for i, x in enumerate(empties):
        if x:
            array.insert(i, array.pop())
            # print(array)

    return sum([x*i for i, x in enumerate(array)])



def part2(data: str):
    """Solution for part 2."""
    data = [int(x) for x in data]
    blocks = data[::2]
    ids = [id for id in range(len(blocks))]
    empty = data[1::2]

    array = []
    empties = []
    files = []
    for i, id in enumerate(ids):
        array.extend([id] * blocks[i])
        empties.extend([0] * blocks[i])
        files.extend([id] * blocks[i])
        try:
            empties.extend([1] * empty[i])
            files.extend(["."] * empty[i])
        except IndexError:
            pass

    print(files)
    length = 1
    for char in range(len(files)):
        if files[char] == ".":
            continue
        if files[::-1][char] == files[::-1][char + 1]:
            length += 1
        else:
            print(length)
            break