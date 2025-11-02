def Largest(arr):
    largest=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest = arr[i]
    return largest
arr=[4,0,6,1,3,7,2,5]
print(Largest(arr))
# O(N)