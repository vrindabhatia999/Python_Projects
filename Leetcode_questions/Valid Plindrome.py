def isPalindrome(s):
    res = ""
    for i in s:
        if i.isalnum():
            res = res + i.lower()

    n = len(res)
    l = 0
    r = n - 1

    while l < r:
        if res[l] != res[r]:
            return False

        l = l + 1
        r = r - 1  # r moves backward
    return True

print(isPalindrome('A man, a plan, a canal: Panama'))
