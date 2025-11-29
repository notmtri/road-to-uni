#Data structures: Lists, Tuples, Dictionaries, Sets
#1. Lists [] => ordered, changeable, allow duplicates
my_list = [2, 2.3, "This is a string", True]
print(my_list[2]) #Prints the 2nd value: 2.3 (count from 0)
my_list.append(30) #Add 30 to the end (appendix)
my_list[4] = False #Change 30 to False
print(my_list) #Print all

#2. Tuples () => ordered, unchangeable, allow duplicates
my_tuple = (1, 2, 3, "four")
# my_tuple[0] = 5 # This would cause an error (immutable)
print(my_tuple[3]) # Output: four

#3. Dictionaries {} => ordered (Python 3.7+), changeable, no duplicates
person = {
    "name": "Tri",
    "age": 17,
    "grade": 12
}
print(person["name"])
person["age"] = 18          #change 17 -> 18
person["job"] = "student"     #add new value pair
print(person["job"])
print(person["age"])

#4. Sets {} => unordered, unindexed, changeable, no duplicates
my_set = {"a", "b", "c", "d", "a"}
print(my_set) #Output: {'a', 'c', 'b'} (Order may vary, 'a' is not duplicated)
my_set.add("e")
print(f"After adding 'e': {my_set}")

#############__________EXERCISES_____________################
#Exercise 1:
num_list = [2, 4, 6, 8, 10]
for i in range(5):
    a = num_list[i]**2
    print(a)
    i+=1

#Exercise 2:
coordinates = (10, 20)
coordinates[0] = 5      #error: tuple objects are fixed

#Exercise 3:
inventory = {
    "apples": 10,
    "bananas": 5,
    "oranges": 15
}
inventory["apples"]=12
print(inventory["apples"])

#Exercise 4:
colors = {"red", "blue", "green", "red"}
print(colors)

