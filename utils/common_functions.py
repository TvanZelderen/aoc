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