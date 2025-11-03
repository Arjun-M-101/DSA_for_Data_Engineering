class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        res = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]  # subtract if smaller before larger
            else:
                res += roman[s[i]]  # add otherwise
        res += roman[s[-1]]  # add last character value
        return res
# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("LVIII"))    # Output: 58
    print(sol.romanToInt("MCMXCIV"))  # Output: 1994
# Time Complexity - O(N)
# Space Complexity - O(1)