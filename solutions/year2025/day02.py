EXAMPLE_INPUT = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
""".strip()

def part1(data: str):
    """Solution for part 1."""
    total = 0
    data = [line for line in data.split(",")]
    data = [line.split("-") for line in data]
    for l,r in data:
        # print(f"l: {l} and r: {r}")
        for i in range(int(l), int(r)+1):
            string = str(i)
            if len(string)%2 != 0:
                continue
            elif string[0] == 0:
                continue
            else:
                first = string[:len(string)//2]
                second = string[len(string)//2:]
                if first == second:
                    # print(first, second, "same!", i)
                    total += i
    return total

def principal_period(s):
    i = (s+s).find(s, 1, -1)
    return None if i == -1 else s[:i]

def part2(data: str):
    """Solution for part 2."""
    total = 0
    data = [line for line in data.split(",")]
    data = [line.split("-") for line in data]
    for l,r in data:
        # print(f"l: {l} and r: {r}")
        for i in range(int(l), int(r)+1):
            # print(f"i: {i}")
            if principal_period(str(i)):
                # print(principal_period(str(i)))
                total += i
    return total