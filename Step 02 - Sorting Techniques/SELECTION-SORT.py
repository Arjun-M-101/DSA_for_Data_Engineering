# SELECTION SORT
# Index range 0 to n (for - outer)
# min index moved from 1 to n (for - inner)
array1 = [5,8,2,4,0,1,1]
n=len(array1)
for i in range(n):
    min_idx=i
    for j in range(i+1,n):
        if array1[j]<array1[min_idx]:
            min_idx=j
    array1[i],array1[min_idx]=array1[min_idx],array1[i]
    # Here swapping of elements happens only if any minimum found or else no swap
print(array1)
'''
# Time Complexity - O(N^2)

Selection Sort = Decreasing window size - Left-to-Right approach

Comparison/Swap Window = Over all elements (Decreasing for every iteration)

Initial:   [ ?    ?    ?    ?    ? ]   (all unsorted)
Step 1:    [min][ ?    ?    ?    ? ]   (first element fixed)
Step 2:    [min][min][ ?    ?    ? ] 
Step 3:    [min][min][min][ ?    ? ]
Step 4:    [min][min][min][min][ ? ]
Step 5:    [min][min][min][min][min]   (fully sorted)
'''