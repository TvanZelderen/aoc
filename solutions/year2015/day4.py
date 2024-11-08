import hashlib

puzzle_input = "bgvyzdsv"
test_input = "pqrstuv"

for i in range(2000000):
    m = hashlib.md5()
    string = (f"{puzzle_input}{i}")
    encoded_string = string.encode('utf-8')
    m.update(encoded_string)
    if m.hexdigest().startswith("000000"):
        print(f"Solution found at {i}.")
        break

    
