#1. longest word in a string
str = ["apple", "banana", "kiwi"]
longest = ""
for i in range(len(str)):
    if len(str[i]) > len(longest):
        longest = str[i]
print(longest)

#2. count times max appear
nums = [1, 7, 7, 3]
count = 0
for i in nums:
    if i == max(nums):
        count += 1
print(count)

#3. reverse a list
nums = [1, 2, 3, 4, 4, 5, 6, 7, 100, -10, 2, 2]
rev = []
i = len(nums) - 1
while i >= 0:
    rev.append(nums[i])
    i -= 1
print(rev)

#4. is palindrome
nums = [1, 2, 3, 4, 4, 3, 2, 1]
rev = []
i = len(nums) - 1
while i >= 0:
    rev.append(nums[i])
    i -= 1
if nums == rev:
    print(True)
else:
    print(False)

#5. second smallest without set()
nums = [4, 1, 1, 2, 5]
nums_set = []
for i in nums:
    if i not in nums_set:
        nums_set.append(i)
print(sorted(nums_set)[1])
#Alternative solution without sort() or set(): see practask 2