# Brute Force
def remove_dup1(arr):
    set1=set()
    for i in range(0,len(arr)):
        set1.add(arr[i]) # O(N)
    index=0
    for idx, val in enumerate(set1): # O(N)
        arr[index]=val
        index+=1
    return index
arr=[1,1,2,2,2,3,3]
print(remove_dup1(arr))
# Time Complexity - O(2N)
# Space Complexity - O(N)

# Optimal
# 2 Pointer approach
def remove_dup2(arr):
    i=0 # 1st index point fixed
    for j in range(1,len(arr)): # Use another pointer that iterates throught the array to find new element
        if arr[i] != arr[j]: # Don't increment the 1st index pointer until new element is found
            i+=1 # Increment the index pointer until new element is found
            arr[i]=arr[j] # Update the current index pointer until new element is found
    return i+1 # return the size of the unique by unique index+1
arr=[1,1,2,2,2,3,3]
print(remove_dup2(arr))
# Time Complexity - O(N)
# Space Complexity - O(1)