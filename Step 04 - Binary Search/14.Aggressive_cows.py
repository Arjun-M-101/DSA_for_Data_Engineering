# Brute Force
class Solution1:
    def cows(self, stalls:list, cows:int)->int:
        stalls.sort()
        mini=stalls[0]
        maxi=stalls[-1]
        for gap in range(maxi-mini+1):
            if self.can_we_place(stalls,gap,cows)==True:
                continue
            else:
                return gap-1
    def can_we_place(self, stalls:list, gap:int, cows:int)->bool:
        cow_count=1
        last_be=stalls[0]
        for i in range(1,len(stalls)):
            if stalls[i]-last_be>=gap:
                cow_count+=1
                last_be=stalls[i]
        if cow_count>=cows:
            return True
        else:
            return False
if __name__ == '__main__':
    sol1=Solution1()
    stalls=[0,3,4,7,10,9]
    cows=4
    print(sol1.cows(stalls,cows))
# Time Complexity - O((max(stalls)-min(stalls))*N)
# Space Complexity - O(1)

# Optimal
class Solution2:
    def cows(self, stalls:list, cows:int)->int:
        stalls.sort()
        low=0
        high=stalls[-1]-stalls[0]
        ans=-1
        while low<=high:
            mid=(low+high)//2
            possibility=self.can_we_place(stalls,mid,cows)
            if possibility is True:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
    def can_we_place(self, stalls:list, gap:int, cows:int)->bool:
        cow_count=1
        last_be=stalls[0]
        for i in range(1,len(stalls)):
            if stalls[i]-last_be>=gap:
                cow_count+=1
                last_be=stalls[i]
        if cow_count>=cows:
            return True
        else:
            return False
if __name__ == '__main__':
    sol2=Solution2()
    stalls=[0,3,4,7,10,9]
    cows=4
    print(sol2.cows(stalls,cows))
# Time Complexity - O(NlogN+log(max-min)*N)
# Space Complexity - O(1)