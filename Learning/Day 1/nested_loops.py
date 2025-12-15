#Example 1: generate 3x3 grid multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        result = i*j
        print(f"{i}*{j} = {result} ", end ='\t')    # \t is a tab space
    print()                                         # new line

#Example 2: iterating over a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]

for row in matrix:                              # each "row" is a list inside the matrix
    for element in row:                         # each "element" is a number in the matrix 
        print(f"{element}", end = '\t')
    print()

#Example 3: nested while loops
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        result = i*j
        print(f"Outer: {i} \t Inner: {j}")
        j += 1
    i += 1
        



