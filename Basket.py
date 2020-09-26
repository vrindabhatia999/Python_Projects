#basket add to   arr[i]=dict[key]
basket={}


print("Vegetable Basket")
print("**************")
print("1.Add to basket")
print("2.Remove from basket")
print("3.view basket")
print("4.exit")


while True:
 choice = int(input("enter your choice:"))
 if choice==1:
    item=input("enter item name")

    if item in basket:
        print("enter new quantity:")
        quant=int(input("enter quantity"))
        basket[item]+=quant
    else:
     quant=int(input("enter its quantity"))
     basket[item]=quant

 elif choice==2:
   item=input("enter the item you want to delete:")
   del(basket[item])


 elif choice==3:
    for item in basket:
        print(item,":",basket[item])

 elif choice==4:
     break

 else:
     print("choose valid option")


