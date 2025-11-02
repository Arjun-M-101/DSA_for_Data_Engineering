# INSERTION SORT
array1 = [5,8,2,4,0,1,1]
n=len(array1)
for i in range(1,n): # Why 1 because we are using leftmost approach for comparison
    j = i
    while j>0 and array1[j-1]>array1[j]: # Here j compares the previous element and swaps till the left end
        array1[j-1],array1[j]=array1[j],array1[j-1]
        j-=1 # decrements the j index window (inner for loop) for leftmost comparison approach 
print(array1)
'''
# Time Complexity - O(N^2)
# Time complexity - O(N) - Best case

Insertion Sort = Increasing window size – Right-to-Left approach (insert into place)

Comparison/Shift Window = Between 2 elements till it completes inner loop (Backwards - Fixed for every iteration)

Initial:   [  ?       ?       ?       ?       ?   ]   (all unsorted)
Pass 1:    [  ?   ][  ?       ?       ?       ?   ]   (first element is trivially sorted)
Pass 2:    [sorted][  ?       ?       ?           ]   (2nd element inserted into sorted prefix)
Pass 3:    [sorted][sorted][  ?       ?           ]   (3rd element inserted into sorted prefix)
Pass 4:    [sorted][sorted][sorted][  ?           ] 
Pass 5:    [sorted][sorted][sorted][sorted][sorted]   (fully sorted)
'''