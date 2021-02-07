def restoreString(str, indices):
    t = list(str)
    zipped = zip(indices, t)
    z = [x for _, x in sorted(zipped)]
    return "".join(z)


a=restoreString("codeleet",[4,5,6,7,0,2,1,3])
print(a)