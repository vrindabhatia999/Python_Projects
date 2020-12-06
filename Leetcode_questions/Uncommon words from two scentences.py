def uncom(s1,s2):
    a=s1.split()
    b=s2.split()
    c=[]
    d=[]

    for i in a:
        if i not in b:
            c.append(i)


    for j in b:
        if j not in a:
            d.append(j)




    print(c+d)


uncom("this apple is sweet","this apple is sour")

#More faster and efficient ethod also available, 


