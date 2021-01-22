def thousandSeparator(n):
    res = str()
    ans = list(str(n))
    ans.reverse()

    i = 3

    while i < len(ans):
        ans.insert(i, ".")

        i += 4
    ans.reverse()

    for k in ans:
        res += k

    return res

a=thousandSeparator((1234566))
print(a)
