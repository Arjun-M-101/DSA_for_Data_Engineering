# Sorting method
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""      
        # Sort strings
        strs.sort()
        first, last = strs[0], strs[-1]
        # Compare first and last
        prefix = ""
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                prefix += first[i]
            else:
                break
        return prefix
# Example
print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"
print(Solution().longestCommonPrefix(["apple", "banana", "grape"]))  # ""
# Time Complexity - O(NlogN + M)
# Space Complexity - O(1)

# Vertical Scanning - No sorting
def longestCommonPrefixVertical(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        i = 0
        while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
            i += 1
        prefix = prefix[:i]
        if not prefix:
            break
    return prefix
print(longestCommonPrefixVertical(["interview", "internet", "internal", "interval"]))  # "inter"
# Time Complexity - O(N*M)
# Space Complexity - O(1)