def ArrayRot(arr,d,n):   #d means how many elements to rotate

    for i in range(d):
        leftrot(arr,n)


def leftrot(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]

    arr[n-1]=temp


def printf(arr):
    print(arr)



arr=[2,3,4,5,8,9]
d=2
n=len(arr)
ArrayRot(arr,d,n)
printf(arr)