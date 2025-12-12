nums = [1,2,3,4,5,6,7,8,9]
def my_min(lst):
    x = lst[0]
    for i in lst:
        if x>i:
            x = i
    return x
print(my_min(nums))