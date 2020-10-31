#reversing string by modifying the input array in-place with O(1)
def Reverse(srr):
    left = 0
    right = len(srr) - 1
    while left < right:
        temp = srr[left]
        srr[left] = srr[right]
        srr[right] = temp

        left = left + 1
        right = right - 1


    return srr

a=Reverse(['h','e','l','l','o'])
print(a)
