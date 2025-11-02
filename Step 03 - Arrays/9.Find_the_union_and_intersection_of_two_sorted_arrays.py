# UNION

# Brute Force
def union_array1(arr1,arr2):
    set1=set()
    for a1 in range(len(arr1)): # O(n1)
        set1.add(arr1[a1])
    for a2 in range(len(arr2)): # O(n2)
        set1.add(arr2[a2])
    return sorted(list(set1)) #  O((n1+n2) log(n1+n2))
arr1=[1,1,2,3,4,5]
arr2=[2,3,4,4,5,6]
print(union_array1(arr1,arr2))
# Time-Complexity =  #  O((n1+n2) log(n1+n2)) + O(n1+n2)
# Space-Complexity = O(n1+n2) - set
# For return answer = O(n1+n2) - list

# Optimal
def union_array2(arr11,arr21):
    i,j=0,0
    result = []
    while i<=len(arr11)-1 and j<=len(arr21)-1:
        if arr11[i]<=arr21[j]: # O(n1)
            if arr11[i] not in result:
                result.append(arr11[i])
            i+=1
        else: # O(n2)
            if arr21[j] not in result:
                result.append(arr21[j])
            j+=1
    while i<=len(arr11)-1:
        if arr11[i] not in result:
            result.append(arr11[i]) # To check & append any leftovers from arr11
        i+=1
    while j<=len(arr21)-1:
        if arr21[j] not in result:
            result.append(arr21[j])  #To check & append any leftovers from arr21
        j+=1
    return result
arr11=[1,1,2,3,4,5]
arr21=[2,3,4,4,5,6]
print(union_array2(arr11,arr21))
# Time-Complexity = O(n1+n2)
# Space-Complexity = O(n1+n2) - list

# INTERSECTION

# Brute Force
def intersection_array1(arr12,arr22):
    visited=[0]*len(arr22)
    result = []
    for i in range(0,len(arr12)):
        for j in range(0,len(arr22)):
            if arr12[i]==arr22[j] and visited[j]== 0:
                result.append(arr12[i])
                visited[j]=1
                break
            if arr22[j]>arr12[i]:
                break
    return result
arr12=[1,2,2,3,3,4,5,6]
arr22=[2,3,3,5,6,6,7]
print(intersection_array1(arr12,arr22))
# Time-Complexity = O(n1*n2)
# Space-Complexity = O(n2)

def intersection_array2(arr13,arr23):
    result = []
    i,j=0,0
    while i<len(arr13) and j<len(arr23):
        if arr13[i]<arr23[j]:
            i+=1
        elif arr23[j]<arr13[i]:
            j+=1
        else: # arr13[i] == arr23[j]
            result.append(arr13[i])
            i+=1
            j+=1
    return result
arr13=[1,2,2,3,3,4,5,6]
arr23=[2,3,3,5,6,6,7]
print(intersection_array2(arr13,arr23))
# Time-Complexity = O(n1+n2)
# Space Complexity = O(1) extra (O(min(n1,n2)) for result list)