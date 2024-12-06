text = """3   4
4   3
2   5
1   3
3   9
3   3"""
# Read text and conver in two list
right_list = []
left_list = []

for line in text.splitlines():
    left, right = line.split("   ")
    right_list.append(int(right))
    left_list.append(int(left))

# Sort lists
right_list = sorted(right_list)
left_list = sorted(left_list)

total = 0
similarity = 0
# Nor are ordered, only need to calcualate the difference with same index
for i in range(min(len(left_list), len(left_list))):
    total += abs(left_list[i] - right_list[i])

    # Part two
    # Use count to find how many are in right list
    similarity += left_list[i] * right_list.count(left_list[i])

print(f"Result part 1: {total}")
print(f"Result part 2: {similarity}")
