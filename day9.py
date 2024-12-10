import re

text = """2333133121414131402"""


def check_ordered(disk_block: list):
    total_empty = disk_block.count(".")
    expected_first_empty = len(disk_block) - total_empty
    return disk_block.index(".") == expected_first_empty


total_part_1 = 0
total_part_2 = 0

disk_map = list(text)

disk_block = []
id = 0
empty_block = False

# Go through each digit in disk map
for digit in disk_map:

    # Add the number of the digit of .(empty block) or file id
    for _ in range(int(digit)):
        if empty_block:
            disk_block.append(".")
        else:
            disk_block.append(id)

    # If file writted increment if
    if not empty_block:
        id += 1

    # Alternate between empty block and file
    empty_block = not empty_block


for i in range(len(disk_block), 0, -1):
    if check_ordered(disk_block):
        break

    # Get first palce of empty
    first_empty = disk_block.index(".")

    # Alternate position with file and first empty
    disk_block[first_empty] = disk_block[i - 1]
    disk_block[i - 1] = "."

# Final count 
for i in range(disk_block.index(".")):
    total_part_1 += i * int(disk_block[i])


print(f"Result part 1: {total_part_1}")
print(f"Result part 2: {total_part_2}")
