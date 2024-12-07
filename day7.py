import re

text = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

OPERATORS_PART1 = ["*", "+"]
OPERATORS_PART2 = ["*", "+", "||"]


def change_operator(operators, i, operators_list: list):
    index = operators_list.index(operators[i])
    if index == len(operators_list)-1:
        operators[i] = operators_list[0]
    else:
        operators[i] = operators_list[index+1]
    return operators


def apply_operation(operator, x, y):
    if operator == "*":
        return x*y
    elif operator == "+":
        return x+y
    else:
        return int(str(x)+str(y))


def search_operations(result, values: list, operators_list) -> bool:
    # with 2 operators, 4 values: 2^3 posibilities
    total_posibilities = len(operators_list)**(len(values)-1)

    # Number of oeprator availables
    operators = [operators_list[0]]*(len(values)-1)
    for i in range(total_posibilities):
        total = values[0]
        for j, operator in enumerate(operators):
            # Change operator?
            if i % (len(operators_list)**j) == 0:
                operators = change_operator(operators, j, operators_list)

            # Make operation
            total = apply_operation(operator, total, values[j+1])

        # If posibility found return true
        if total == int(result):
            return True

    return False


total_part_1 = 0
total_part_2 = 0

regex = r"(\d+): (.+)"

matches = re.findall(regex, text)

for match in matches:
    result, values = match
    if search_operations(result, [int(s) for s in values.split(" ")], OPERATORS_PART1):
        total_part_1 += int(result)
    if search_operations(result, [int(s) for s in values.split(" ")], OPERATORS_PART2):
        total_part_2 += int(result)


print(f"Result part 1: {total_part_1}")
print(f"Result part 2: {total_part_2}")
