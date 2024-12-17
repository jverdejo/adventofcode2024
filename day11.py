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


num_blinks=75
for _ in range(num_blinks):
    arrangement=blink(arrangement)

total_part_1=len(arrangement)

print(f"Result part 1: {total_part_1}")
print(f"Result part 2: {total_part_2}")
