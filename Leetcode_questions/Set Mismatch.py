def setmis(nums):
    so=sorted(nums)

    n=len(nums)
    for i in range(n-1):
        if so[i+1]==so[i]:
            dup=so[i]
            break


    mis=set([i for i in range(1,n+1)]).difference(set(so))   #i runs over inexes->1,2,3,4

    x=next(iter(mis))


    return[dup,x]


s=setmis([1,2,2,4])
print(s)
