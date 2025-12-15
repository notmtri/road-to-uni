i = 1
while i <= 3:
    j = 1
    while j <= 3:
        result = i*j
        print(f"Outer: {i} \t Inner: {j}")
        j += 1
    i += 1