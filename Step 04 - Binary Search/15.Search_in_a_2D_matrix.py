# Brute Force
class Solution1:
    def search_matrix(self, matrix:list, target:int)->int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==target:
                    return i,j
        return -1,-1
if __name__ == '__main__':
    sol1=Solution1()
    matrix=[[3,4,7,9],[12,13,16,18],[20,21,23,29]]
    target=23
    print(sol1.search_matrix(matrix,target))
# Time Complexity - O(i*j)
# Space Complexity - O(1)

# Better
class Solution2:
    def search_matrix(self, matrix:list, target:int)->int:
        for i in range(len(matrix)):
            if matrix[i][0] <= target and target <= matrix[i][len(matrix[0])-1]:
                col=self.binary_search(matrix[i],target)
                if col!=-1:
                    return i,col
        return -1,-1
    def binary_search(self, matrix:list, target:int)->int:
        N = len(matrix)
        low=0
        high=N-1
        while low<=high:
            mid=(low+high)//2
            if matrix[mid]==target:
                return mid
            elif target>matrix[mid]:
                low=mid+1
            else:
                high=mid-1
        return -1
if __name__ == '__main__':
    sol2=Solution2()
    matrix=[[3,4,7,9],[12,13,16,18],[20,21,23,29]]
    target=23
    print(sol2.search_matrix(matrix,target))
# Time Complexity - O(i*logj)
# Space Complexity - O(1)

# Optimal - 2D -> 1D
# Formula: row - mid/m, col - mid%m
class Solution3:
    def search_matrix(self, matrix:list, target:int)->int:
        n,m=len(matrix),len(matrix[0])
        low,high=0,n*m-1
        while low<=high:
            mid=(low+high)//2
            row,col=mid//m,mid%m
            if matrix[row][col]==target:
                return row,col
            elif matrix[row][col]<target:
                low=mid+1
            else:
                high=mid-1
        return -1,-1
if __name__ == '__main__':
    sol3=Solution3()
    matrix=[[3,4,7,9],[12,13,16,18],[20,21,23,29]]
    target=23
    print(sol2.search_matrix(matrix,target))
# Time Complexity - O(log(n*m))
# Space Complexity - O(1)