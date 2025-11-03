class Solution:
    def floor_and_ceil(self, arr:list, x:int)->int:
        N = len(arr)
        low=0
        high=N-1
        floor,ceil=-1,-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]<=x:
                floor=arr[mid]
                low=mid+1
            elif arr[mid]>=x:
                ceil=arr[mid]
                high=mid-1
        return floor,ceil
if __name__ == '__main__':
    result=Solution()
    arr=[10,20,30,40,50]
    x=25
    print(result.floor_and_ceil(arr,x))
# Time Complexity - O(logN)
# Space Complexity - O(1)