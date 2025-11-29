#File I/O

#Writing to a file
with open("my_file.txt", "w") as file:
    file.write("I am writing to a file \n")
    file.write("This is the second line")

#Reading from a file
with open("my_file.txt", "r") as file:
    content = file.read()
    print(content)

#Appending
with open("my_file.txt", "a") as file:
    file.write("Im appending something")

#Printing the entire thing
with open("my_file.txt", "r") as file:
    content = file.read()
    print(content)

############___________EXERCISES____________###############
with open("my_notes.txt", "w") as file:
    file.write("Python is powerful.")
    file.write("File handling is essential.")
with open("my_notes.txt", "r") as file:
    for line in file:
        print(line)
