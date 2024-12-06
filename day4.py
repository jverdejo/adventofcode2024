text="""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

SEARCH="XMAS"
SEARCH_2="MAS"

def check_row(i, j, matrix):
    len_row=len(matrix[0])
    count=0
    #right
    if j <= len_row - len(SEARCH) and "".join(matrix[i][j:j+4]) == SEARCH:
        count+=1
    #left
    if j>=len(SEARCH)-1 and "".join(reversed(matrix[i][j-4:j])) == SEARCH:
        count+=1

    return count

def check_column(i,j,matrix):
    len_column=len(matrix)
    count=0

    #down
    if i<= len_column - len(SEARCH) and "".join([matrix[i+z][j] for z in range(len(SEARCH))]) == SEARCH:
        count+=1
    #up
    if i>=len(SEARCH)-1 and "".join([matrix[i-z][j] for z in range(len(SEARCH))]) == SEARCH:
        count+=1
    return count

def check_diagonal(i,j,matrix,search):
    len_column=len(matrix)
    len_row=len(matrix[0])
    #diagonal down
    #right
    count=0
    if i<= len_column - len(search) and j <= len_row - len(search) and "".join([matrix[i+z][j+z] for z in range(len(search))]) == search:
        count+=1
    #left
    if i<= len_column - len(search) and j>=len(search)-1 and "".join([matrix[i+z][j-z] for z in range(len(search))]) == search:
        count+=1

    #diagonal up
    #right
    if i>=len(search)-1 and j <= len_row - len(search) and "".join([matrix[i-z][j+z] for z in range(len(search))]) == search:
        count+=1
    #left
    if i>=len(search)-1 and j>=len(search)-1 and "".join([matrix[i-z][j-z] for z in range(len(search))]) == search:
        count+=1
    
    return count

def check_cross(i,j,matrix):
    len_column=len(matrix)
    len_row=len(matrix[0])
    # Check limits
    if i<1 or i==len_row-1 or j<1 or j==len_column-1:
        return 0 
    # cross_1 -> \
    cross_1= "".join([matrix[i-1+z][j-1+z] for z in range(len(SEARCH_2))])

    # cross_2 -> /
    cross_2= "".join([matrix[i+1-z][j-1+z] for z in range(len(SEARCH_2))])

    return (cross_1==SEARCH_2 or cross_1=="".join(reversed(SEARCH_2))) and (cross_2==SEARCH_2 or cross_2=="".join(reversed(SEARCH_2)))


# Create matrix
matrix=[list(x) for x in text.splitlines()]


total=0
#part 1
for i in range(len(matrix)):    
    for j in range(len(matrix[i])):
        total+=check_row(i,j,matrix)
        total+=check_column(i,j,matrix)
        total+=check_diagonal(i,j,matrix,SEARCH)

#part 2
total_part2=0
for i in range(len(matrix)):    
    for j in range(len(matrix[i])):
        # check if each element it´s a cross X
        if check_cross(i,j,matrix):
            total_part2+=1

print(f"Result part 1: {total}")
print(f"Result part 2: {total_part2}")
