
class Solution:
    # Iterative
    def binary_search1(self, arr1:list, target1:int)->int:
        N = len(arr1)
        low=0
        high=N-1
        while low<=high:
            mid=(low+high)//2
            if arr1[mid]==target1:
                return mid
            elif target1>arr1[mid]:
                low=mid+1
            else:
                high=mid-1
        return -1
    # Recursive
    def binary_search2(self, arr2:list, low2:int, high2:int, target2:int)->int:
        if low2>high2:
            return -1
        mid2=(low2+high2)//2
        if arr2[mid2]==target2:
            return mid2
        elif target2>arr2[mid2]:
            return self.binary_search2(arr2,mid2+1,high2,target2)
        else:
            return self.binary_search2(arr2,low2,mid2-1,target2)
if __name__ == '__main__':
    result=Solution()
    arr1=[3,4,6,7,9,12,16,17]
    arr2=[3,4,6,7,9,12,16,17]
    target1=6
    target2=9
    low2=0
    high2=len(arr2)-1
    print(result.binary_search1(arr1,target1))
    print(result.binary_search2(arr2,low2,high2,target2))
# Time Complexity - O(log(2)N)
# Space Complexity - O(1) for iterative, O(log2N) for recursive