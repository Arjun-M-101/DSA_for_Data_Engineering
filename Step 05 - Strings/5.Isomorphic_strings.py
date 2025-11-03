class Solution:
    def isomorphicString(self, s: str, t: str) -> bool:
        # Step 1: If lengths differ, they can't be isomorphic
        if len(s) != len(t):
            return False
        # Step 2: Create two arrays of size 256 (for all ASCII characters)
        m1 = [0] * 256  # Tracks last seen position of characters in s
        m2 = [0] * 256  # Tracks last seen position of characters in t
        # Step 3: Loop through each character in both strings
        for i in range(len(s)):
            c1 = ord(s[i])  # ASCII value of s[i]
            c2 = ord(t[i])  # ASCII value of t[i]
            # Step 4: Compare last seen positions
            if m1[c1] != m2[c2]:
                return False  # Mismatch in pattern
            # Step 5: Update last seen positions to current index + 1
            m1[c1] = i + 1
            m2[c2] = i + 1
        # Step 6: All checks passed → strings are isomorphic
        return True
# 🔍 Test cases
sol = Solution()
print(sol.isomorphicString("paper", "title"))  # True
print(sol.isomorphicString("foo", "bar"))      # False
print(sol.isomorphicString("egg", "add"))      # True
print(sol.isomorphicString("ab", "aa"))        # False
# Time Complexity - O(N)
# Space Complexity - O(1)