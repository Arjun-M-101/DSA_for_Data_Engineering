# Brute Force
# Variety 1 - No. of negatives & positives are equal
def rearrange_odd_even1(arr1):
    positives=[]
    negatives=[]
    for i in range(len(arr1)):
        if arr1[i]>=0:
            positives.append(arr1[i])
        else:
            negatives.append(arr1[i])
    for j in range(len(arr1)//2):
        arr1[j*2]=positives[j]
        arr1[j*2+1]=negatives[j]
    return arr1
arr1 = [3,1,-2,-5,2,-4]
print(rearrange_odd_even1(arr1))
# Time Complexity - O(2N)
# Space Complexity - O(N)

# Optimal - Two pointers
def rearrange_odd_even2(arr2):
    if arr2[0]>=0:
        pos,neg=0,1
    elif arr2[0]<0:
        neg,pos=0,1
    ans=[0]*len(arr2)
    for i in range(len(arr2)):
        if arr2[i]>=0:
            ans[pos]=arr2[i]
            pos+=2
        else:
            ans[neg]=arr2[i]
            neg+=2
    return ans
arr2 = [3,1,-2,-5,2,-4]
print(rearrange_odd_even2(arr2))
# Time Complexity - O(N)
# Space Complexity - O(N)

# Variety 2 - No. of negatives & positives are not equal
# Optimal - Two pointers
def rearrange_odd_even3(arr3):
    positives,negatives=[],[] # Initiate empty arrays to store +ve & -ve values
    for i in range(len(arr3)):
        if arr3[i]>=0:
            positives.append(arr3[i]) # Store +ve
        else:
            negatives.append(arr3[i]) # Store -ve
    if len(positives)<=len(negatives): # Find the common array limit between +ve & -ve
        limit = len(positives)
    else:
        limit = len(negatives)
    index=0 # Initial index
    if arr3[0]>=0: # Flag to check first value
        start_positive=True
    else:
        start_positive=False
    for j in range(limit):
        if start_positive: # If initial value is positive
            arr3[index]=positives[j] # Insert +ve first at 0 index
            arr3[index+1]=negatives[j] # Insert -ve first at 0 index+1
        else: # If initial value is negative
            arr3[index]=negatives[j] # Insert -ve first at 0 index
            arr3[index+1]=positives[j] # Insert +ve first at 0 index+1
        index+=2 # increment by 2 due to gap between +ve & -ve
    if len(positives)>len(negatives): # Add leftovers to the array
        arr3[index:]=positives[limit:] # Use the last index of array to modify leftovers of +ve
    else:
        arr3[index:]=negatives[limit:] # Use the last index of array to modify leftovers of -ve
    return arr3
arr3 = [-1,2,3,4,-3,1]
print(rearrange_odd_even3(arr3))
# Time Complexity - O(2N)
# Space Complexity - O(N)