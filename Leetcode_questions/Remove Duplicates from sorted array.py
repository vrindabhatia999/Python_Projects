
def removeDuplicates(nums):
        i = 0
        while i < len(nums):
            if nums[i] in nums[i + 1:]:
                nums.remove(nums[i])

            else:
                i = i + 1

        return nums

print(removeDuplicates([1,1,2]))