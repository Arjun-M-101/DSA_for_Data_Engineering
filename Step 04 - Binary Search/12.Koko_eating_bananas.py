# Brute Force
class Solution1:
    def banana(self, arr:list, hour:int)->int:
        for i in range(1,max(arr)+1):
            time_required=self.eat(arr,i)
            if time_required<=hour:
                return i
        return -1
    def eat(self, arr:list, speed:int)->int:
        totalhrs=0
        for i in range(len(arr)):
            totalhrs += (arr[i]+speed-1)//speed # ceil
        return totalhrs
if __name__ == '__main__':
    sol1=Solution1()
    arr=[3,6,7,11]
    hour=8
    print(sol1.banana(arr,hour))
# Time Complexity - O(N*max(arr))
# Space Complexity - O(1)

# Optimal - Binary Search
class Solution2:
    def banana(self, arr:list, hour:int)->int:
        low=1
        high=max(arr)
        ans=high
        while low<=high:
            mid=(low+high)//2
            totalhrs=self.eat(arr,mid)
            if totalhrs<=hour:
                ans=mid
                high=mid-1 # opposite polarity
            else:
                low=mid+1 # opposite polarity
        return ans
    def eat(self, arr:list, speed:int)->int:
        totalhrs=0
        for i in range(len(arr)):
            totalhrs += (arr[i]+speed-1)//speed # ceil
        return totalhrs
if __name__ == '__main__':
    sol2=Solution2()
    arr=[3,6,7,11]
    hour=8
    print(sol2.banana(arr,hour))
# Time Complexity - O(N*logmax(arr))
# Space Complexity - O(1)