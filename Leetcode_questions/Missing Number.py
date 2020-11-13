def missingNumber(nums):
    return (

            sum(range(len(nums) + 1)) - sum(nums)
    )
a=missingNumber([3,0,1])
print(a)