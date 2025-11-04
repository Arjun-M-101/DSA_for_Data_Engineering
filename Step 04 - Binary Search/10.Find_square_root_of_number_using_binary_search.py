class Solution1:
    def sqrt1(self, num: int)->int:
        low=0
        high=num
        while low<=high:
            mid=(low+high)//2
            if mid*mid<=num:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
if __name__ == '__main__':
    sol1=Solution1()
    num=28
    print(sol1.sqrt1(num))
# Time Complexity - O(logN)
# Space Complexity - O(1)