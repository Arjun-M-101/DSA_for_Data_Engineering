# Brute Force
class Solution1:
    def longest_substring(self, string:str)->int:
        max_length=float('-inf')
        for i in range(len(string)):
            hash_array=[0]*256
            for j in range(i,len(string)):
                if hash_array[ord(string[j])]==1:
                    break
                length=j-i+1
                max_length=max(max_length,length)
                hash_array[ord(string[j])]=1
        return max_length
if __name__ == '__main__':
    sol1=Solution1()
    string="abcabcbb"
    x=6
    print(sol1.longest_substring(string))
# Time Complexity - O(i*j)
# Space Complexity - O(N)

# Optimal - Two pointer & Sliding window
class Solution2:
    def longest_substring(self, string:str)->int:
        max_length=float('-inf')
        N=len(string)
        left,right=0,0
        hash_array=[-1]*256
        while right<N:
            if hash_array[ord(string[right])]!=-1: # If already present
                if hash_array[ord(string[right])]>=left: # If it's present after left
                    left=hash_array[ord(string[right])]+1 # Move left to new position
            length=right-left+1 # Calculate new length
            max_length=max(max_length,length)
            hash_array[ord(string[right])]=right # Mark position
            right+=1
        return max_length
if __name__ == '__main__':
    sol2=Solution2()
    string="abcabcbb"
    x=6
    print(sol2.longest_substring(string))
# Time Complexity - O(N)
# Space Complexity - O(N)