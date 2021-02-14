def mergesort(nums1,nums2,m,n):
    if n != 0:
        j = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[j]
            j = j + 1
        nums1 = nums1.sort()

        return nums1
a=mergesort([1,2,3,0,0,0],[4,5,6],3,3)
print(a)