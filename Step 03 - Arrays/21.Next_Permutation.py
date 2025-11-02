# Brute Force

# 1. Generate all possible combinations using Recursion
# 2. Linear Search
# 3. Get the next index of the stored combination

# But implementing with this Brute Force method is not advisable...
# Because of the extremely high time complexity

# Optimal

# 1. Find the longest prefix match - arr[i] < a[i+1]
# 2. Find someone greater that arr[i] from i+1 to n-1, but smallest one - close
# 3. Try to place the remaining in sorted order

def next_permutation(arr):
    N = len(arr)
    index=-1
    for i in range(N-2,-1,-1): # O(N)
        if arr[i]<arr[i+1]:
            index = i
            break
    if index==-1: # O(N)
        arr.reverse()
        return arr
    for j in range(N-1,index,-1): # O(N)
        if arr[j]>arr[index]:
            arr[j],arr[index]=arr[index],arr[j]
            break
    arr[index+1:N]=arr[index+1:N][::-1]
    return arr    
arr=[2,1,5,4,3,0,0]
print(next_permutation(arr))
# Time Complexity - O(N)
# Space Complexity - O(1)