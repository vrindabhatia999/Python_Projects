def isPerfectSquare(num):
    value = num ** 0.5
    if value.is_integer():
        return True
    else:
        return False

a=isPerfectSquare(12)
print(a)
