def pivotIndex(nums):
    pivot = -1
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i + 1:]):
            pivot = i
            break

    return pivot

a=pivotIndex([1,7,3,6,5,6])
print(a)
