def detectCapitalUse(word):
    if word == word.upper():
        return True

    if word == word.lower():
        return True

    if word == word[:1].upper() + word[1:].lower():
        return True
print(detectCapitalUse("Hello"))
