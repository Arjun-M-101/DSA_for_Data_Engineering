class Solution:
    def frequencySort(self, s: str):
        # Step 1: Count frequency
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        # Step 2: Sort directly on freq.items()
        # (-v, k) ensures: higher frequency first, then alphabetical
        sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        # Step 3: Extract characters in order
        return [k for k, _ in sorted_items]
# 🔍 Test
sol = Solution()
print(sol.frequencySort("tree"))     # ['e', 'r', 't']
print(sol.frequencySort("raaaajj"))  # ['a', 'j', 'r']
# Time Complexity - O(n + k log k)
# Space Complexity - O(k)