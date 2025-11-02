# Brute Force
def move_zeroes1(arr):
    temp = []
    for i in range(len(arr)): # O(N)
        if arr[i]!=0:
            temp.append(arr[i])
    for j in range(len(temp)): # O(x)
        arr[j]=temp[j]
    for z in range(len(temp),len(arr)): # O(N-x)
        arr[z]=0
    return arr
arr=[1,0,2,3,2,0,0,4,5,1]
print(move_zeroes1(arr))
# Time Complexity - O(2N)
# Space Complexity - O(x) -> O(N) worst case when no zeroes

# Optimal - Two pointer
def move_zeroes2(arr2):
    j=-1
    for i in range(len(arr2)): # O(x)
        if arr2[i]==0:
            j=i
            break
    for k in range(j,len(arr2)): # O(N-x)
        if arr2[k]!=0:
            arr2[k],arr2[j]=arr2[j],arr2[k]
            j+=1
    return arr2
arr2=[1,0,2,3,2,0,0,4,5,1]
print(move_zeroes2(arr))
# Time Complexity - O(N)
# Space Complexity - O(1)