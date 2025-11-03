# Brute Force
def areAnagrams_sort(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)
# Test
print(areAnagrams_sort("CAT", "ACT"))     # True
print(areAnagrams_sort("RULES", "LESRT")) # False
# Time Complexity - O(NlogN)
# Space Complexity - O(1)

# Optimal
def areAnagrams_count(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    freq = [0] * 26  # assuming uppercase A–Z
    for c in s1:
        freq[ord(c) - ord('A')] += 1
    for c in s2:
        freq[ord(c) - ord('A')] -= 1
    # If all counts are zero, it's an anagram
    return all(f == 0 for f in freq)
# Test
print(areAnagrams_count("INTEGER", "TEGERNI")) # True
print(areAnagrams_count("RULES", "LESRT"))     # False
# Time Complexity - O(N)
# Space Complexity - O(1)