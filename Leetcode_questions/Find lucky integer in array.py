from collections import Counter
def findLucky(arr):
    counter =Counter(arr)
    lag = []
    for i in counter:
        if i == counter[i]:
            lag.append(i)

    if lag:
        return max(lag)

    return -1

a=findLucky([2,2,3,3,3,1,5])
print(a)
