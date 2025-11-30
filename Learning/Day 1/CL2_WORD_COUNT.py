#Input Specification: A string $S$ representing a sentence. Words are separated by one or more spaces.
#Output Specification: Print an integer representing the total number of words in the sentence.
def word_count(s):
    # The split() method, when called without arguments, splits the string 
    # by any whitespace and handles multiple spaces between words correctly.
    words = s.split()
    return len(words)

input_s = input()
print(word_count(input_s))