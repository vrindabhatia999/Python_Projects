def goodpair(nums):
    l = len(nums)

    for i in range(l):

        for j in range(i+1,l):
            if nums[i]==nums[j] and i<j:
                print("good pair")

goodpair([1,2,4,1])