# Brute Force
def leaders1(arr1):
    ans=[]
    for i in range(len(arr1)):
        leader=True
        for j in range(i,len(arr1)):
            if arr1[j]>arr1[i]:
                leader=False
                break
        if leader==True:
            ans.append(arr1[i])
    return ans
arr1=[10,22,12,3,0,6]
print(leaders1(arr1))
# Time Complexity ~ O(N^2)
# Space Complexity - O(N) - for ans

# Optimal
def leaders2(arr2):
    ans=[]
    maximum=float('-inf')
    N=len(arr2)
    for i in range(N-1,-1,-1):
        if arr2[i]>maximum:
            maximum=arr2[i]
            ans.append(maximum)
    ans.reverse() # O(m) If wanted output in the same order of array
    return ans
arr2=[10,22,12,3,0,6]
print(leaders2(arr2))
# Time Complexity - O(N) + O(m)
# Space Complexity - O(N) - for ans