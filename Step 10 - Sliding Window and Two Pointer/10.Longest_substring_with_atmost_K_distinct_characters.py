# Brute Force
class Solution1:
    # Function to calculate longest substring with at most K distinct characters
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Track the maximum valid substring length
        max_len = 0
        # Try every possible starting index
        for i in range(len(s)):
            # Use dictionary to count frequencies of characters
            freq = {}
            # Expand the substring from index i
            for j in range(i, len(s)):
                # Update character frequency
                freq[s[j]] = freq.get(s[j], 0) + 1
                # If more than k distinct characters, stop expanding
                if len(freq) > k:
                    break
                # Update the maximum length
                max_len = max(max_len, j - i + 1)
        # Return the result
        return max_len
# Driver code
if __name__ == "__main__":
    sol1 = Solution1()
    s = "aaabbccd"
    k = 2
    print(sol1.lengthOfLongestSubstringKDistinct(s, k))
# Time Complexity - O(i*j) ~ O(N^2)
# Space Complexity - O(k)

# Optimal
class Solution2:
    # Function to return length of longest substring with at most K distinct characters
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Edge case
        if k == 0 or not s:
            return 0
        # Dictionary to store frequency of characters
        freq = {}
        # Initialize pointers and result
        left, right = 0, 0
        maxLen = 0
        # Iterate using right pointer
        while right < len(s):
            # Add current char to freq map
            freq[s[right]] = freq.get(s[right], 0) + 1
            # Shrink window if needed
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0: # Once the frequency is decreased
                    del freq[s[left]] # remove the element
                left += 1 # Move left pointer
            # Update maxLen
            maxLen = max(maxLen, right - left + 1)
            right +=1
        return maxLen
# Driver code
if __name__ == "__main__":
    sol2 = Solution2()
    s = "aaabbccd"
    k = 2
    print(sol2.lengthOfLongestSubstringKDistinct(s, k))