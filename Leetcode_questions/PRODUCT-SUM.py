def ps(n):

    pro=1
    sum=0
    for i in str(n):
        pro=pro*int(i)

    for i in str(n):
        sum=sum+int(i)

    return(pro-sum)
















a=ps(1234)

print(a)
