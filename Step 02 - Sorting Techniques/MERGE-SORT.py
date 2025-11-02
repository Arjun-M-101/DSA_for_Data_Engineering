# MERGE SORT
# Divide & Conquer(Merge) - Algorithm
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
arr=[5,7,2,0,1,8,1,4,9,6]
low=0
high=len(arr)-1
merge_sort(arr,low,high)
print(arr)
'''
Time Complexity:
- Best case:    O(N log N)
- Worst case:   O(N log N)
Space Complexity:
- O(N) auxiliary (for temp array)
- O(log N) recursion stack
'''