#Input Specification: A string $S$ representing a sentence. Words are separated by single spaces.
#If there is a tie, print the first word encountered that has the maximum length.
#Output Specification: Print the longest word found in the sentence. 
def longest_word(s):
    words = s.split()
    for i in words:
        if len(words[i])<len(words[i+1]):
            a = len(words[i+1])
            i+=1
        else : 
            a = len(words[i])
            print(a)

s_input = input()
print(longest_word(s_input))