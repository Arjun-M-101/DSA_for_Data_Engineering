# BUBBLE SORT
# Pushes the maximum element at last by adjacent swaps
array1 = [5,8,2,4,0,1,1]
n=len(array1)
for i in range(n-1):          # 0 to n-2
    didSwap = 0
    for j in range(n-1-i):    # shrink inner loop each pass
        if array1[j] > array1[j+1]:
            array1[j], array1[j+1] = array1[j+1], array1[j]
            didSwap = 1
    if didSwap == 0: # O(N) - Best case
        break
print(array1)
'''
# Time Complexity - O(N^2) - Worst case
# Time Complexity - O(N) - Best case (If optimized)

Bubble Sort = Increasing window size – Right-to-Left approach (max bubbles right)

Comparison/Swap Window = Between 2 elements in inner loop (Fixed for every iteration)

Initial:   [ ?    ?    ?    ?    ? ]   (all unsorted)
Pass 1:    [ ?    ?    ?    ? ][max]   (largest element bubbled to end)
Pass 2:    [ ?    ?    ? ][max][max]   (second largest fixed)
Pass 3:    [ ?    ? ][max][max][max]
Pass 4:    [ ? ][max][max][max][max]
Pass 5:    [max][max][max][max][max]   (fully sorted)
'''