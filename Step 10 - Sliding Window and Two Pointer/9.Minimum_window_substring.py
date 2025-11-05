# Brute Force
class Solution1:
    def minimum_window_substring(self, string1:str, string2:str)->str:
        min_length = float('inf')
        start_index = -1
        for i in range(len(string1)):
            hash_array = [0]*256
            count = 0
            for ch in string2:
                hash_array[ord(ch)] += 1
            for j in range(i, len(string1)):
                if hash_array[ord(string1[j])] > 0:
                    count += 1
                    hash_array[ord(string1[j])] -= 1
                if count == len(string2):
                    if j - i + 1 < min_length:
                        min_length = j - i + 1
                        start_index = i
                    break
        if start_index == -1:
            return ""  # No such window
        return string1[start_index:start_index + min_length]
if __name__ == '__main__':
    sol1 = Solution1()
    string1 = "ddaaabbca"
    string2 = "abc"
    print(sol1.minimum_window_substring(string1, string2))
# Time Complexity - O(i+j)
# Space Complexity - O(256)

class Solution2:
    def minimum_window_substring(self, string1: str, string2: str) -> str:
        N, M = len(string1), len(string2)   # N = length of main string, M = length of target string
        l, r = 0, 0                         # l = left pointer, r = right pointer (sliding window boundaries)
        min_length = float('inf')           # Track the length of the smallest valid window found so far
        start_index = -1                    # Track the starting index of the smallest valid window
        count = 0                           # Number of characters from string2 matched so far
        hash_array = [0] * 256              # Frequency array for ASCII chars (size 256 covers all characters)
        # Step 1: Build frequency map of characters required from string2
        for i in range(M):
            hash_array[ord(string2[i])] += 1
        # Step 2: Expand the window by moving the right pointer 'r'
        while r < N:
            # If the current character at r is still needed (frequency > 0), 
            # it contributes to satisfying string2, so increment count
            if hash_array[ord(string1[r])] > 0:
                count += 1
            # Decrement frequency for this character because it's now included in the window
            hash_array[ord(string1[r])] -= 1
            # Move right pointer forward to expand the window
            r += 1
            # Step 3: When all characters from string2 are matched (count == M)
            while count == M:
                # Update minimum window if the current window is smaller
                if (r - l) < min_length:
                    min_length = r - l
                    start_index = l
                # Before shrinking the window, restore frequency of the leftmost character
                hash_array[ord(string1[l])] += 1
                # If restoring makes its frequency > 0, it means this character was required,
                # and by removing it we are now missing one required character → decrease count
                if hash_array[ord(string1[l])] > 0:
                    count -= 1
                # Shrink the window from the left
                l += 1
        # Step 4: If no valid window was found, return empty string
        if start_index == -1:
            return ""
        else:
            # Otherwise, return the substring starting at start_index with length = min_length
            return string1[start_index:start_index + min_length]
# Driver code to test
if __name__ == '__main__':
    sol2 = Solution2()
    string1 = "ddaaabbca"
    string2 = "abc"
    print(sol2.minimum_window_substring(string1, string2))  # Expected output: "bca"
# Time Complexity: O(N + M)
#   - O(M) to build frequency map of string2
#   - O(N) to slide the window across string1 (each char visited at most twice: once by r, once by l)
# Space Complexity: O(256)
#   - Constant space for ASCII frequency array