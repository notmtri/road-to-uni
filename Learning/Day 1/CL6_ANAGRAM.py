def is_ana(w1, w2):
    if sorted(w1) == sorted(w2) and len(w1) == len(w2): #set() does not work for aba, bba (which are [a,b] and 3 char long)
        return True
    else: 
        return False

s1 = input()
s2 = input()
print(is_ana(s1,s2))