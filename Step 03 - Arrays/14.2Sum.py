# Variety 1 - Return indices
# Varitey 2 - Return Yes or No

# Brute Force - Suitable for both Variety 1 & 2
def TwoSum1(arr1,Sum1):
    for i in range(len(arr1)):
        for j in range(i+1,len(arr1)):
            if arr1[i]+arr1[j]==Sum1:
                return i,j # return 'Yes'
    return 'No'
arr1=[2,6,5,8,11]
Sum1=14
print(TwoSum1(arr1,Sum1))
# Time Complexity - O(N^2)
# Space Complexity - O(1)

# Better - Hash-table - Suitable for both Variety 1 & 2
def TwoSum2(arr2,Sum1):
    hash_dict1={}
    for i in range(len(arr2)):
        num1=arr2[i]
        num2=Sum1-num1
        if num2 in hash_dict1:
            return hash_dict1[num2],i # return 'Yes'
        hash_dict1[num1]=i # Keep adding elements to hash_table until we find num2 (another required num) in it
    return 'No'
arr2=[2,6,5,8,11]
Sum1=14
print(TwoSum2(arr2,Sum1))
# Time Complexity - O(N)
# Space Complexity - O(N)

# Optimal - Two pointer - Suitable for only Variety 2
def TwoSum3(arr3,Sum1):
    left,right=0,len(arr3)-1
    arr3.sort() # O(NlogN)
    while left<right:
        if arr3[left]+arr3[right]<Sum1:
            left+=1
        elif arr3[left]+arr3[right]>Sum1:
            right-=1
        else:
            return 'Yes'
    return 'No'
arr3=[2,6,5,8,11]
Sum1=14
print(TwoSum3(arr3,Sum1))
# Time Complexity - O(N) + O(NlogN)
# Space Complexity - O(1)