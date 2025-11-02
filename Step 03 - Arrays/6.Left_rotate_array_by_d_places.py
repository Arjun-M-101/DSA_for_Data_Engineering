# Brute Force
# LEFT ROTATION
def left_rotated(arr,d):
    d=d%len(arr)
    temp = arr[0:d] # Time Complexity - O(D)
    for i in range(d,len(arr)): # Time Complexity - O(N-D)
        arr[i-d]=arr[i]
    # index = 0, since starts from 0
    for j in range(len(arr)-d,len(arr)): # Time Complexity - O(D)
        # the index of temp can be recaptured as j-(len(arr)-d)=0
        arr[j]=temp[j-(len(arr)-d)] # Space Complexity - O(D)
    return arr
arr=[1,2,3,4,5,6,7]
print(left_rotated(arr,2))
# Time Complexity - O(N+D)
# Space Complexity - O(D)

# Optimal - Reverse method
def left_rotated2(arr2,d):
    arr2[:d]=reversed(arr2[:d])
    arr2[d:]=reversed(arr2[d:])
    arr2.reverse()
    return arr
arr2=[1,2,3,4,5,6,7]
print(left_rotated2(arr2,2))
# Time Complexity - O(2N)
# Space Complexity - O(1)

# Optimal - Reverse method in-place
def left_rotated3(arr3,d):
    reverse_array(0,d-1,arr3)
    reverse_array(d,len(arr3)-1,arr3)
    reverse_array(0,len(arr3)-1,arr3)
    return arr3
def reverse_array(left,right,arr):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1  
arr3=[1,2,3,4,5,6,7]
print(left_rotated3(arr3,2))
# Time Complexity - O(2N)
# Space Complexity - O(1)

# ROTATION

# Optimal - Reverse method
def right_rotated1(arr4,d):
    arr4[:len(arr)-d]=reversed(arr4[:len(arr)-d])
    arr4[len(arr)-d:]=reversed(arr4[len(arr)-d:])
    arr4.reverse()
    return arr4
arr4=[1,2,3,4,5,6,7]
print(right_rotated1(arr4,2))
# Time Complexity - O(2N)
# Space Complexity - O(1)

# Optimal - Reverse method in-place
def right_rotated2(arr5,d):
    reverse_array(0,len(arr)-d-1,arr5)
    reverse_array(len(arr)-d,len(arr5)-1,arr5)
    reverse_array(0,len(arr5)-1,arr5)
    return arr5
def reverse_array(left,right,arr):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1  
arr5=[1,2,3,4,5,6,7]
print(right_rotated2(arr5,2))
# Time Complexity - O(2N)
# Space Complexity - O(1)