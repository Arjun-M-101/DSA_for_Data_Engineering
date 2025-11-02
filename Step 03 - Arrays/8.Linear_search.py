def linear_search(arr,num):
    for i in range(len(arr)):
        if arr[i]==num:
            return i
    return -1
arr=[6,7,8,4,1]
print(linear_search(arr,4))
# Time Complexity - O(N)
# Space Complexity - O(1)