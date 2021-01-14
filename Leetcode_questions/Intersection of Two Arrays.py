def intersection( nums1, nums2 )  :
    return (list(set(nums1) & set(nums2)))

a=intersection([1,2,3],[2,3,2])
print(a)