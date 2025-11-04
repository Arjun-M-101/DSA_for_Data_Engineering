class Solution1:
    def first(self, arr:list, target:int)->int:
        N = len(arr)
        low=0
        high=N-1
        first=-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
                first=mid
                high=mid-1
            elif arr[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return first
    def last(self, arr:list, target:int)->int:
        N = len(arr)
        low=0
        high=N-1
        last=-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
                last=mid
                low=mid+1
            elif arr[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return last
    def count(self, arr:list, target:int)->int:
        if self.first(arr,target)==-1:
            return -1,-1
        first = self.first(arr,target)
        last = self.last(arr,target)
        return last-first+1
if __name__ == '__main__':
    result=Solution1()
    arr=[2,4,6,8,8,8,11,13]
    target=8
    print(result.count(arr,target))
# Time Complexity - O(2logN)
# Space Complexity - O(1)