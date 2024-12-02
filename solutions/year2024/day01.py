EXAMPLE_INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
""".strip()

# Expected results for example input
EXAMPLE_RESULT_1 = 11  # Replace with actual expected result
EXAMPLE_RESULT_2 = 31  # Replace with actual expected result when implementing part 2

def parse_input(data: str) -> list[str]:
    """Parse input string into desired format."""
    return [x for x in data.splitlines()]

def process_numbers(data: str) -> tuple[list[int], list[int]]:
    """Parse and sort numbers from the input data."""
    numbers = parse_input(data)
    left_list = []
    right_list = []
    for line in numbers:
        left_num, right_num = line.split()
        left_list.append(int(left_num))
        right_list.append(int(right_num))
    left_list.sort()
    right_list.sort()
    return left_list, right_list

def part1(data: str) -> int:
    """Solution for part 1."""
    left_list, right_list = process_numbers(data)
    difference = sum(abs(ln - rn) for ln, rn in zip(left_list, right_list))
    return difference

from collections import Counter

def part2(data: str) -> int:
    """Solution for part 2 with improved performance."""
    left_list, right_list = process_numbers(data)
    
    right_counts = Counter(right_list)
    
    similarities = sum(number * right_counts[number] for number in left_list)
    # similarities = sum(number * right_list.count(number) for number in left_list)
    
    return similarities
