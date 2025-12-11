EXAMPLE_INPUT = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""".strip()

from math import prod
from itertools import zip_longest

def part1(data: str):
    """Solution for part 1."""
    data = [line.split() for line in data.splitlines()]
    data = zip(*data)

    total = 0

    for row in data:
        if row[-1] == "+":
            nums = row[:-1]
            nums = map(int, nums)
            total += sum(nums)
        elif row[-1] == "*":
            nums = row[:-1]
            nums = map(int, nums)
            total += prod(nums)
    return total

def part2(data: str):
    """Solution for part 2."""
    data = [line for line in data.splitlines()]
    data = zip_longest(*data, fillvalue=' ')

    total = 0
    line = []

    for row in data:
        if all(s == " " for s in row):
            if operation == "sum":
                line.append("+")
            elif operation == "prod":
                line.append("*")
            else:
                print("invalid operation!")

            # print("A blank line was found!")
            # print(line)

            if line[-1] == "+":
                nums = line[:-1]
                nums = map(int, nums)
                sub = sum(nums)
                total += sub
                # print(sub)
            elif line[-1] == "*":
                nums = line[:-1]
                nums = map(int, nums)
                sub = prod(nums)
                total += sub
                # print(sub)
            line = []
        else:
            number = []
            for n in row:
                if n == " ":
                    continue
                elif n == "+":
                    operation = "sum"
                elif n == "*":
                    operation = "prod"
                else:
                    number.append(n)
            line.append(''.join(number))
    if operation == "sum":
        line.append("+")
    elif operation == "prod":
        line.append("*")
    else:
        print("invalid operation!")

    # print("The last line was found!")
    # print(line)

    if line[-1] == "+":
        nums = line[:-1]
        nums = map(int, nums)
        sub = sum(nums)
        total += sub
        # print(sub)
    elif line[-1] == "*":
        nums = line[:-1]
        nums = map(int, nums)
        sub = prod(nums)
        total += sub
        # print(sub)

    return total