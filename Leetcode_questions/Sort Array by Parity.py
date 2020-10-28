def SortByParity(arr):

    even=[]
    odd=[]

    for i in arr:
        if i%2==0:
            even.append(i)

        else:
            odd.append(i)


    return even+odd

a=SortByParity([2,1,4,5])
print(a)