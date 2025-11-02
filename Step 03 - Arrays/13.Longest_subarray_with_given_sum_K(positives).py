# Brute Force - Type 1
def longest_subarray_sum1(arr1,K):
    length=0
    for i in range(len(arr1)):
        for j in range(i,len(arr1)): # Forming the subarray
            sum1=0
            for k in range(i,j+1): # Adding separately
                sum1+=arr1[k]
            if sum1==K:
                length=max(length,j-i+1)
    return length
arr1=[1,2,3,1,1,1,1,4,2,3]
K=3
print(longest_subarray_sum1(arr1,K))
# Time Complexity - O(N^3)
# Space Complexity - O(1)

# Brute Force - Type 2
def longest_subarray_sum2(arr2,K):
    length=0
    for i in range(len(arr2)):
        sum1=0
        for j in range(i,len(arr2)):
            sum1+=arr2[j] # Adding elements directly while forming the subarray
            if sum1==K:
                length=max(length,j-i+1)
    return length
arr2=[1,2,3,1,1,1,1,4,2,3]
K=3
print(longest_subarray_sum2(arr2,K))
# Time Complexity - O(N^2)
# Space Complexity - O(1)

# Better - Prefix-sum with Hash_table
# Applicable to positives, negatives & zeroes too
def longest_subarray_prefixsum(arr3,K):
    prefix_hash={}
    prefix_sum=0
    max_length=0
    for i, num in enumerate(arr3):
        prefix_sum+=num
        if prefix_sum == K:
            max_length=max(max_length,i+1)
        if prefix_sum-K in prefix_hash:
            max_length=max(max_length,i-prefix_hash[prefix_sum - K])
        if prefix_sum not in prefix_hash:
            prefix_hash[prefix_sum]=i
    return max_length
arr3=[1,2,3,1,1,1,1,4,2,3]
K=3
print(longest_subarray_prefixsum(arr3,K))
# Time Complexity - O(N) -> O(N^2) during collisions - worst case
# Space Complexity - O(N)

'''
The prefix sum that are stored in the hash-table (python) are game-changer. Because it acts like memory to store the progress our sum...

Here K = 3, 
In the given array, there can be any possibilities...
The subarray could be like:

3
0,0,3
0,1,2
0,0,1,1,1

The concept is... the more granular the elements are, the more length we will get in the subarray... How?
Because, if the elements are granular the distribution of prefix sum will be large... In the above example - 0,0,1,1,1 - length = 5 & sum = 3

We are just using the prefix sum stored in the hash-table to calculate that maximum length of the available prefix sum (in the hash table)

And the reason for letting this happen:

prefix_sum == K is....

Because we are letting it to form the base sum (prefix sum) equal to K.... So that after n no. of iterations (later)... we can recapture the index of the biggest prefix sum difference of the sub array...

Through which we can calculate the max length.
'''

# Optimal - 2 pointer
# Applicable to positives, zeroes only
def longest_subarray_2pointer(arr4,K):
    sum1,maxlength,left,right=0,0,0,0
    n=len(arr4)
    for right in range(n): # O(N)
        sum1+=arr4[right]
        while left<=right and sum1>K: # O(N) - Overall
            sum1-=arr4[left]
            left+=1
        if sum1==K:
            maxlength=max(maxlength,right-left+1)
    return maxlength
arr4=[1,2,3,1,1,1,1,3,3]
K=6
print(longest_subarray_2pointer(arr4,K))
# Time Complexity - O(2N)
# Space Complexity - O(1)