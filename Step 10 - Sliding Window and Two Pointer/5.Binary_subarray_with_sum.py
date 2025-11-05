# Brute Force
class Solution1:
    # Function to count number of subarrays with sum equal to goal
    def numSubarraysWithSum(self, nums, goal):
        # Variable to store the final count of valid subarrays
        count = 0
        # Outer loop to fix the starting index of subarray
        for start in range(len(nums)):
            # Variable to store sum of current subarray
            total = 0
            # Inner loop to fix the ending index of subarray
            for end in range(start, len(nums)):
                # Add the current element to total
                total += nums[end]
                # If subarray sum equals goal, increment count
                if total == goal:
                    count += 1
        # Return the total count of valid subarrays
        return count
# Driver code
if __name__ == "__main__":
    obj1 = Solution1()
    nums = [1, 0, 1, 0, 1]
    goal = 2
    # Output: 4
    print(obj1.numSubarraysWithSum(nums, goal))
# Time Complexity - O(N^2)
# Space Complexity - O(1)

# Optimal
class Solution2:
    # Function to compute number of subarrays with sum exactly equal to goal
    def numSubarraysWithSum(self, nums, goal):
        # Return difference between atMost(goal) and atMost(goal - 1)
        return self.atMost(nums, goal) - self.atMost(nums, goal - 1)
    # Helper function to compute subarrays with sum at most k
    def atMost(self, nums, k):
        # No subarrays for negative sum
        if k < 0:
            return 0
        left = 0
        right = 0
        total = 0
        curr_sum = 0
        # Traverse array using right pointer
        while right<len(nums):
            # Add current element to sum
            curr_sum += nums[right]
            # Shrink window if sum exceeds k
            while curr_sum > k:
                curr_sum -= nums[left]
                left += 1
            # Add number of valid subarrays ending at right
            total += (right - left + 1)
            right +=1
        return total
# Driver code
if __name__ == "__main__":
    sol2 = Solution2()
    nums = [1, 0, 1, 0, 1]
    goal = 2
    print(sol2.numSubarraysWithSum(nums, goal))  # Output: 4
# Time Complexity - O(2N)
# Space Complexity - O(1)