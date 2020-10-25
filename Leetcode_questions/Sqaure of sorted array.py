def square(arr):

    list=[]

    for i in arr:
        list.append(i**2)

    return sorted(list)

print(square([-4,-1,0,3,10]))
