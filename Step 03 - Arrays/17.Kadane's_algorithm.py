# Brute Force - Method 1
def max_array_sum1(arr1):
    max_sum = float('-inf')
    for i in range(len(arr1)):
        for j in range(i,len(arr1)):
            sum1=0
            for k in range(i,j+1):
                sum1+=arr1[k]
            max_sum=max(max_sum,sum1)
    return max_sum
arr1=[-2,-3,4,-1,-2,1,5,-3]
print(max_array_sum1(arr1))
# Time Complexity - O(N^3)
# Space Complexity - O(1)

# Better
def max_array_sum2(arr2):
    max_sum = float('-inf')
    for i in range(len(arr2)):
        sum1=0
        for j in range(i,len(arr2)):
            sum1+=arr1[j]
            max_sum=max(max_sum,sum1)
    return max_sum
arr2=[-2,-3,4,-1,-2,1,5,-3]
print(max_array_sum2(arr2))
# Time Complexity - O(N^2)
# Space Complexity - O(1)

# Optimal - Kadane's Algorithm
def max_array_sum3_kadanes(arr3):
    max_sum,sum1 = arr3[0],arr3[0]
    for i in range(1,len(arr3)):
        sum1+=arr3[i]
        if sum1>max_sum:
            max_sum=sum1
        if sum1<0:
            sum1=0
    return max_sum
arr3=[-2,-3,4,-1,-2,1,5,-3]
print(max_array_sum3_kadanes(arr3))
# Time Complexity - O(N)
# Space Complexity - O(1)

# Provide subarray of maximum sum - Kadane's
def max_array_sum4_kadanes2(arr4):
    max_sum,sum1 = arr4[0],arr4[0]
    start_index,end_index=0,0
    for i in range(1,len(arr4)):
        if sum1 == 0:
            start=i # Recapturing index start once sum resets
        sum1+=arr4[i]
        if sum1>max_sum:
            max_sum=sum1
            start_index=start # Updating the start index as start
            end_index=i # Updating the end index every time when new max_sum is calculated
        if sum1<0:
            sum1=0
    return arr4[start_index:end_index+1], max_sum
arr4=[-2,-3,4,-1,-2,1,5,-3]
print(max_array_sum4_kadanes2(arr4))
# Time Complexity - O(N)
# Space Complexity - O(1)