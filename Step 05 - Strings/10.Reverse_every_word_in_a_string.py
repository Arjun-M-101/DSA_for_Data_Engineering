# Brute Force
class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        words = []
        i = 0       
        # Extract words skipping spaces
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            if i >= n:
                break
            start = i
            while i < n and s[i] != ' ':
                i += 1
            end = i - 1
            words.append(s[start:end + 1])      
        # Build reversed string
        ans = ""
        for i in range(len(words) - 1, -1, -1):
            ans += words[i]
            if i != 0:
                ans += ' '
        return ans
# Example Usage
if __name__ == "__main__":
    s = " amazing coding skills "
    sol = Solution()
    ans = sol.reverseWords(s)
    print("Input string:", s)
    print("After reversing every word:", ans)
# Time Complexity - O(N)
# Space Complexity - O(N)

# Optimal - In-place
class Solution:
    def reverseString(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)      
        # Reverse whole string
        self.reverseString(s, 0, n - 1)
        i = 0  # index for placing new characters
        j = 0  # scanning index
        while j < n:
            while j < n and s[j] == ' ':
                j += 1
            if j == n:
                break
            start = i
            while j < n and s[j] != ' ':
                s[i] = s[j]
                i += 1
                j += 1
            end = i - 1
            # Reverse each word
            self.reverseString(s, start, end)
            if j < n:
                s[i] = ' '
                i += 1
        # Remove trailing space if exists
        if i > 0 and s[i - 1] == ' ':
            i -= 1
        return "".join(s[:i])
# Example Usage
if __name__ == "__main__":
    s = " amazing coding skills "
    sol = Solution()
    ans = sol.reverseWords(s)
    print("Input string:", s)
    print("After reversing every word:", ans)
# Time Complexity - O(N)
# Space Complexity - O(1)