# vrinda bhatia code
# [Done]First Part to input the para
# [Done]putting the words in dict and displaying the dict like in the input format
# [Done]last is we have to change the casing small->capital and capital->small
def paragraph(para):
    output = {}
    for word in para.split():
        a = word.upper()
        if a in output.keys():
            output[a] = output.get(a) + 1
        else:
            output[a] = 1

    sort = sorted(output, key=output.get, reverse=True)[:5]
    print("TOP FIVE Elements acc to frequency")
    for element in sort:
        print(element)
        print(output[element])

    print(output)


def printLine(para):
    finalWords = []
    for i in para.split():
        temp = []
        for char in list(i):
            if (char.isupper()):
                temp.append(a.join(char.lower()))
            else:
                temp.append(a.join(char.upper()))
        finalWords.append(temp)
    sentence(finalWords)


def sentence(finalWords):
    ans = " "
    for i in finalWords:
        word = " "
        for j in i:
            word = word + j

        ans = ans + word + " "

    print(ans)


a = "Test is to TEST the Cloud Students. Cloud StudentS have the tesT "
paragraph(a)
printLine(a)
