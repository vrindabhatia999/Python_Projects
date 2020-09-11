dict={}
while True:
    print("_______Birthday manager_______")
    print("1.Show bday's")
    print("2.add a bday")
    print("3.Exit")
    choice=int(input("Enter the choice:"))
    if choice==1:
        if len(dict.keys())==0:
            print("No bday to show, please enter some data..kindly move to second option")

        else:
            name=input("Enter the name of your friend:")
            bday=dict.get(name,"no data found")
            print("The bday comes on:")
            print(bday)

    elif choice==2:
        name=input("Enter the name of your friend:")
        date=input("Enter his/her birth date:")
        dict[name]=date
        print("...adding")
        print("Added Successfully")

    elif choice==3:
        break

    else:
        print("Choose a valid option")



