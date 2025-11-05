# Brute Force
class Solution1:
    def max_consecutive_ones(self, arr:list, k:int)->int:
        max_length=float('-inf')
        for i in range(len(arr)):
            zeroes=0
            for j in range(i,len(arr)):
                if arr[j]==0:
                    zeroes+=1
                if zeroes<=k:
                    length=j-i+1
                    max_length=max(max_length,length)
                else:
                    break
        return max_length
if __name__ == '__main__':
    sol1=Solution1()
    arr=[1,1,1,0,0,0,1,1,1,1,0]
    k=2
    print(sol1.max_consecutive_ones(arr,k))
# Time Complexity - O(i*j) ~ O(N^2)
# Space Complexity - O(1)

# Optimal
class Solution2:
    def max_consecutive_ones(self, arr:list, k:int)->int:
        left,right,zeroes,max_length,N=0,0,0,float('-inf'),len(arr)
        while right<N:
            if arr[right]==0:
                zeroes+=1
            if zeroes>k: # If zero exceeds
                if arr[left]==0: # And if left is still 0
                    zeroes-=1 # Reduce zero
                left+=1 # And move left to right until its not zero
            if zeroes<=k: # Once zero is within k range
                length=right-left+1
                max_length=max(max_length,length)
            right+=1
        return max_length
if __name__ == '__main__':
    sol2=Solution2()
    arr=[1,1,1,0,0,0,1,1,1,1,0]
    k=2
    print(sol2.max_consecutive_ones(arr,k))
# Time Complexity - O(N)
# Space Complexity - O(1)