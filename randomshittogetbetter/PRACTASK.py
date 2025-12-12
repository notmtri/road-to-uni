#BUBBLE SORTING
nums = [4, 1, 9, 9, 3]
for i in range(len(nums)):          #this guarantees all maxes are pushed to the end
    for i in range(len(nums) - 1):  #this is just bringing max to the end, not sorting
        if nums[i] > nums[i+1]:
            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp        #or nums[i], nums[i+1] = nums[i+1], nums[i]
print(nums)

#PRACTASK 1: Second-largest and largest without sorting
nums = [12, 5, 19, 7, 19, 3]
fir = None
sec = None
for x in nums:
    if fir is None or fir < x:
        sec = fir
        fir = x
    elif (sec is None or x > sec) and x != fir:
        sec = x
print(f"{fir}, {sec}")

#PRACTASK 2: Second-smallest and smallest without sorting
nums = [8, 2, 6, 1, 1, 7, -3, 4]
lest = None
seclest = None
for i in nums:
    if lest is None or lest > i:
        seclest = lest
        lest = i
    elif (seclest is None or seclest > i) and i != lest:
        seclest = i
print(f"{lest}, {seclest}")

#PRACTASK 3: Greater than 10
nums = [4, 12, 7, 15, 3, 22, 10, 11]
counter = 0
for i in nums:
    if i > 10:
        counter +=1
print(counter)

#PRACTASK 4: Sum of even numbers:
nums = [5, 8, 12, 9, 21, 16, 4]
sum = 0
for i in nums:
    if i%2==0:
        sum +=i
print(sum)

#PRACTASK 5: New list of numbers doubled:
nums = [3, 6, 1, 8]
double = []
for i in nums:
    double.append(i*2)
print(double)

#PRACTASK 6: Count specific duplicates:
nums = [9, 4, 9, 1, 9, 7, 2]
count = 0
for i in nums:
    if i == 9:
        count += 1
print(count)

#PRACTASK 7: Index of first negative number:
nums = [5, 3, -1, 7, -4, 2]
index = None
for i in range(len(nums)): #enumerate() gives both index and value
    if nums[i] < 0:
        index = i
        break
print(index)