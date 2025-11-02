# Provide subarray of maximum sum - Kadane's
# Optimal
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