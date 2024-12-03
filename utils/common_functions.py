import re
import itertools
import math

def parse_grid(data: str):
    """Parse a grid
    Example input:
    123
    456
    789
    Output:
    Column, Row
    """
    return [[char for char in line] for line in data.splitlines()]

def parse_coordinates(data: str) -> list[complex]:
    """Parse coordinate pairs as complex numbers.
    
    Example input:
    0,9
    5,9
    
    Returns a list of complex numbers where:
    - real part represents x coordinate
    - imaginary part represents y coordinate
    """
    return [complex(int(x), int(y)) for line in data.splitlines() 
            for x, y in [line.split(',')]]

def parse_blocks(data: str) -> list[list[str]]:
    """Parse input separated by blank lines.
    Example input:
    block1 line1
    block1 line2

    block2 line1
    """
    return [block.splitlines() for block in data.split('\n\n')]

def parse_key_value(data: str) -> dict[str, int]:
    """Parse key-value pairs.
    Example input:
    key1: 123
    key2: 456
    """
    result = {}
    for line in data.splitlines():
        key, value = line.split(': ')
        result[key] = int(value)
    return result

def letter_count(string: str):
    letter_count = {}
    for letter in string:
        letter_count[letter] = letter_count.get(letter,0)+1
    return letter_count

def skip_index(line: list):
    return ((line[:i] + line[i + 1:]) for i in range(len(line)))

def parse_integers(s: str) -> list[int]:
    """
    Extract all integers from a string, including negative numbers.
    
    Examples:
    parse_integers("Day 1: 83 -4 26") -> [1, 83, -4, 26]
    parse_integers("Temperature: -5 degrees") -> [-5]
    """
    return [int(num) for num in re.findall(r'-?\d+', s)]

def sliding_window(iterable, window_size):
    """
    Create sliding windows of a specified size over an iterable.
    
    Examples:
    list(sliding_window([1,2,3,4,5], 3)) -> [(1,2,3), (2,3,4), (3,4,5)]
    """
    it = iter(iterable)
    window = tuple(itertools.islice(it, window_size))
    if len(window) == window_size:
        yield window
    for elem in it:
        window = window[1:] + (elem,)
        yield window

def lcm(a: int, b: int) -> int:
    """
    Calculate Least Common Multiple of two numbers.
    
    Example:
    lcm(4, 6) -> 12
    """
    return abs(a * b) // math.gcd(a, b)

def intersection_of_sets(a: set, b: set) -> set:
    return a & b

if __name__ == "__main__":
    pass