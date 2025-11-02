# Brute Force
# Formula ans[j][n-1-i] = a1[i][j]

def rotate_matrix1(a1):
    n=len(a1)
    ans=[[0]*n for _ in range(n)] # Create empty array of same size
    for i in range(n):
        for j in range(n):
            ans[j][n-1-i] = a1[i][j] # Apply the formula
    return ans
a1=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(rotate_matrix1(a1))
# Time Complexity - O(N^2)
# Space Complexity - O(N^2)

# Optimal - Inplace
# Trick:
# 1. Transpose - Leave the diagonal. But change the remaining like this
# For every i -> 0 to n-1 & j -> i+1 to n-1. Swap the elements
# 2. Reverse

def rotate_matrix2(a2):
    n=len(a2)
    for i in range(n): # O(N/2 * N/2)
        for j in range(i+1,n):
            a2[i][j],a2[j][i] = a2[j][i],a2[i][j]
    for i in range(n): # O(N * N/2)
        a2[i].reverse()
    return a2
a2=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(rotate_matrix2(a2))
# Time Complexity - O(N/2 * N/2) + O(N * N/2) ~ O(N^2)
# Space Complexity - O(1)