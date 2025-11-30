#Input Specification: A string $S$ representing a sentence. Words are separated by single spaces.
#If there is a tie, print the first word encountered that has the maximum length.
#Output Specification: Print the longest word found in the sentence. 
def longest_word(s):
    words = s.split()
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest

s = input()
print(longest_word(s))