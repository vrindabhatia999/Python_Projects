from collections import *
def sort(nums):
    s = Counter(nums)
    nums.sort(key=lambda x: (s[x], -x))
    return nums



a=sort([1,2,3,1,2,3,1])
print(a)