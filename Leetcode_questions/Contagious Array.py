def findMaxLength(nums):
    dict = {}
    subarray, count = 0, 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1

        else:
            count -= 1

        if count == 0:
            subarray = i + 1

        if count in dict:
            subarray = max(subarray, i - dict[count])

        else:
            dict[count] = i

    return subarray

a=findMaxLength([0,1,1,0,1,1,1])
print(a)