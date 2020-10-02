
import csv
from collections import Counter

print("****File_To_Dict****")
print("1.Read the file as dict")
print("2.Write to it")
print("3. view by name")
print("4.Exit")
while True:
 choice=int(input("enter choice:"))

 if choice==1:

     file = open("Test.txt", 'r')
     dict = {}

     for line in file:
         x = line.split(",")
         a = x[0]
         b = x[1]
         # c=len(b)-1
         # b=b[0:c]

         dict[a] = b

     print(dict)

 elif choice==2:
     file=open("Test.txt","a")

     write1=input("enter what to append:")
     file.writelines("\n")

     file.writelines(write1)
     print("content added")

     file.close()



 elif choice==3:


     nme=input("hose occupation you want to view?")
     occu=dict.get(nme,"b")
     print(occu)

 elif choice==4:
     break

 else:
     print("wrong choice")



 




