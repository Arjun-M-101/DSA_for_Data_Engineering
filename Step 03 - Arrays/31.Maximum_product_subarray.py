# Brute Force - Method 1 
def maximum_array_product1(arr1):
    max_prod = float('-inf')
    for i in range(len(arr1)):
        for j in range(i,len(arr1)):
            prod = 1
            for k in range(i,j+1):
                prod*=arr1[k]
            max_prod=max(max_prod,prod)
    return max_prod
arr1=[2,3,-2,4]
print(maximum_array_product1(arr1))
# Time Complexity - O(N^3)
# Space Complexity - O(1)

# Brute Force - Method 2
def maximum_array_product2(arr2):
    max_prod = float('-inf')
    for i in range(len(arr2)):
        prod = 1
        for j in range(i,len(arr2)):
            prod*=arr2[j]
            max_prod=max(max_prod,prod)
    return max_prod
arr2=[2,3,-2,4]
print(maximum_array_product2(arr2))
# Time Complexity - O(N^2)
# Space Complexity - O(1)

# Optimal - Prefix & Suffix prod
def maximum_array_product3(arr3):
    prefix_prod,suffix_prod=1,1
    max_prod=float('-inf')
    for i in range(len(arr3)):
        if prefix_prod==0:
            prefix_prod=1
        if suffix_prod==0:
            suffix_prod=1
        prefix_prod*=arr3[i]
        suffix_prod*=arr3[len(arr3)-1-i]
        max_prod=max(max_prod,max(prefix_prod,suffix_prod))
    return max_prod
arr3=[2,3,-2,4]
print(maximum_array_product3(arr3))
# Time Complexity - O(N)
# Space Complexity - O(1)