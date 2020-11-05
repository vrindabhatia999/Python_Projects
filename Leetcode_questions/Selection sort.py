def selection(arr):
    n=len(arr)

    for i in range(n):

        min_pos=i
        for j in range(i+1,n):
            if arr[min_pos]>arr[j]:
                min_pos=j


        temp=arr[i]
        arr[i]=arr[min_pos]
        arr[min_pos]=temp

arr=[6,7,9,3]
selection(arr)
print(arr)