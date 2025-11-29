#Error Handling (try. . .except)
try:
    # Code that might cause an error
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)

except ValueError:
    # Handled if the user enters non-numeric text
    print("Error: Invalid input. Please enter a whole number.")

except ZeroDivisionError:
    # Handled if the user enters 0
    print("Error: Cannot divide by zero.")

except Exception as e:
    # Catches any other unexpected error
    print(f"An unexpected error occurred: {e}")

finally:
    # Optional: This code always executes, regardless of whether an error occurred or not
    print("Execution attempt finished.")

#############__________EXERCISES___________##############
try:
    my_list = [1,2,3]
    print(my_list[5])
except IndexError as e:
    print("You tried to access an index that doesn't exist!")
    print(f"Error info: {e}")