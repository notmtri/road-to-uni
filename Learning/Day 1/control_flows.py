#Conditional statements (if, elif, else)
grade = 85
print (f"Grade: {grade}")
if grade >= 90:
    print("A")
elif grade >= 80:  # Short for "else if"
    print("B")
else:
    print("C or lower")

#For loop
print(f"Natural Numbers that are lower than 5 are:")
for i in range(5):
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}") #Output: I like + fruit names

#While loop
count = 0 
while count <5 :
    print(f"Count is: {count}")
    count += 1  # Increment count by 1

#############_______EXERCISES_______################
#Exercise 1 (if/else)
fav_num_str = input(f"Write your favorite number:")
fav_num = int(fav_num_str)
if fav_num > 10 :
    print("That's a big number!")
else :
    print("That's a small number")

#Exercise 2 (for loop)
for i in range(1, 11): #range() function can be (stop), (start,stop), or (start, stop, step). Values are integers
    s = i%2
    if s == 0 : print(f"{i} is an even number")
    else : print(f"{i} is not an number")
    i += 1
#Another approach: for i in range (2, 11, 2) : print(i)

#Exercise 3 (while loop)
x = 5
while x>0 :
    x-=1
    print(x)


