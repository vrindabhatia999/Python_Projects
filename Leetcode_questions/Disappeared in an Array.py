from collections import Counter
def finddisappear(arr):
    d=Counter(arr)
    a=[]
    for i in range(1,len(arr)+1):  #goes through index of arr from 1 to n inlusice both
        if i not in d:  #i loops through key value of dictionary-d
            a.append(i)

    return a

s1=finddisappear([4,3,2,7,8,2,3,1])
print(s1)



