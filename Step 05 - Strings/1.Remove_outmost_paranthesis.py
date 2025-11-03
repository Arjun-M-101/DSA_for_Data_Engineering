class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        level = 0
        for char in s:
            if char == '(':
                if level > 0:   # not outermost
                    result += '('
                level += 1
            else:  # char == ')'
                level -= 1
                if level > 0:   # not outermost
                    result += ')'
        return result
# Example usage
s = "(()())(())"
sol = Solution()
print(sol.removeOuterParentheses(s))  # Output: "(()())()"
# Time Complexity - O(N)
# Space Complexity - O(1)