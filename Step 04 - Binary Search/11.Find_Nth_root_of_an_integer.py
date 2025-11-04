# Brute Force
class Solution1:
    def root1(self, num:int, x:int)->int:
        for i in range(1,num+1):
            power = self.power(i,x)
            if power == num:
                return i
            elif power > num:
                break
        return -1
    def power(self, base:int, exp:int)->int:
        result = 1
        for _ in range(exp):
            result *= base
        return result
if __name__ == '__main__':
    sol1=Solution1()
    num=27
    x=3
    print(sol1.root1(num,x))
# Time Complexity - O(N*X) - with log function it will be O(N*logX)
# Space Complexity - O(1)

# Optimal - Binary Search
class Solution2:
    def root2(self, num:int, x:int)->int:
        low=1
        high=num
        while low<=high:
            mid=(low+high)//2
            power=self.power(mid,x)
            if power==num:
                return mid
            elif power<num:
                low=mid+1
            else:
                high=mid-1
        return -1
    def power(self, base:int, exp:int)->int:
        result = 1
        for _ in range(exp):
            result *= base
        return result
if __name__ == '__main__':
    sol2=Solution2()
    num=27
    x=3
    print(sol2.root2(num,x))
# Time Complexity - O(logN*logX)
# Space Complexity - O(1)