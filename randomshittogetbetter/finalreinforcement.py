#DICTIONARY
nums = [1, 2, 3, 4, 0, 0, 0, -5, -4, -2, 1, 3]
count = {
    "positive": [],
    "negative": [],
    "zero": []
}
for i in nums:
    if i == 0:
        count["zero"].append(i)
    elif i > 0:
        count["positive"].append(i)
    else:
        count["negative"].append(i)
print(count) 

#UNIQUE BUT KEEP ORDER
nums = [3, 1, 3, 5, 1, 2, 3]
res = []
for i in nums:
    if i not in res:
        res.append(i)
print(res)

#FIRST INDEX OF MAX VALUE
nums = [4, 9, 1, 9, 3]
maxval = nums[0]
maxind = 0
for i in range(len(nums)):
    if maxval < nums[i]:
        maxval = nums[i]
        maxind = i
print(maxind)

#REMOVE ALL ODD NUMS:
nums = [3, 8, 5, 2, 7, 10, 1]
for i, v in enumerate(nums):
    if v % 2 != 0:
        nums.remove(v)
        i += 1
print(nums)

#IMPLEMENT YOUR OWN MIN()
nums = [1,2,3,4,5,6,7,8,9]
def my_min(lst):
    x = lst[0]
    for i in lst:
        if x>i:
            x = i
    return x

