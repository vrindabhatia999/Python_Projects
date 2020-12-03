def removeElement(nums,val):
    if len(nums) == 0:
        return 0

    while val in nums:
        nums.remove(val)

    return len(nums)
a=removeElement([3,2,2,3],2)
print(a)
