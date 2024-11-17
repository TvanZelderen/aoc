import argparse
import importlib
from datetime import datetime
from pathlib import Path
from time import perf_counter

def get_default_day():
    """Get current day in December, or 1 if not December."""
    today = datetime.now()
    return today.day if today.month == 12 else 1

def run_solution(year: int, day: int, use_example: bool = False):
    """Run a specific day's solution."""
    # Import solution module
    try:
        module = importlib.import_module(f"solutions.year{year}.day{day:02d}")
    except ImportError as e:
        print(f"Could not find solution for year {year} day {day}")
        return

    # Get input data
    if use_example:
        if not hasattr(module, "EXAMPLE_INPUT"):
            print(f"No example input found for year {year} day {day}")
            return
        data = module.EXAMPLE_INPUT
    else:
        try:
            input_file = Path("inputs") / str(year) / f"day{day:02d}.txt"
            data = input_file.read_text().strip()
        except FileNotFoundError:
            print(f"No input file found at {input_file}")
            return

    # Run solutions
    start = perf_counter()
    for part in (1, 2):
        part_func = getattr(module, f"part{part}", None)
        if part_func:
            try:
                result = part_func(data)
                elapsed = perf_counter() - start
                print(f"Part {part}: {result} ({elapsed:.3f}s)")
            except Exception as e:
                print(f"Error in part {part}: {e}")
        else:
            print(f"Part {part} not implemented")

def main():
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions")
    parser.add_argument("--year", type=int, default=datetime.now().year,
                       help="Year of puzzle (default: current year)")
    parser.add_argument("--day", type=int, default=get_default_day(),
                       help="Day of puzzle (default: current day in December, or 1)")
    parser.add_argument("--example", action="store_true",
                       help="Use example input instead of puzzle input")
    
    args = parser.parse_args()
    run_solution(args.year, args.day, args.example)

if __name__ == "__main__":
    main()