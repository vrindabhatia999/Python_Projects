def searchB(arr,target):
    s=0
    l=len(arr)-1

    while s<=l:
        mid=s+1//2

        if arr[mid]==target:
            return mid

        if arr[mid]<target:
            s=mid+1

        else:
            l=mid-1

    return -1


a=searchB([1,2,3,6,8,9],6)
print(a)
