EXAMPLE_INPUT = """
987654321111111
811111111111119
234234234234278
818181911112111
""".strip()

from itertools import combinations

def part1(data: str):
    """Solution for part 1."""
    data = [line for line in data.splitlines()]
    total = 0
    for line in data:
        values = [int(''.join(x)) for x in combinations(str(line), 2)]
        total += max(values)
    return total

def get_max_n_digits(line, n):
    result = []
    start = 0
    
    for position in range(n):
        # Calculate how far we can search while leaving enough digits
        remaining_needed = n - position - 1
        end = len(line) - remaining_needed
        
        # Find the maximum digit in the valid range
        max_digit = '0'
        max_index = start
        for i in range(start, end):
            if line[i] > max_digit:  # String comparison works for digits, so I stopped converting
                max_digit = line[i]
                max_index = i
        
        result.append(max_digit)
        start = max_index + 1
        
    return ''.join(result)

def part2(data: str):
    """Solution for part 2."""
    lines = data.splitlines()
    return sum(int(get_max_n_digits(line, 12)) for line in lines)