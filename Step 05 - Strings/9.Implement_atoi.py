class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Remove spaces at both ends
        if not s:       # If string is empty after removing spaces, return 0
            return 0
        sign = 1        # Default sign is positive
        start = 0       # Start reading from index 0
        # Check if first character is '+' or '-'
        if s[0] == '-':
            sign = -1    # Negative number
            start = 1    # Start reading digits from next character
        elif s[0] == '+':
            start = 1    # Positive number, start from next character
        num = 0
        # Read digits one by one
        for i in range(start, len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])  # Build the number digit by digit
                # Check for overflow and clamp if necessary
                if sign * num > 2**31 - 1:
                    return 2**31 - 1
                if sign * num < -2**31:
                    return -2**31
            else:
                break  # Stop reading at first non-digit character
        return sign * num  # Return the final signed number
# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("   -42"))            # Output: -42
    print(sol.myAtoi("4193 with words"))   # Output: 4193
    print(sol.myAtoi("words and 987"))     # Output: 0
# Time Complexity - O(N)
# Space Complexity - O(1)