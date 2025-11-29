#Data types: int ,float ,str ,bool
age = 17
height = 1.65
name = "mam"
is_cute = False

print("Mam is", age, "years old")
print("Mam is", height, "cm tall")
print("Mam is called", name)
print("Is Mam acceptable? Answer:", is_cute)

print("_______________________________")
print("                             ")

#Operators: +  -  *  /  %  //  **
#Comparison Operators: ==  !=  >  <  >=  <=
#Logical Operators: and  or  not

length = 5
width = 1.5
shape_name = "rectangle"
print(f"Length of the {shape_name} is {length}cm")
print(f"Width of the {shape_name} is {width}cm")

area = length * width
print(f"The area of the {shape_name} is {area}cm^2")

print(f"The remainder of 17/4 is {17%4}")

is_greater = (length > 10) and (width <20)
print("Is the length greater than 10 and width less than 20?", is_greater)
