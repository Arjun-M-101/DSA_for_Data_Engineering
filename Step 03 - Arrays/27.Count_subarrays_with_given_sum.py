# Brute Force
def count_array_sum1(arr1,K):
    N=(len(arr1))
    count=0
    for i in range(N):
        sum1=0
        for j in range(i,N):
            sum1+=arr1[j]
            if sum1==K:
                count+=1
    return count
arr1=[1,2,3,-3,1,1,1,4,2,-3]
K=3
print(count_array_sum1(arr1,K))
# Time Complexity - O(N^2)
# Space Complexity - O(1)

# Optimal - Prefix sum
def count_array_sum2(arr2,K):
    N=len(arr2)
    hash_dict={0:1}
    prefix_sum=0
    count=0
    for i in range(N):
        num = arr2[i]
        prefix_sum+=num
        possible_sum = prefix_sum-K
        # If we've seen this possible sum before, add its frequency
        if possible_sum in hash_dict:
            count += hash_dict[possible_sum]
        # Record the current prefix sum
        hash_dict[prefix_sum] = hash_dict.get(prefix_sum, 0) + 1
    return count
arr2=[1,2,3,-3,1,1,1,4,2,-3]        
K=3
print(count_array_sum2(arr2,K))
# Time Complexity - O(N)
# Space Complexity - O(N)