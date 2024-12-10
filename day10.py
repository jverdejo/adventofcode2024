text = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def search_next(matrix, position: tuple, top_set: set):
    # Geta actual height
    height = matrix[position[0]][position[1]]
    global total_part_2
    if height == 9:
        # Part 1 how many tops are in the trailhead
        top_set.add(position)
        # Part 2 the number of total times we arrive to a top
        total_part_2+=1
        return

    next_height = height+1
    next_positions = []

    # Right
    if position[1] < len(matrix[0])-1 and matrix[position[0]][position[1]+1] == next_height:
        next_positions.append((position[0], position[1]+1))
    # Left
    if position[1] > 0 and matrix[position[0]][position[1]-1] == next_height:
        next_positions.append((position[0], position[1]-1))

     # Down
    if position[0] < len(matrix)-1 and matrix[position[0]+1][position[1]] == next_height:
        next_positions.append((position[0]+1, position[1]))
    # Up
    if position[0] > 0 and matrix[position[0]-1][position[1]] == next_height:
        next_positions.append((position[0]-1, position[1]))

    # Recursion to find next positions
    for next_position in next_positions:
        search_next(matrix, next_position, top_set)


total_part_1 = 0
total_part_2 = 0

matrix_map = [[int(char) for char in x] for x in text.splitlines()]

start_positions = []

for i, row in enumerate(matrix_map):
    for j, column in enumerate(row):
        if column == 0:
            start_positions.append((i, j))

# Solver with recursion
for position in start_positions:
    # Use set to avoid duplication when a trailhead goes to a 9 in differetn ways
    top_set = set()
    search_next(matrix_map, position, top_set)
    total_part_1 += len(top_set)

print(f"Result part 1: {total_part_1}")
print(f"Result part 2: {total_part_2}")
