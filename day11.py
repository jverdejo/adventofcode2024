from collections import defaultdict

text = """572556 22 0 528 4679021 1 10725 2790"""


def blink(arrangement_list):
    # To control index whena dding elements to list
    extra_index = 0

    # Make a copy of arramgement to avoid problem modifying list while iterating
    for i, element in enumerate(arrangement_list[:]):
        if element == "0":
            arrangement_list[extra_index+i] = "1"
        elif len(element) % 2 == 0:
            # COnvertoi to int to remove leadind zeros
            left_stone = int(element[:int(len(element)/2)])
            right_stone = int(element[int(len(element)/2):])

            # Set left_stonre in original position
            arrangement_list[extra_index+i] = str(left_stone)

            # Set right in the next, incrementing our index
            extra_index += 1
            arrangement_list.insert(extra_index+i, str(right_stone))
        else:
            new_stone = int(element)*2024
            arrangement_list[extra_index+i] = str(new_stone)

    return arrangement


total_part_1 = 0
total_part_2 = 0

arrangement = text.split(" ")

# Part 1
num_blinks = 25
for _ in range(num_blinks):
    arrangement = blink(arrangement)

total_part_1 = len(arrangement)

# Part 2
stones = defaultdict(int)
arrangement = text.split(" ")

# Initial state
for stone in arrangement:
    stones[stone] += 1

num_blinks = 75

# The idea of optimized code is to have a list without duplicationsm maintaning the quantioty of duplicated items
for i in range(num_blinks):
    
    # Use a temporal dict to avoid list modification during iteration
    tmp_stones = defaultdict(int)
    
    for stone, qty in stones.items():
        if stone == "0":            
            # All zeros are converted to 1
            tmp_stones["1"] += qty
        elif len(str(stone)) % 2 == 0:
            left_stone = int(stone[:int(len(stone)/2)])
            right_stone = int(stone[int(len(stone)/2):])

            # Maintain the quantity when split
            tmp_stones[str(left_stone)] += qty
            tmp_stones[str(right_stone)] += qty
        else:            
            new_stone = int(stone)*2024
            tmp_stones[str(new_stone)] += qty

    # Copy temporal stones into real
    stones = tmp_stones

# sum all quantity of each item
total_part_2 = sum([x for _, x in stones.items()])

print(f"Result part 1: {total_part_1}")
print(f"Result part 2: {total_part_2}")
