#Input Specification: A list of integers $L$.
#Output Specification: Print a list containing all elements of $L$ but with duplicates removed, 
#maintaining the original insertion order (or close to it).

def no_dups(s):
    s = s.split()
    seen = set(s)
    results = []
    for x in s:
        if x not in seen:
            results.append(x)
            seen.add(x)
    return results

s = input()
print(no_dups(s))