import re

text = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


def print_table(matrix):
    for row in matrix:
        line = " "
        for column in row:
            line += column + ""
        print(line)


def get_points_part_1(antenna1: tuple, antenna2: tuple, _):
    # distance
    diff_i = abs(antenna1[0] - antenna2[0])
    diff_j = abs(antenna1[1] - antenna2[1])

    # new points
    new_point_1 = ()
    new_point_2 = ()

    # first axis
    if antenna1[0] < antenna2[0]:
        new_point_1 += (antenna1[0] - diff_i,)
        new_point_2 += (antenna2[0] + diff_i,)
    else:
        new_point_1 += (antenna1[0] + diff_i,)
        new_point_2 += (antenna2[0] - diff_i,)

    # second axis
    if antenna1[1] < antenna2[1]:
        new_point_1 += (antenna1[1] - diff_j,)
        new_point_2 += (antenna2[1] + diff_j,)
    else:
        new_point_1 += (antenna1[1] + diff_j,)
        new_point_2 += (antenna2[1] - diff_j,)

    return [new_point_1, new_point_2]


def get_points_part_2(antenna1: tuple, antenna2: tuple, matrix):
    # distance
    diff_i = abs(antenna1[0] - antenna2[0])
    diff_j = abs(antenna1[1] - antenna2[1])

    # new points
    new_points_1 = []
    new_points_2 = []

    # first axis i
    stop_flag = False
    while not stop_flag:
        # Take previous or first
        original_i_1 = antenna1[0] if len(
            new_points_1) == 0 else new_points_1[-1][0]
        original_i_2 = antenna2[0] if len(
            new_points_2) == 0 else new_points_2[-1][0]
        if antenna1[0] < antenna2[0]:
            new_points_1.append((original_i_1 - diff_i,))
            new_points_2.append((original_i_2 + diff_i,))

            # When we go out of the table in both
            if original_i_1 < 0 and original_i_2 > len(matrix):
                stop_flag = True

        else:
            new_points_1.append((original_i_1 + diff_i,))
            new_points_2.append((original_i_2 - diff_i,))

            # When we go out of the table in both
            if original_i_2 < 0 and original_i_1 > len(matrix):
                stop_flag = True

    # first axis j
    stop_flag = False
    for i in range(len(new_points_1)):
        # Take previous or first
        original_j_1 = antenna1[1] if i == 0 else new_points_1[i - 1][1]
        original_j_2 = antenna2[1] if i == 0 else new_points_2[i - 1][1]
        if antenna1[1] < antenna2[1]:
            new_points_1[i] += (original_j_1 - diff_j,)
            new_points_2[i] += (original_j_2 + diff_j,)
        else:
            new_points_1[i] += (original_j_1 + diff_j,)
            new_points_2[i] += (original_j_2 - diff_j,)

    return new_points_1 + new_points_2


def add_point(matrix, new_point):
    if new_point[0] >= 0 and new_point[0] < len(matrix) and new_point[1] >= 0 and new_point[1] < len(matrix[0]):
        matrix_map[new_point[0]][new_point[1]] = "#"


def solve(matrix_map, get_point_function):
    # Search all antenas
    antennas = search_antennas(matrix_map)

    # Go through each type of antenna
    for type, antenna_positions in antennas.items():
        # Go through each oposition
        for antenna_pos in antenna_positions:
            # COmapre each antenna with all antennas of same type
            for pair_antenna in antenna_positions:
                if pair_antenna != antenna_pos:
                    new_points = get_point_function(
                        antenna_pos, pair_antenna, matrix_map)

                    for point in new_points:
                        add_point(matrix_map, point)


def search_antennas(matrix_map):
    # Search all antenas
    antennas = {}

    for i, row in enumerate(matrix_map):
        for j, column in enumerate(row):
            if column != ".":
                if column not in antennas:
                    antennas[column] = [(i, j)]
                else:
                    antennas[column].append((i, j))
    return antennas

total_part_1 = 0
total_part_2 = 0


# Part 1
# Read original map
matrix_map = [list(x) for x in text.splitlines()]

solve(matrix_map, get_points_part_1)

# count X(not very optimal but... :D)
for row in matrix_map:
    total_part_1 += row.count("#")

# Part 2
# Read original map
matrix_map = [list(x) for x in text.splitlines()]

solve(matrix_map, get_points_part_2)

# count X(not very optimal but... :D)
for row in matrix_map:
    total_part_2 += len([char for char in row if char != '.'])


print(f"Result part 1: {total_part_1}")
print(f"Result part 2: {total_part_2}")
