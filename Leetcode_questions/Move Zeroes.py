def move(nums):


        i = 0
        for j in range(len(nums)):
            if (nums[j] != 0):
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        return(nums)

a=move([1,0,3,0,12])
print(a)
