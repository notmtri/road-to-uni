def seclar(l):
    l = list(set(l))
    l.sort()
    return l[-2]

l_input = list(map(int, input().split()))
print(seclar(l_input))