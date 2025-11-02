# Brute Force - Merge Intervals
def merge1(arr1):
    N = len(arr1)
    arr1.sort()   # O(NlogN)
    ans = []
    i = 0
    while i < N:
        start = arr1[i][0]
        end = arr1[i][1]
        # check all later intervals for overlap
        j = i + 1
        while j < N and arr1[j][0] <= end: # To check continuity - if (2) in 2,4 comes between 1,3 - Yes
            end = max(end, arr1[j][1]) # If continous interval, we are taking the max of the y - [j][1]
            j += 1
        ans.append([start, end])
        i = j   # skip over merged intervals
    return ans
arr1 = [[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]
print(merge1(arr1))
# Time Complexity - O(2N) + O(NlogN)
# Space Complexity - O(N)

# Optimal
def merge_optimal(arr2):
    arr2.sort()   # O(N log N)
    ans = [arr2[0]]
    for i in range(1, len(arr2)):
        # if current interval overlaps with last in ans
        if arr2[i][0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], arr2[i][1]) # If the interval extends we are updating the last element
        else:
            ans.append(arr2[i]) # If not we're just including the interval
    return ans
arr2 = [[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]
print(merge_optimal(arr2))
# Time Complexity - O(N) + O(NlogN)
# Space Complexity - O(N)