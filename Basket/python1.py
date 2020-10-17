class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beg(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_values(self,datal):

        for i in datal:
            self.insert_at_beg(i)


    def getlen(self):
        count=0
        itr=self.head

        while itr:
            count=count+1

            itr=itr.next

        print(count)


    def remove_at_pos(self,index):
        if index<0:
            print("invalid")
            return

        if index==0:
            self.head=self.head.next


        itr=self.head
        count=0
        while itr:
         if count==index-1:
             itr.next=itr.next.next

             break

        count=count+1
        itr=itr.next



    def printf(self):
        if self.head is None:
            print("empty")
            return


        itr=self.head

        lst=""
        while itr:
            lst+=str(itr.data)+"--->"

            itr=itr.next


        print(lst)


l1=LinkedList()
l1.insert_at_beg(3)
l1.insert_at_beg(2)


l1.printf()
l1.insert_values(['a','b'])
l1.printf()
l1.getlen()
l1.remove_at_pos(2)
l1.printf()




