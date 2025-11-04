class Solution1:
    def first_and_last1(self, arr:list, target:int)->int:
        first,last=-1,-1
        for i in range(len(arr)):
            if arr[i]==target:
                if first==-1:
                    first=i
                last=i
        return first,last
if __name__ == '__main__':
    result=Solution1()
    arr=[2,4,6,8,8,8,11,13]
    target=8
    print(result.first_and_last1(arr,target))
# Time Complexity - O(N)
# Space Complexity - O(1)

class Solution2:
    def lower_bound(self, arr:list, target:int)->int:
        N = len(arr)
        low=0
        high=N-1
        ans=N
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def upper_bound(self, arr:list, target:int)->int:
        N = len(arr)
        low=0
        high=N-1
        ans=N
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def first_and_last2(self, arr:list, target:int)->int:
        lowerbd=self.lower_bound(arr,target)
        if lowerbd==len(arr) or arr[lowerbd]!=target: # To modify the usual behaviour of lowerbound
            return -1,-1
        return lowerbd,self.upper_bound(arr,target)-1
if __name__ == '__main__':
    result=Solution2()
    arr=[2,4,6,8,8,8,11,13]
    target=8
    print(result.first_and_last2(arr,target))
# Time Complexity - O(2logN)
# Space Complexity - O(1)

# Direct apprach - Binary Search
class Solution3:
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
    def first_and_last3(self, arr:list, target:int)->int:
        if self.first(arr,target)==-1:
            return -1,-1
        return self.first(arr,target),self.last(arr,target)
if __name__ == '__main__':
    result=Solution3()
    arr=[2,4,6,8,8,8,11,13]
    target=8
    print(result.first_and_last3(arr,target))
# Time Complexity - O(2logN)
# Space Complexity - O(1)