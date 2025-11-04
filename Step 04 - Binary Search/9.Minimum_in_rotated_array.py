# Brute Force
class Solution1:
    def findMin(self, nums):
        # Initialize answer with a large number
        min_val = float('inf')
        # Traverse each element
        for i in range(len(nums)):
            # Update minimum value
            min_val = min(min_val, nums[i])
        return min_val
nums = [4, 5, 6, 7, 0, 1, 2]
sol1 = Solution1()
result = sol1.findMin(nums)
print("Minimum element is", result)
# Time Complexity - O(N)
# Space Complexity - O(1)

# Optimal
class Solution2:
    def findMin(self, nums):
        low, high = 0, len(nums) - 1
        min_val = float('inf')
        while low <= high:
            mid = low + (high - low) // 2
            # Check which half to discard
            if nums[low]<=nums[mid]: # Minimum lies in left half
                min_val = min(min_val, nums[low]) # Take the smallest of left half
                low = mid + 1 # And elimate the left half
            else: # Minimum lies in left half (including mid)
                min_val = min(min_val, nums[mid])
                high = mid # And elimate the righ half
        return min_val # or return nums[low] - if min_val not used
nums = [4, 5, 6, 7, 0, 1, 2]
sol2 = Solution2()
result = sol2.findMin(nums)
print("Minimum element is", result)
# Time Complexity - O(logN)
# Space Complexity - O(1)