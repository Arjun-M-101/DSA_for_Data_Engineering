# Optimal
def maximum(arr1):
    cnt=0
    m=0
    for i in range(len(arr1)):
        if arr1[i]==1:
            cnt+=1
            m=max(m,cnt)
        else:
            cnt=0
    return m
arr1=[1,1,0,1,1,1,0,1,1]
print(maximum(arr1))
# Time Complexity - O(N)
# Space Complexity - O(1)