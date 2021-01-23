def perfect(num):
    l=list()
    for i in range(1,num):
        if num%i==0:
            l.append(i)


    if sum(l)==num:
        return True

a=perfect(28)
print(a)
