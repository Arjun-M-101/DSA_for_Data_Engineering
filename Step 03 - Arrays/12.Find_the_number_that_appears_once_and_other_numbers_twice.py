# Brute Force
def count_once1(arr1):
    for i in range(len(arr1)):
        num = arr1[i]
        count1 = 0 # Count is reset to 0 for every element
        for j in range(len(arr1)):
            if arr1[j]==num:
                count1+=1
        if count1 == 1:
            return num
arr1=[1,1,2,3,3,4,4]
print(count_once1(arr1))
# Time Complexity - O(N^2)
# Space Complexity - O(1)

# Better - method1: hash_array
def count_once2(arr2):
    m=0
    for i in range(len(arr2)):
        m=max(arr2[i],m)
    hash_array1=[0]*(m+1)
    for j in range(len(arr2)):
        hash_array1[arr2[j]]+=1
    for k in range(len(hash_array1)):
        if hash_array1[k]==1:
            return k
arr2=[1,1,2,3,3,4,4]
print(count_once2(arr2))
# Time Complexity - O(3N)
# Space Complexity - O(m)

# But when the array has negative elements, numbers with high range. Hash_array is not suitable

# Better - method2: hash_table
def count_once3(arr3):
    hash_dict1={}
    for i in range(len(arr3)): # O(N)
        hash_dict1[arr3[i]]=hash_dict1.get(arr3[i],0)+1
    for k,v in hash_dict1.items(): # O(N/2 + 1)
        if v==1:
            return k
arr3=[1,1,2,3,3,4,4]
print(count_once3(arr3))
# Time Complexity - O(N) + O(N/2 + 1)
# Space Complexity - O(1) + O(N/2 + 1)

# Optimal - XOR
def count_once4(arr4):
    xor1=0
    for i in range(len(arr4)):
        xor1^=arr4[i]
    return xor1
arr4=[1,1,2,3,3,4,4]
print(count_once4(arr4))
# Time Complexity - O(N)
# Space Complexity - O(1)