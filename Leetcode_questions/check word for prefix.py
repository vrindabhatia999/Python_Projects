def isPrefixOfWord(sentence, searchWord):
    s1 = sentence.split()
    for i, word in enumerate(s1):
        if word.startswith(searchWord):
            return i + 1

    return -1
a=isPrefixOfWord("i love eating burger","burg")
print(a)