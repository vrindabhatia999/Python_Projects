def findTheDifference(s,t) :
    a = list(set(s))
    b = list(set(t))
    for i in b:
        if s.count(i) != t.count(i):
            return i


a=findTheDifference("abcd","abcde")
print(a)