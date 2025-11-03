# Brute Force
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            rotated = s[i:] + s[:i]  # slice and rotate
            if rotated == goal:
                return True
        return False
# Test
sol = Solution()
print(sol.rotateString("rotation", "tionrota"))  # True
print(sol.rotateString("hello", "lohelx"))       # False
# Time Complexity - O(N^2)
# Space Complexity - O(1)

# Optimal
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        doubled_s = s + s
        return goal in doubled_s
# Test
sol = Solution()
print(sol.rotateString("rotation", "tionrota"))  # True
print(sol.rotateString("hello", "lohelx"))       # False
# Time Complexity - O(N)
# Space Complexity - O(1)