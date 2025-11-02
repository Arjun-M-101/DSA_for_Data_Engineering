# Brute Force
def count_inversions1(arr1):
    count=0
    ans=[]
    for i in range(len(arr1)):
        for j in range(i+1,len(arr1)):
            if arr1[i]>arr1[j]:
                count+=1
                #ans.append([arr1[i],arr1[j]])
    return count #, ans
arr1=[5,3,2,4,1]
print(count_inversions1(arr1))
# Time Complexity - O(N^2)
# Space Complexity - O(1) - If ans not used

# Optimal
def merge_sort_count(arr):
    def merge_sort(arr, temp, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += merge_sort(arr, temp, left, mid)
            inv_count += merge_sort(arr, temp, mid+1, right)
            inv_count += merge(arr, temp, left, mid, right)
        return inv_count
    def merge(arr, temp, left, mid, right):
        i, j, k = left, mid+1, left
        inv_count = 0
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                inv_count += (mid - i + 1)  # all remaining in left half are > arr[j]
                j += 1
            k += 1
        while i <= mid:
            temp[k] = arr[i]; i += 1; k += 1
        while j <= right:
            temp[k] = arr[j]; j += 1; k += 1
        for idx in range(left, right+1):
            arr[idx] = temp[idx]
        return inv_count
    return merge_sort(arr, [0]*len(arr), 0, len(arr)-1)
arr2 = [5,3,2,4,1]
print(merge_sort_count(arr2))
# Time Complexity - O(NlogN)
# Space Complexity - O(N)