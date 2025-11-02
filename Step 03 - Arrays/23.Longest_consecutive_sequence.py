# Brute Force
def longest1(arr1):
    longest=float('-inf')
    for i in range(len(arr1)):
        num = arr1[i]
        cnt = 1
        while num+1 in arr1:
            num+=1
            cnt+=1
        longest=max(longest,cnt)
    return longest
arr1=[102,4,100,1,101,3,2,1,1]
print(longest1(arr1))
# Time Complexity - O(N^2)
# Space Complexity - O(1)

# Better
def longest2(arr2):
    arr2.sort()
    current_element=arr2[0]
    current_count=1
    longest=current_count
    for i in range(1,len(arr2)):
        if arr2[i]==current_element:
            continue
        elif arr2[i]==current_element+1:
            current_element=arr2[i]
            current_count+=1
            longest=max(longest,current_count)
        else:
            current_element=arr2[i]
            current_count=1
    return longest
arr2=[102,4,100,1,101,3,2,1,1]
print(longest2(arr2))
# Time Complexity - O(NlogN) + O(N)
# Space Complexity - O(1)

# Optimal
def longest3(arr3):
    if len(arr3)==0:
        return 0
    longest = 0
    set1=set(arr3) # Removing duplicates using set ~ O(N)
    for num in set1: # For each number ~ O(2N)
        if num-1 not in set1: # Checking if there are any lower number
            current = num # If no lower number, that is the current number
            cnt = 1 # First occurence of that number
            while current+1 in set1: # Checking if there are higher number
                cnt+=1 # If present increasing count
                current+=1 # Making that higher number current
        longest=max(longest,cnt) # Taking max count
    
    return longest
arr3=[102,4,100,1,101,3,2,1,1]
print(longest3(arr3))
# Time Complexity - O(3N)
# Space Complexity - O(N)