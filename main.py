import argparse
import importlib
from datetime import date
from pathlib import Path
from time import perf_counter

def run_part(module, part_num, data, expected=None):
    """Run a single part of the solution, returns (result, time_taken, passed)"""
    part_func = getattr(module, f"part{part_num}", None)
    if not part_func:
        return None, 0, False

    start = perf_counter()
    # try:
    result = part_func(data)
    time_taken = perf_counter() - start
    passed = (result == expected) if expected is not None else None
    return result, time_taken, passed
    # except Exception as e:
    #     print(f"Error in part {part_num}: {str(e)}")  # More helpful error message
    #     return None, 0, False

def run_solution(year: int, day: int):
    """Run a specific day's solution."""
    try:
        module = importlib.import_module(f"solutions.year{year}.day{day:02d}")
    except ImportError:
        print(f"Could not find solution for year {year} day {day}")
        return

    print(f"Advent of Code {year} day {day:02d}")

    # Load inputs and expected results
    try:
        input_file = Path("inputs") / str(year) / f"day{day:02d}.txt"
        puzzle_input = input_file.read_text().strip()
    except FileNotFoundError:
        print(f"No input file found at {input_file}")
        return

    example_input = getattr(module, "EXAMPLE_INPUT", None)
    
    # Run parts
    for part in (1, 2):
        expected = getattr(module, f"EXAMPLE_RESULT_{part}", None)
        
        # Run example if available
        if example_input and expected is not None:
            example_result, _, example_passed = run_part(module, part, example_input, expected)
            if example_result is None:
                continue  # Part not implemented
        else:
            example_passed = None  # No example available
            
        # Run actual input
        result, time_taken, _ = run_part(module, part, puzzle_input)
        if result is None:
            continue  # Part not implemented
            
        # Skip part 2 if explicitly signaled
        if part == 2 and result is None:
            continue
            
        # Format and print result
        example_status = "passed" if example_passed else "failed" if example_passed is False else "no test"
        print(f"Part {part}: example {example_status:<10} result: {result} ({time_taken:.3f}s)")

def main():
    parser = argparse.ArgumentParser(
        description="Run Advent of Code solutions.",
        epilog="If no arguments are provided, runs the current day's solution."
    )
    parser.add_argument(
        "numbers", type=int, nargs='*',
        help="Year and day (e.g., 2023 5), defaults to current date"
    )
    
    args = parser.parse_args()
    
    if not args.numbers:
        today = date.today()
        if today.month != 12 or today.day > 25:
            print("Note: Not running during Advent, defaulting to day 1")
            day = 1
        else:
            day = today.day
        year = today.year
    elif len(args.numbers) == 2:
        year, day = args.numbers
        if year < 2015 or year > date.today().year:
            parser.error("Invalid year: Advent of Code started in 2015")
        if day < 1 or day > 25:
            parser.error("Invalid day: must be between 1 and 25")
    else:
        parser.error("Please provide either no arguments or both year and day")

    run_solution(year, day)

if __name__ == "__main__":
    main()