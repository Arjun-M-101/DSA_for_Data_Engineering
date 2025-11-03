class Solution:
    def largeOddNum(self, s: str) -> str:
        # Step 1: find the last odd digit
        ind = -1
        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) % 2 == 1:
                ind = i
                break     
        # If no odd digit found
        if ind == -1:
            return ""       
        # Step 2: skip leading zeros
        start = 0
        while start <= ind and s[start] == '0':
            start += 1       
        # Step 3: return substring
        return s[start:ind + 1]
# Example usage
sol = Solution()
print(sol.largeOddNum("53476"))      # "5347"
print(sol.largeOddNum("0214638"))   # "21463"
print(sol.largeOddNum("504"))       # "5"
print(sol.largeOddNum("42068"))     # "" (no odd digit)