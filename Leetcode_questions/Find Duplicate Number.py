def dup(arr):
    for i in arr:
        if arr.count(i)>1:
            return [i]


a=dup([1,3,2,4,2,5,4])
print(a)
