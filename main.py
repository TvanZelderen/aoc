import argparse
import importlib
from datetime import date
from pathlib import Path
from time import perf_counter

def run_part(module, part_num, data):
    """Run a single part of the solution, returns (result, time_taken, passed)"""
    part_func = getattr(module, f"part{part_num}", None)
    if not part_func:
        return None, 0, False
    start = perf_counter()
    result = part_func(data)
    time_taken = perf_counter() - start
    return result, time_taken

def run_solution(year: int, day: int):
    """Run a specific day's solution."""
    try:
        module = importlib.import_module(f"solutions.year{year}.day{day:02d}")
    except ImportError:
        print(f"Could not find solution for year {year} day {day}")
        return

    # Determine input file and expected results
    input_file = Path("inputs") / str(year) / f"day{day:02d}.txt"
    puzzle_input = input_file.read_text().strip()

    # Run parts
    for part in (1, 2):
        # Run part
        result, time_taken = run_part(module, part, puzzle_input)

        # Skip part 2 if explicitly signaled
        if part == 2 and result is None:
            continue
           
        # Format and print result
        print(f"Output part {part}:     {result} ({time_taken:.3f}s)")

def run_test(year: int, day: int):
    """Run a specific day's solution."""
    try:
        module = importlib.import_module(f"solutions.year{year}.day{day:02d}")
    except ImportError:
        print(f"Could not find solution for year {year} day {day}")
        return

    print(f"Advent of Code {year} day {day:02d}")
    print("--------------------------")

    # Determine input file and expected results
    test_input = getattr(module, "EXAMPLE_INPUT", None)

    # Run parts
    for part in (1, 2):

        # Run test
        result, _ = run_part(module, part, test_input)
           
        # Format and print result
        print(f"Test part {part}:       {result}")

def main():
    parser = argparse.ArgumentParser(
        description="Run Advent of Code solutions.",
        epilog="If no arguments are provided, runs the current day's solution."
    )
    parser.add_argument(
        "numbers", type=int, nargs='*',
        help="Year and day (e.g., 2023 5), defaults to current date"
    )
    parser.add_argument(
        "--test", action="store_true",
        help="Run with example input instead of puzzle input"
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
    if args.test:
        run_test(year, day)
    else:
        run_solution(year, day)

if __name__ == "__main__":
    main()
