def peakIndexInMountainArray(arr)  :
    for index, value in enumerate(arr):
        if arr[index + 1] < arr[index]:
            return index



a=peakIndexInMountainArray([0,2,3,1,-1])
print(a)
