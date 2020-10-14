#leetcode plusone
def plusone(digits):
    digits=list(map(str,digits))
    digits=''.join(digits)
    digits=str(int(digits)+1) #converting into integer like 124 and adding one to it

    digits=list(digits)
    return list(map(int,digits))


a=plusone([1,2,3])
print(a)

