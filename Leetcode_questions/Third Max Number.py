def thirdMax(nums):
    SetNums = set(nums)
    if len(SetNums) < 3:
        return max(SetNums)

    sortN = list(sorted(SetNums))
    return sortN[-3]

a=thirdMax([2,-3,21,45,6])
print(a)
