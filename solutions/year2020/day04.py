EXAMPLE_INPUT = """
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
""".strip()

# Expected results for example input
EXAMPLE_RESULT_1 = 4  # Replace with actual expected result
EXAMPLE_RESULT_2 = 4  # Replace with actual expected result when implementing part 2

def parse_input(data: str) -> list:
    """Parse input string into desired format."""
    return [passport for passport in data.split("\n\n")]

def part1(data: str):
    """Solution for part 1."""
    passports = parse_input(data)
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    valid_passports = []
    for passport in passports:
        passport = passport.replace("\n", " ")
        passport_keys = {}
        for field in passport.split(" "):
            key, value = field.split(":")
            passport_keys[key] = value
        if required_keys.issubset(passport_keys):
            valid_passports.append(passport)
    return len(valid_passports)

def validate_birth_year(byr: str) -> bool:
    try:
        year = int(byr)
        return 1920 <= year <= 2002
    except ValueError:
        return False
    
def validate_issue_year(iyr: str) -> bool:
    try:
        year = int(iyr)
        return 2010 <= year <= 2020
    except ValueError:
        return False
    
def validate_expiration_year(eyr: str) -> bool:
    try:
        year = int(eyr)
        return 2020 <= year <= 2030
    except ValueError:
        return False

def validate_height(hgt: str) -> bool:
    try:
        if hgt.endswith("cm"):
            height = int(hgt[:-2])
            return 150 <= height <= 193
        elif hgt.endswith("in"):
            height = int(hgt[:-2])
            return 59 <= height <= 76
        return False
    except ValueError:
        return False
    
def validate_hair_color(hcl: str) -> bool:
    if not hcl.startswith("#") or len(hcl) != 7:
        return False
    valid_chars = set("0123456789abcdef")
    return all(c in valid_chars for c in hcl[1:])

def validate_eye_color(ecl: str) -> bool:
    valid_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    return ecl in valid_colors
    
def validate_passport_id(pid: str) -> bool:
    digits = set("0123456789")
    if  len(pid) != 9:
        return False
    return all(c in digits for c in pid)

def part2(data: str):
    """Solution for part 2."""
    passports = parse_input(data)
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    valid_passports = []
    for passport in passports:
        passport = passport.replace("\n", " ")
        passport_keys = {}
        for field in passport.split(" "):
            key, value = field.split(":")
            passport_keys[key] = value
        if required_keys.issubset(passport_keys):
            if not validate_birth_year(passport_keys["byr"]): # continue if birth year validation fails.
                continue
            if not validate_issue_year(passport_keys["iyr"]):
                continue
            if not validate_expiration_year(passport_keys["eyr"]):
                continue
            if not validate_height(passport_keys["hgt"]):
                continue
            if not validate_hair_color(passport_keys["hcl"]):
                continue
            if not validate_eye_color(passport_keys["ecl"]):
                continue
            if not validate_passport_id(passport_keys["pid"]):
                continue
            valid_passports.append(passport)
    return len(valid_passports)
    # return None