# Brute Force

def merge_sort(arr,low,high):
    if low>=high:
        return
    mid = (low+high)//2
    # 1) sort left half
    merge_sort(arr,low,mid)
    # 2) sort right half
    merge_sort(arr,mid+1,high)
    # 3) merge the two sorted halve
    merge_array(arr,low,mid,high)
def merge_array(arr,low,mid,high):
    # pointers for left and right halves
    temp = []
    left=low
    right=mid+1
    # merge by choosing the smaller head each time
    while left<=mid and right<=high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    # flush any leftovers
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    # copy back: align arr[low..high] with temp[0..len-1]
    for idx in range(low,high+1):
        arr[idx]=temp[idx-low]
arr=[0,1,2,0,1,2,1,2,0,0,0,1]
low=0
high=len(arr)-1
merge_sort(arr,low,high)
print(arr)
# Time Complexity - O(N log N)
# Space Complexity - O(N)

# Better
def sort2_0s_1s_2s(arr2):
    count0,count1,count2=0,0,0
    for i in range(len(arr2)): # O(N)
        if arr2[i]==0:
            count0+=1
        if arr2[i]==1:
            count1+=1
        if arr2[i]==2:
            count2+=1
    for zeros in range(count0):
        arr2[zeros]=0
    for ones in range(count0,count0+count1):
        arr2[ones]=1
    for twos in range(count0+count1,count0+count1+count2):
        arr2[twos]=2
    # O(N)
    return arr2
arr2=[0,1,2,0,1,2,1,2,0,0,0,1]
print(sort2_0s_1s_2s(arr2))
# Time Complexity - O(2N)
# Space Complexity - O(1)

# Optimal - Dutch National Flag Alogrithm
def sort3_0s_1s_2s_dutch(arr3):
    low,mid=0,0
    high=len(arr3)-1
    while mid<=high:
        if arr3[mid]==0:
            arr3[low],arr3[mid]=arr3[mid],arr3[low]
            low+=1
            mid+=1
        elif arr3[mid]==1:
            mid+=1
        else:
            arr3[mid],arr3[high]=arr3[high],arr3[mid]
            high-=1
    return arr3
arr3=[0,1,2,0,1,2,1,2,0,0,0,1]
print(sort3_0s_1s_2s_dutch(arr3))
# Time Complexity - O(N)
# Space Complexity - O(1)