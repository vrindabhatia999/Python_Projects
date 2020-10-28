def ValidMountain(arr):
    if len(arr)<3:
        return False

    top_index=arr.index(max(arr)) #gives the first appearence of the maximum occuring element
    if top_index+1==len(arr) or top_index==0:
        return False

    i=0
    while i<top_index:
        if arr[i]<arr[i+1]:
            i+=1

        else:
            return False


    i=top_index
    while i<len(arr)-1:
        if arr[i]>arr[i+1]:
            i=i+1

        else:
            return False


    return True

a=ValidMountain([0,3,2,1])
print(a)