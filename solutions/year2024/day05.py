EXAMPLE_INPUT = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".strip()

def parse_lines(data: str):
    instructions = []
    updates = []

    data = [line for line in data.splitlines()]
    get_instructions = True

    for line in data:
        if not line:
            get_instructions = False
        elif get_instructions:
            a,b = line.split("|")
            instructions.append([a,b])
        else:
            updates.append([x for x in line.split(",")])
    return instructions, updates

def check_update(update, instructions):
    for a, b in instructions:
        try:
            if not(update.index(a) < update.index(b)):
                return False
        except ValueError:
            pass
    return True

def fix_update(update, instructions):
    for a, b in instructions:
        try:
            if (update.index(a) < update.index(b)):
                continue
            else:
                index_a = update.index(a)
                index_b = update.index(b)
                # print(update, a, index_a, b, index_b)
                update.pop(index_b)
                update.insert(index_a, b)
        except ValueError:
            pass
    return update

def part1(data: str):
    """Solution for part 1."""
    instructions, updates = parse_lines(data)
    valid_sum = 0
    for update in updates:
        if check_update(update, instructions):
            valid_sum += int(update[len(update) // 2])
            # print(update[len(update) // 2])
    return valid_sum

def part2(data: str):
    """Solution for part 2."""
    instructions, updates = parse_lines(data)
    valid_sum = 0
    for update in updates:
        if not check_update(update, instructions):
            valid_update = False
            # print(f"Before fix: {update}")
            while not valid_update:
                update = fix_update(update, instructions)
                # print(f"After fix: {update}")
                if check_update(update, instructions):
                    valid_update = True
            
            valid_sum += int(update[len(update) // 2])
            # print(update[len(update) // 2])
    return valid_sum