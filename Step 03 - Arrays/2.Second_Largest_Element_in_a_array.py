# Better approach
def SLargest(arr):
    largest=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest = arr[i]
    slargest = float('-inf')
    for j in range(1,len(arr)):
        if arr[j]>slargest and arr[j]!=largest:
            slargest = arr[j]
    return slargest
arr=[4,0,6,1,3,7,7,6,2,5]
print(f"Second largest using better approach: {SLargest(arr)}")
# O(2N)

# Optimal approach
def SLargest2(arr):
    largest=arr[0]
    slargest=float('-inf')
    for i in range(1,len(arr)):
        if arr[i]>largest: # If the current element is greater than current largest
            slargest = largest # Then make the old largest as second largest
            largest = arr[i] # And update the new largest with the current element
        elif arr[i]<largest and arr[i]>slargest: # But if the current element is smaller than current largest but greater than current second largest
            slargest = arr[i] # Then update the current element as second largest
    return slargest
arr=[4,0,6,1,3,7,7,6,2,5]
print(f"Second largest using optimized approach: {SLargest2(arr)}")
# O(N)

# Optimal approach
def SSmallest(arr):
    smallest=arr[0]
    ssmallest=float('inf')
    for i in range(1,len(arr)):
        if arr[i]<smallest: # If the current element is smaller than current smallest
            ssmallest = smallest # Then make the old smallest as second smallest
            smallest = arr[i] # And update the new smallest with the current element
        elif arr[i]>smallest and arr[i]<ssmallest: # But if the current element is greater than current smallest but lesser than current second smallest
            ssmallest = arr[i] # Then update the current element as second smallest
    return ssmallest
arr=[4,0,6,1,3,7,7,6,2,5]
print(f"Second smallest using optimized approach: {SSmallest(arr)}")
# O(N)