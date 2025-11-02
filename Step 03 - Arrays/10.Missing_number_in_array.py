# Brute Force
def find_missing_n1(arr1,N):
    for i in range(1,N+1): # Outer loop → i = 1, 2, 3, 4, 5
        flag = 0
        for j in range(len(arr1)): # Inner loop → j = 0..len(arr1)-1
            if arr1[j]==i:
                flag = 1
                break # exits only the INNER loop
        if flag == 0: # As soon as the INNER loop ends it checks the flag for given number
            return i # It returns the missing number if flag is 0
arr1=[1,2,4,5]
N=5
print(find_missing_n1(arr1,N))
# Time Complexity ~ O(N^2)
# Space Complexity - O(1)

# Better
def find_missing_n2(arr2,N):
    hash_array1=[0]*(N+1)
    for i in range(0,len(arr2)):
        hash_array1[arr2[i]]=1
    for j in range(1,N+1):
        if hash_array1[j]==0:
            return j
arr2=[1,2,4,5]
N=5
print(find_missing_n2(arr2,N))
# Time Complexity - O(2N)
# Space Complexity - O(N)

# Optimal - method1 - SUM
def find_missing_n3(arr3,N):
    sum1=(N*(N+1))/2
    sum2 = 0
    for i in range(0,len(arr3)):
        sum2 += arr3[i]
    return sum1-sum2
arr3=[1,2,4,5]
N=5
print(find_missing_n2(arr3,N))
# Time Complexity - O(N)
# Space Complexity - O(1)

# Optimal - method2 - XOR
def find_missing_n4(arr4,N):
    xor1,xor2=0,0
    for i in range(0,N-1):
        xor1^=arr4[i] # XOR with array element
        xor2^=(i+1) # XOR with natural number 1..N-1
    xor2^=N # include the last number N
    return xor1^xor2
arr4=[1,2,4,5]
N=5
print(find_missing_n4(arr4,N))
# Time Complexity - O(N)
# Space Complexity - O(1)

# Why XOR? Because when the N range is high N(N+1)/2 becomes very high.
# Int cannot hold that much bigger range. That's why XOR.