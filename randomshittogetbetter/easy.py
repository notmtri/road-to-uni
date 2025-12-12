#Ex1: second largest num
nums = [1, 2, 3, 4, 4, 5, 6, 7, 100, -10, 2, 2]
nums = sorted(set(nums))
print(nums[-2])

#Ex2: how many numbers > average
nums = [1, 2, 3, 4, 4, 5, 6, 7, 100, -10, 2, 2]
avg = 0
count = 0
for i in nums:
    avg += i
avg /= len(nums) 
for i in nums:
    if i > avg:
        count += 1
print(count)

#Ex3: index of first negative num
nums = [1, 2, 3, 4, 4, 5, 6, 7, 100, -10, 2, 2]
for i, v in enumerate(nums):
    if v < 0:
        print(i)
        break

#Ex4: remove even num
nums = [1, 2, 3, 4, 4, 5, 6, 7, 100, -10, 2, 2]
odd_nums = []
for i in nums:
    if i % 2 != 0:
        odd_nums.append(i)
print(odd_nums)

#Ex5: is increasing
nums = [1, 2, 3, 4, 4, 5, 6, 7, 100, -10, 2, 2]
def is_increase(l):
    for i in range(len(l) - 1):
        if l[i] >= l[i+1]:
            return False            #stops if error happens
    return True                     #confirms the loop finishes through the list
print(is_increase(nums))