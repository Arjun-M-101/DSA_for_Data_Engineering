class Solution:
    def upper_bound(self, arr:list, x:int)->int:
        N = len(arr)
        low=0
        high=N-1
        ans=N
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>x:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
if __name__ == '__main__':
    result=Solution()
    arr=[1,2,3,3,5,8,8,11,11,12]
    x=10
    print(result.upper_bound(arr,x))
# Time Complexity - O(logN)
# Space Complexity - O(1)