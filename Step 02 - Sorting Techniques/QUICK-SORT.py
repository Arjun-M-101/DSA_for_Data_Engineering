# QUICK SORT
# Divide & Conquer
def quick_sort(arr, low, high):
    if low < high:
        partition_index = find_pivot(arr, low, high)
        quick_sort(arr, low, partition_index)       # left side
        quick_sort(arr, partition_index + 1, high)  # right side
def find_pivot(arr, low, high):
    pivot = arr[(low+high)//2]   # choose first element as pivot
    i = low
    j = high
    while True:
        if i >= j: # Base condition - keep crossing i & j until i is greater than j
            return j   # partition index
        # increment ith index right until arr[i] >= pivot is found - to swap greater elements after pivot
        while arr[i] < pivot:
            i += 1
        # decrement jth index left until arr[j] <= pivot is found - to swap lesser elements before pivot
        while arr[j] > pivot:
            j -= 1
        # swap out-of-place elements
        # > For i, swap the ith element with jth element to bring ith element right which is greater than pivot
        # > For j, swap the jth element with ith element to bring jth element left which is lesser than pivot
        arr[i], arr[j] = arr[j], arr[i]
arr=[4,6,2,5,7,9,1,3]
low=0
high=len(arr)-1
quick_sort(arr,low,high)
print(arr)
'''
Time Complexity:
- Best case:    O(N log N)
- Average case: O(N log N)
Space Complexity:
- O(1) auxiliary (for temp array)
- O(log N) recursion stack
'''