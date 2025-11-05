# Brute Force
class Solution1:
    def no_of_substrings_3_char(self, string:str)->int:
        count=0
        for i in range(len(string)):
            hash_array=[0]*256
            for j in range(i,len(string)):
                hash_array[ord(string[j])-ord('a')]=1
                if hash_array[0]+hash_array[1]+hash_array[2]==3:
                    count+=1
        return count
if __name__ == '__main__':
    sol1=Solution1()
    string="bbacba"
    print(sol1.no_of_substrings_3_char(string))
# Time Complexity - O(i*j)
# Space Complexity - O(256)

# Better
class Solution2:
    def no_of_substrings_3_char(self, string:str)->int:
        count=0
        for i in range(len(string)):
            hash_array=[0]*256
            for j in range(i,len(string)):
                hash_array[ord(string[j])-ord('a')]=1
                if hash_array[0]+hash_array[1]+hash_array[2]==3:
                    count+=len(string)-j # Because once if its valid, It will be valid throughout the string
                    break
        return count
if __name__ == '__main__':
    sol2=Solution2()
    string="bbacba"
    print(sol2.no_of_substrings_3_char(string))
# Time Complexity - O(i*j)
# Space Complexity - O(256)

# Optimal
class Solution3:
    def no_of_substrings_3_char(self, string: str) -> int:
        freq = [0, 0, 0] # counts of 'a', 'b', 'c'
        left, right = 0, 0
        count = 0
        while right < len(string):
            freq[ord(string[right]) - ord('a')] += 1 # add character at 'right'
            # shrink window while it contains all three chars
            while freq[0] > 0 and freq[1] > 0 and freq[2] > 0:
                count += len(string) - right # add count of valid substrings
                freq[ord(string[left]) - ord('a')] -= 1 # remove char at 'left'
                left += 1 # shrink from left
            right += 1 # expand from right
        return count
# Driver code
if __name__ == "__main__":
    sol3 = Solution3()
    string = "bbacba"
    print(sol3.no_of_substrings_3_char(string))