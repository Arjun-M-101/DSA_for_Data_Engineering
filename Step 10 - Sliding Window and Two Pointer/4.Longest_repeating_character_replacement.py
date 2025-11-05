# Brute Force
class Solution1:
    def longest_substring(self, string:str, k:int)->int:
        max_length=float('-inf')
        for i in range(len(string)):
            hash_array=[0]*26
            max_freq=0 # reset for current character
            for j in range(i,len(string)):
                current=ord(string[j])-ord('A')
                hash_array[current]+=1
                max_freq=max(max_freq,hash_array[current])
                changes=(j-i+1)-max_freq # Total count - max frequency
                if changes<=k:
                    max_length=max(max_length,j-i+1)
                else:
                    break
        return max_length
if __name__ == '__main__':
    sol1=Solution1()
    string="AABABBA"
    k=2
    print(sol1.longest_substring(string,k))
# Time Complexity - O(i*j) ~ O(N)
# Space Complexity - O(26)

# Optimal
class Solution2:
    def longest_substring(self, string: str, k: int) -> int:
        left,right,maxCount,maxLength,freq,N = 0,0,0,0,[0]*26,len(string)
        # Iterate through the string with right pointer
        while right<N:
            # Increment the frequency of current character
            current=ord(string[right]) - ord('A')
            freq[current]+= 1
            # Update maxCount with the max frequency seen so far
            maxCount = max(maxCount, freq[current])
            # If the current window is more than k replacements, move left
            while (right - left + 1) - maxCount > k:
                freq[ord(string[left]) - ord('A')] -= 1
                left += 1
            # Update the maximum window length
            maxLength = max(maxLength, right - left + 1)
            right+=1
        # Return the maximum valid window length
        return maxLength
# Driver code
if __name__ == "__main__":
    sol2 = Solution2()
    string = "AABABBA"
    k = 2
    # Output: 5
    print(sol2.longest_substring(string, k))
# Time Complexity - O(N)
# Space Complexity - O(26)