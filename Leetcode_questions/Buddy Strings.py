def buddyStrings( A, B) :
    if len(A) != len(B):
        return False

    if A == B and len(set(A)) < len(A):
        return True

    diff = []
    for x in range(len(B)):
        if A[x] != B[x]:
            diff.append([A[x], B[x]])

    if len(diff) == 2 and diff[0] == diff[-1][::-1]:
        return True
    return False


a=buddyStrings("aaaabc","aaaacb")
print(a)