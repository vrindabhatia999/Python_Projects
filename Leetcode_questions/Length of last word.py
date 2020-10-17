def lengthOfLastWord(s):
    if s == '':
        return 0
    s1 = s.split()

    if not s1:
        return 0

    return len(s1[-1])


a=lengthOfLastWord("hello world")
print(a)
