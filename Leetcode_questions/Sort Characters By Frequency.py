def frequencySort(s):
    res = ""
    dict = {}

    for i in s:
        if i in dict:
            dict[i] += 1

        else:
            dict[i] = 1

    s = sorted(dict, key=lambda x: dict[x], reverse=True)

    for ch in s:
        res += ch * dict[ch]

    return res
a=frequencySort("treee")
print(a)