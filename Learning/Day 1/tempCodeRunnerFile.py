def is_ana(w1, w2):
    w1 = set(w1)
    w2 = set(w2)
    if w1 == w2:
        return True
    else: 
        return False

s1 = input()
s2 = input()
print(is_ana(s1,s2))