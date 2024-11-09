"""
Advent of Code solution runner that executes solutions for specific days and years.
Supports both example and actual input data with execution time tracking.
"""

import argparse
import importlib
from pathlib import Path
from time import perf_counter
from typing import Optional


class AdventRunner:
    """Handles execution of Advent of Code solutions."""

    def __init__(self, year: int, day: int, use_example: bool = False):
        """
        Initialize the runner with specific year and day.

        Args:
            year: The year of the Advent of Code challenge
            day: The day of the challenge
            use_example: Whether to use example input data instead of actual input
        """
        self.year = year
        self.day = day
        self.use_example = use_example
        self.module = self._load_module()
        self.start_time = 0.0

    def _load_module(self):
        """Load the solution module for the specified year and day."""
        module_name = f"solutions.year{self.year}.day{self.day:02d}"
        try:
            return importlib.import_module(module_name)
        except ImportError as e:
            raise ImportError(f"Could not find solution module: {module_name}") from e

    def _read_input(self) -> str:
        """Read the input file for the specified year and day."""
        input_file = Path("inputs") / str(self.year) / f"day{self.day:02d}.txt"
        try:
            return input_file.read_text().strip()
        except FileNotFoundError as e:
            raise FileNotFoundError(
                f"Input file not found: {input_file}. "
                "Make sure it exists in the inputs directory."
            ) from e

    def _get_input_data(self) -> str:
        """Get the appropriate input data based on configuration."""
        if self.use_example:
            if not hasattr(self.module, "EXAMPLE_INPUT"):
                raise AttributeError(
                    f"No EXAMPLE_INPUT found in year {self.year} day {self.day} module"
                )
            return self.module.EXAMPLE_INPUT
        return self._read_input()

    def _run_part(self, part_num: int) -> Optional[str]:
        """
        Run a specific part of the day's solution.

        Args:
            part_num: The part number (1 or 2) to run

        Returns:
            Optional timing message if the part completed successfully
        """
        part_func = getattr(self.module, f"part{part_num}", None)
        if not part_func:
            return (
                f"Part {part_num} not implemented for year {self.year} day {self.day}"
            )

        try:
            part_func(self._get_input_data())
            elapsed = perf_counter() - self.start_time
            return (
                f"{self.year} day {self.day}, problem {part_num} "
                f"completed in {elapsed:.3f}s"
            )
        except KeyboardInterrupt:
            elapsed = perf_counter() - self.start_time
            return (
                f"{self.year} day {self.day}, problem {part_num} "
                f"cancelled after {elapsed:.3f}s"
            )
        except Exception as e:
            return f"Error in part {part_num}: {str(e)}"

    def run(self):
        """Execute both parts of the day's solution."""
        self.start_time = perf_counter()

        for part in (1, 2):
            result = self._run_part(part)
            if result:
                print(result)


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Run Advent of Code solutions for a specific day."
    )
    parser.add_argument(
        "year", type=int, help="The year of the Advent of Code challenge"
    )
    parser.add_argument("day", type=int, help="The day of the Advent of Code challenge")
    parser.add_argument(
        "--example",
        action="store_true",
        help="Use example input data instead of actual input",
    )
    return parser.parse_args()


def main():
    """Main entry point for the script."""
    args = parse_args()
    try:
        runner = AdventRunner(args.year, args.day, args.example)
        runner.run()
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
