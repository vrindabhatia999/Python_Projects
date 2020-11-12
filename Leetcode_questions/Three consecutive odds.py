def threeConsecutiveOdds(arr):
    for i in range(len(arr) - 2):
        if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
            return True
            break

    return False

a=threeConsecutiveOdds([2,6,4,1])
print(a)