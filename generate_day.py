import argparse
from pathlib import Path
from aocd import get_data
from datetime import date
from dotenv import load_dotenv
import os


def create_data_file(year, day):
    # Define the path to save the data
    data_file_path = Path(f"inputs/{year:04d}/day{day:02d}.txt")
    data_file_path.parent.mkdir(
        parents=True, exist_ok=True
    )  # Create directory if it doesn’t exist

    # Fetch the input data
    data = get_data(day=day, year=year)

    # Write the data to the file
    with data_file_path.open("w") as file:
        file.write(data)

    print(f"Data for {year}-Day {day} saved to {data_file_path}")


def create_solution_file(year, day):
    # Read the template content
    template_path = Path("template.py")
    template_content = template_path.read_text()

    # Replace placeholders in template
    template_content = template_content.replace("{year}", str(year))
    template_content = template_content.replace("{day}", str(day))

    # Define the path for the new file
    solution_file_path = Path(f"solutions/year{year}/day{day:02d}.py")
    solution_file_path.parent.mkdir(
        parents=True, exist_ok=True
    )  # Create directory if it doesn’t exist

    # Write the new file with replaced content
    solution_file_path.write_text(template_content)

    print(f"Created solution file for {year} Day {day} at {solution_file_path}")


def main():
    # load AoC cookie from .env file
    load_dotenv()
    session_cookie = os.getenv("AOC_SESSION")
    print(f"Session cookie: {session_cookie}")

    parser = argparse.ArgumentParser(
        description="Script for generating a new Advent of Code day."
    )
    parser.add_argument(
        "numbers", type=int, nargs='*',
        help="Year and day of the Advent of Code challenge"
    )
    
    args = parser.parse_args()
    
    if not args.numbers:
        # Generate the current date
        year, day = date.today().year, date.today().day
        create_data_file(year, day)
        create_solution_file(year, day)
    elif len(args.numbers) == 2:
        # Generate the requested date
        year, day = args.numbers
        create_data_file(year, day)
        create_solution_file(year, day)
    else:
        parser.error("Please provide either no arguments or both year and day")


if __name__ == "__main__":
    main()
