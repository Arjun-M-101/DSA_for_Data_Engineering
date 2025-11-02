# Brute Force
def majority1(arr1):
    N=len(arr1)
    limit=N//2
    for i in range(N):
        cnt=0
        for j in range(N):
            if arr1[i]==arr1[j]:
                cnt+=1
        if cnt>limit:
            return arr1[i]
    return -1
arr1=[2,2,3,3,1,2,2]
print(majority1(arr1))
# Time Complexity - O(N^2)
# Space Complexity - O(1)

# Better - Hash-table
def majority2(arr2):
    N=len(arr2)
    limit=N//2
    hash_dict1={}
    for i in range(len(arr2)):
        num = arr2[i]
        hash_dict1[num]=hash_dict1.get(num, 0) + 1
    for k,v in hash_dict1.items():
        if v>limit:
            return k
    return -1
arr2=[2,2,3,3,1,2,2]
print(majority2(arr2))
# Time Complexity - O(2N)
# Space Complexity - O(N)

# Optimal - Moore's Voting Algorithm
def majority3_moore(arr3):
    cnt1,ele=0,0
    N=len(arr3)
    limit=N//2
    for i in range(N):
        if cnt1==0:
            cnt1=1
            ele=arr3[i]
        elif arr3[i]==ele:
            cnt1+=1
        else:
            cnt1-=1
    cnt2=0
    for i in range(N):
        if arr3[i]==ele:
            cnt2+=1
    if cnt2>limit:
        return ele
    return -1
arr3=[2,2,3,3,1,2,2]
print(majority3_moore(arr3))
# Time Complexity - O(N) + O(N)
# Space Complexity - O(1)