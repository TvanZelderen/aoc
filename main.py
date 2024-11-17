import argparse
import importlib
from datetime import datetime
from pathlib import Path
from time import perf_counter

def get_default_day():
    """Get current day in December, or 1 if not December."""
    today = datetime.now()
    return today.day if today.month == 12 else 1

def run_solution(year: int, day: int):
    """Run a specific day's solution, testing against example first."""
    # Import solution module
    try:
        module = importlib.import_module(f"solutions.year{year}.day{day:02d}")
    except ImportError as e:
        print(f"Could not find solution for year {year} day {day}")
        return

    # Verify we have example input and expected results
    if not hasattr(module, "EXAMPLE_INPUT"):
        print(f"No example input found for year {year} day {day}")
        return
    
    if not hasattr(module, "EXAMPLE_RESULT_1"):
        print("Missing EXAMPLE_RESULT_1 in solution file")
        return

    # Test against example input
    print("Testing against example input...")
    for part in (1, 2):
        part_func = getattr(module, f"part{part}", None)
        expected = getattr(module, f"EXAMPLE_RESULT_{part}", None)
        
        if part_func and expected is not None:
            try:
                result = part_func(module.EXAMPLE_INPUT)
                if result != expected:
                    print(f"Part {part} example test failed!")
                    print(f"Expected: {expected}")
                    print(f"Got: {result}")
                    return
                print(f"Part {part} example test passed!")
            except Exception as e:
                print(f"Error in part {part} example: {e}")
                return
        elif part_func:
            print(f"Part {part} has no example result defined")
    
    # Run with actual input
    print("\nRunning with puzzle input...")
    try:
        input_file = Path("inputs") / str(year) / f"day{day:02d}.txt"
        data = input_file.read_text().strip()
    except FileNotFoundError:
        print(f"No input file found at {input_file}")
        return

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
    parser.add_argument("day", nargs="?", type=int, default=get_default_day(),
                       help="Day to run (default: current day in December)")
    
    args = parser.parse_args()
    year = datetime.now().year
    
    run_solution(year, args.day)

if __name__ == "__main__":
    main()