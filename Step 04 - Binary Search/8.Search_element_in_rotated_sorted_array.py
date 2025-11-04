# Brute Force - Linear Search
class Solution1:
    def search(self, arr, n, k):
        for i in range(n):
            if arr[i] == k:
                return i
        return -1
if __name__ == "__main__":
    result=Solution1()
    arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    n = 9
    k = 1
    ans = result.search(arr, n, k)
    if ans == -1:
        print("Target is not present.")
    else:
        print("The index is:", ans)
# Time Complexity - O(N)
# Space Complexity - O(1)

# Optimal - Binary Search
class Solution2:
    def search(self, arr, n, k):
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            # if mid points the target
            if arr[mid] == k:
                return mid
            # if left part is sorted
            if arr[low] <= arr[mid]:
                if arr[low] <= k and k <= arr[mid]: # If k lies between low & mid
                    # element exists
                    high = mid - 1
                else:
                    # element does not exist
                    low = mid + 1
            else:  # if right part is sorted
                if arr[mid] <= k and k <= arr[high]: # If k lies between mid & high
                    # element exists
                    low = mid + 1
                else:
                    # element does not exist
                    high = mid - 1
        return -1
if __name__ == "__main__":
    result=Solution2()
    arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    n = 9
    k = 1
    ans = result.search(arr, n, k)
    if ans == -1:
        print("Target is not present.")
    else:
        print("The index is:", ans)
# Time Complexity - O(logN)
# Space Complexity - O(1)