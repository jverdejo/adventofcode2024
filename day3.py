import re

# regex:
# group 1 action
# group 2 compplete parentheses(empty or with numbers)
# group 3 empty parentheses
# group 4 complete parenetheses with numbers
# group 5 first argument inside parentheses
# group 6 second argument inside parentheses
# https://regex101.com/r/otek7l/2
regex = r"(don't|do|mul)((\(\))|(\((\d+),(\d+)\)))"

test_str = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

# Find all matches in text
matches = re.findall(regex, test_str)
total_part_1 = 0
total_part_2 = 0
enabled = True

for match in matches:
    action, _, empty, _, x, y = match
    # Use a flag to enbaled or disabled future muls
    if action == "do" and empty == "()":
        enabled = True
    elif action == "don't" and empty == "()":
        enabled = False
    elif action == "mul":
        total_part_1 += int(x) * int(y)
        if enabled:
            total_part_2 += int(x) * int(y)

print(f"Result part 1: {total_part_1}")
print(f"Result part 2: {total_part_2}")
