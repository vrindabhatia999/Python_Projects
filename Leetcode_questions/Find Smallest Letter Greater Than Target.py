def nextGreatestLetter( letters, target)  :
    s = ord(target)

    for i in letters:
        if ord(i) > s:
            return i

    return letters[0]

a=nextGreatestLetter('["c", "f", "j"]','a')
print(a)