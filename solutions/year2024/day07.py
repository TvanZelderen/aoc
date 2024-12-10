import itertools

EXAMPLE_INPUT = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".strip()


def part1(data: str):
    """Solution for part 1."""
    data = [line for line in data.splitlines()]
    data = [line.split(":") for line in data]
    operations = ["+", "*"]
    result = []
    for total, numbers in data:
        total = int(total)
        numbers = [int(number) for number in numbers.split()]
        combinations = list(itertools.product(operations, repeat=len(numbers) - 1))

        for combination in combinations:
            # print(f"Combination: {combination}")
            calculation = numbers[0]
            # print(calculation)
            for i in range(len(combination)):
                # print(f"{calculation}{combination[i]}{numbers[i+1]}")
                # print(eval(f"{calculation}{combination[i]}{numbers[i+1]}"))
                calculation = eval(f"{calculation}{combination[i]}{numbers[i+1]}")
                if calculation > total:
                    continue
                
            if calculation == total:
                # print(total)
                result.append(total)
                break
    return sum(result)

def part2(data: str):
    """Solution for part 2."""
    data = [line for line in data.splitlines()]
    data = [line.split(":") for line in data]
    operations = ["+", "*", "||"]
    result = 0
    for total, numbers in data:
        total = int(total)
        numbers = [int(number) for number in numbers.split()]
        combinations = list(itertools.product(operations, repeat=len(numbers) - 1))
        print(len(combinations))

        for combination in combinations:
            # print(f"Combination: {combination}")
            calculation = numbers[0]
            # print(calculation)
            for i in range(len(combination)):
                # print(f"{calculation}{combination[i]}{numbers[i+1]}")
                # print(eval(f"{calculation}{combination[i]}{numbers[i+1]}"))
                if combination[i] == "||":
                    calculation = int(str(calculation)+str(numbers[i+1]))
                else:
                    calculation = eval(f"{calculation}{combination[i]}{numbers[i+1]}")
                
            if calculation == total:
                # print(total)
                result += total
                break
    return result