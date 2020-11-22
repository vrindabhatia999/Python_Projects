def findNumbers(nums):
    counte = 0
    for i in nums:
        if len(str(i)) % 2 == 0:
            counte += 1

    return counte


a=findNumbers([555,32,4654,21111,904])
print(a)