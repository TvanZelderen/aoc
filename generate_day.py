import argparse
from pathlib import Path
from aocd import get_data


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
    # Setup command-line argument parsing
    parser = argparse.ArgumentParser(
        description="Generate Advent of Code files for a specific day."
    )
    parser.add_argument(
        "year", type=int, help="The year of the Advent of Code challenge"
    )
    parser.add_argument("day", type=int, help="The day of the Advent of Code challenge")

    args = parser.parse_args()

    # Generate both data file and solution file
    create_data_file(args.year, args.day)
    create_solution_file(args.year, args.day)


if __name__ == "__main__":
    main()
