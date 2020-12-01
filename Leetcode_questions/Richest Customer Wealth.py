def maximumWealth(accounts):
    a = map(sum, accounts)
    return max(a)
p=maximumWealth([[1,2,3],[3,2,1]])
print(p)