import copy

text="""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

total_part_1=0
total_part_2=0

# dict with position: x,y as key and number of times passed in one position
# if more than 4(one for each position) we are in a infinmte loop
infinite_loop_control={}

class InfiniteLoop(Exception): 
    def __init__(self, message): 
        self.message = message 
        super().__init__(self.message)

def move(matrix, guard_i, guard_j,new_position_i,new_position_j,move_simbol,can_move_simbol):
    # Check if can move
    if matrix[new_position_i][new_position_j]=="#":
        matrix[guard_i][guard_j]=can_move_simbol
        return  matrix,guard_i,guard_j   
     
    # Move
    matrix[new_position_i][new_position_j]=move_simbol

    # Check infinte loop
    key =f"{new_position_i},{new_position_j}"
    if key not in infinite_loop_control:
        infinite_loop_control[key]=1
    else:
        infinite_loop_control[key]=infinite_loop_control[key]+1
    
    if infinite_loop_control[key]>4:
        raise InfiniteLoop("Infinite loop found")
    return  matrix,new_position_i,new_position_j

def go_forward(matrix,guard_i, guard_j):
    """    
    returns finish, matrix, new_postion_i, new_position_j
    """

    # Get rotation
    rotation=matrix[guard_i][guard_j]

    # Set cuurent position as visited
    matrix[guard_i][guard_j]="X"

    # Move
    if rotation=="^":
        # Check end
        if guard_i==0:
            return True, matrix,guard_i, guard_j
        
        # New position
        new_position_i=guard_i-1
        new_position_j=guard_j

        #Move player if posible
        matrix,new_position_i,new_position_j=move(matrix,guard_i,guard_j,new_position_i,new_position_j,"^",">")   
        return False,matrix,new_position_i,new_position_j

    if rotation==">":
        # Check end
        if guard_j==len(matrix[0])-1:
            return True, matrix,guard_i, guard_j
        
        # New position
        new_position_i=guard_i
        new_position_j=guard_j+1

        #Move player if posible
        matrix,new_position_i,new_position_j=move(matrix,guard_i,guard_j,new_position_i,new_position_j,">","v")   
        return False,matrix,new_position_i,new_position_j
    
    if rotation=="v":
        # Check end
        if guard_i==len(matrix)-1:
            return True, matrix,guard_i, guard_j
        
        # New position
        new_position_i=guard_i+1
        new_position_j=guard_j

        #Move player if posible
        matrix,new_position_i,new_position_j=move(matrix,guard_i,guard_j,new_position_i,new_position_j,"v","<")   
        return False,matrix,new_position_i,new_position_j
    if rotation == "<":
        # Check end
        if guard_j==0:
            return True, matrix,guard_i, guard_j
        
        # New position
        new_position_i=guard_i
        new_position_j=guard_j-1

        #Move player if posible
        matrix,new_position_i,new_position_j=move(matrix,guard_i,guard_j,new_position_i,new_position_j,"<","^")   
        return False,matrix,new_position_i,new_position_j

def print_table(matrix):
    for row in matrix:
        line=""
        for column in row:
            line+=column+" "
        print(line)

def solve_map(matrix_map):
    guard_i=-1
    guard_j=-1
    
    # Search player
    for i,row in enumerate(matrix_map):        
        if "^" in row: # aume alwais start lookign up :)
            guard_i=i
            guard_j=row.index("^")


    found=False

    # loop to found exists
    while not found:
        found,matrix_map,guard_i,guard_j=go_forward(matrix_map,guard_i,guard_j)

    return matrix_map         


# Read map into matrix [][]
matrix_map=[list(x) for x in text.splitlines()]
matrix_map=solve_map(matrix_map)

# count X(not very optimal but... :D)
for row in matrix_map:
    total_part_1+= row.count("X")

# Part 2
#reload map
matrix_map_original=[list(x) for x in text.splitlines()]


# Go trought each position adding a obstacle and chech infinite loop
# Brute force?? (not very optimal but... :D)
for i in range(len(matrix_map_original)):
    for j in range(len(matrix_map_original[i])):
        infinite_loop_control={}
        matrix_map_aux=[list(x) for x in text.splitlines()]
        if matrix_map_aux[i][j]=="^":
            continue
        matrix_map_aux[i][j]="#"
        try:
            matrix_map_aux=solve_map(matrix_map_aux)
        except InfiniteLoop:
            total_part_2+=1    


print(f"Result part 1: {total_part_1}")
print(f"Result part 2: {total_part_2}")
