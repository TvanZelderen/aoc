import argparse
import os
import importlib
from datetime import date
from pathlib import Path
from time import perf_counter
from aocd import get_data

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
        result, time_taken = run_part(module, part, test_input)
           
        # Format and print result
        print(f"Test part {part}:       {result}")

def setup_day(year: int, day: int):
    """Set up files for a specific day."""
    
    # Create directory structure
    input_dir = Path("inputs") / str(year)
    solution_dir = Path("solutions") / f"year{year}"
    
    input_dir.mkdir(parents=True, exist_ok=True)
    solution_dir.mkdir(parents=True, exist_ok=True)
    
    # Create __init__.py files
    Path("solutions/__init__.py").touch()
    (solution_dir / "__init__.py").touch()
    
    # Fetch and save input
    input_file = input_dir / f"day{day:02d}.txt"
    if not input_file.exists():
        try:
            puzzle_input = get_data(day=day, year=year)
            input_file.write_text(puzzle_input)
            print(f"✓ Fetched input for day {day}")
        except Exception as e:
            print(f"✗ Failed to fetch input: {e}")
            return False
    else:
        print(f"→ Input already exists: {input_file}")
    
    # Create solution file from template
    solution_file = solution_dir / f"day{day:02d}.py"
    if not solution_file.exists():
        template_file = Path("template.py")
        if not template_file.exists():
            print(f"✗ Template file not found: {template_file}")
            return False
        
        template_content = template_file.read_text()
        # Replace placeholders if any exist in your template
        content = template_content.replace("YEAR", str(year)).replace("DAY", str(day))
        solution_file.write_text(content)
        print(f"✓ Created solution template: {solution_file}")
        print(f"→ Paste example input into EXAMPLE_INPUT in {solution_file}")
    else:
        print(f"→ Solution file already exists: {solution_file}")
    
    return True

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
    parser.add_argument(
        "--setup", action="store_true",
        help="Set up files for a specific day (fetch input and create template)"
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

    if args.setup:
        print(f"Setting up Advent of Code {year} day {day}")
        print("-" * 40)
        setup_day(year, day)
    elif args.test:
        run_test(year, day)
    else:
        run_solution(year, day)

if __name__ == "__main__":
    main()
