# Brute Force
def merge_arrays1(arr1,arr2):
    ans=[]
    N1, N2 = len(arr1), len(arr2)
    left,right=0,0
    while left<N1 and right<N2:
        if arr1[left]<=arr2[right]:
            ans.append(arr1[left])
            left+=1
        else:
            ans.append(arr2[right])
            right+=1
    # Leftovers from arr1
    while left< N1:
        ans.append(arr1[left])
        left+= 1
    # Leftovers from arr2
    while right< N2:
        ans.append(arr2[right])
        right+= 1
    # Copy back into arr1 and arr2
    for a in range(N1):
        arr1[a] = ans[a]
    for b in range(N2):
        arr2[b] = ans[N1 + b]
    return arr1,arr2
arr1 = [1,3,5,7]
arr2 = [2,4,6,8,9]
print(merge_arrays1(arr1,arr2))
# Time Complexity - O(N1+N2) + O(N1+N2) to put them back
# Space Complexity - O(N1+N2)

# Optimal - Method 1
def merge_arrays2(arr3,arr4):
    N1, N2 = len(arr3), len(arr4)
    left,right=len(arr3)-1,0
    # Step 1: Swap until order is correct
    while left>=0 and right<N2:
        if arr3[left]>arr4[right]:
            arr3[left],arr4[right]=arr4[right],arr3[left]
            left-=1
            right+=1
        else:
            break
    # Step 2: Sort both arrays individually
    arr3.sort()
    arr4.sort()
    return arr3, arr4
arr3 = [1,3,5,7]
arr4 = [2,4,6,8,9]
print(merge_arrays2(arr3,arr4))
# Time Complexity - O(min(min(N1,N2)) + O(N1 log N1 + N2 log N2) to sort
# Space Complexity - O(1)

# Optimal - Gap method (Shell sort) - Method 2
def merge_gap(arr1, arr2):
    n, m = len(arr1), len(arr2)
    total = n + m
    # initial gap
    gap = (total // 2) + (total % 2)
    while gap > 0:
        i, j = 0, gap
        while j < total:
            # get values from combined virtual array
            if i < n:
                a = arr1[i]
            else:
                a = arr2[i - n]
            if j < n:
                b = arr1[j]
            else:
                b = arr2[j - n]
            # swap if out of order
            if a > b:
                if i < n and j < n:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                elif i < n and j >= n:
                    arr1[i], arr2[j - n] = arr2[j - n], arr1[i]
                else:
                    arr2[i - n], arr2[j - n] = arr2[j - n], arr2[i - n]
            i += 1
            j += 1
        if gap == 1:
            break
        gap = (gap // 2) + (gap % 2)
    return arr1, arr2
# Example
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8, 9]
print(merge_gap(arr1, arr2))
# Time Complexity - O(min(min(N1,N2)) + O(N1 log N1 + N2 log N2) to sort
# Space Complexity - O(1)