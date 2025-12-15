#Basically, it's a shortened form of for loops to make a list

#Fundamental list comprehension:
result = [x * 2 for x in [1, 2, 3]]  # add x*2 to result[] for x in [1,2,3]
print(result)      

#Filtering (~removing):
result = [x for x in [1, 2, 3, 4, 5] if x % 2 == 0] # remove all that doesn't satisfy condition
print(result)
               
#if-else inside a comprehension
result = [x**2 if x%2 == 0 else x**3 for x in [1, 2, 3, 4, 5]] # square if even, cube if odd
print(result)

#nested loops inside a comprehension
result = [item for row in [[1,2,3], [4,5,6]] for item in row] # syntax: output - outer "loop" - inner "loop"
print(result) # output: [1, 2, 3, 4, 5, 6]

#Conclusion: MENTAL MODEL

# read the code as:
# [ OUTPUT for ITEM in ITERABLE if CONDITION ]

# for nested loops:
# [OUTPUT for SUB in DATA for X in SUB]

