#Input Specification: A string $S$. Assume the string contains only lowercase letters and spaces.
#Output SpecificationPrint True if the string is a palindrome (reads the same forwards and backward, ignoring spaces). 
#Print False otherwise.

def is_palindrome(s):
    # 1. Remove all spaces
    is_cleaned = s.replace(" ", '')
    # 2. Check if the cleaned string is equal to its reverse
    return is_cleaned == is_cleaned[::-1]
s = input()
print(is_palindrome(s))
