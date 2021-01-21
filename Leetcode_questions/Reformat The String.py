def reformat(s):
    numbers = [c for c in s if c.isdigit()]
    alpha = [c for c in s if c.isalpha()]

    dif = abs(len(numbers) - len(alpha))

    if len(numbers) > len(alpha):
        return helper(numbers, alpha, dif)
    else:
        return helper(alpha, numbers, dif)


def helper( longest, shortest, dif):
    ans = ''
    if dif > 1:
        return ans

    if dif == 1:
        ans += longest.pop()

    while longest or shortest:
        ans += shortest.pop() + longest.pop()

    return ans

a=reformat("a0b1c2")
print(a)