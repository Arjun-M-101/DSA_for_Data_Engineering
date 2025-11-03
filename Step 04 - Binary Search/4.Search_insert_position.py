# Uses lower bound logic
class Solution:
    def search_insert_position(self, arr:list, x:int)->int:
        N = len(arr)
        low=0
        high=N-1
        ans=N
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>=x:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
if __name__ == '__main__':
    result=Solution()
    arr=[1,2,4,7]
    x=6
    print(result.search_insert_position(arr,x))
# Time Complexity - O(logN)
# Space Complexity - O(1)