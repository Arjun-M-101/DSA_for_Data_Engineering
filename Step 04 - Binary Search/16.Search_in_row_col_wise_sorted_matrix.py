# Brute Force
class Solution1:
    def search_matrix(self, matrix:list, target:int)->int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==target:
                    return i,j
        return -1
if __name__ == '__main__':
    sol1=Solution1()
    matrix = [
    [1,  4,  7, 11, 15],
    [2,  5,  8, 12, 19],
    [3,  6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
    ]
    target=14
    print(sol1.search_matrix(matrix,target))
# Time Complexity - O(i*j)
# Space Complexity - O(1)

# Better
class Solution2:
    def search_matrix(self, matrix:list, target:int)->int:
        for i in range(len(matrix)):
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
    matrix = [
    [1,  4,  7, 11, 15],
    [2,  5,  8, 12, 19],
    [3,  6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
    ]
    target=14
    print(sol2.search_matrix(matrix,target))
# Time Complexity - O(i*logj)
# Space Complexity - O(1)

# Optimal - Staircase - Traverse between the increasing row & col
# row = 0, col = m-1
class Solution3:
    def search_matrix(self, matrix:list, target:int)->int:
        n,m=len(matrix),len(matrix[0])
        row,col=0,n*m-1
        while row<n and col>=0:
            if matrix[row][col]==target:
                return row,col
            elif matrix[row][col]<target:
                row+=1
            else:
                col-=1
        return -1,-1
if __name__ == '__main__':
    sol3=Solution3()
    matrix = [
    [1,  4,  7, 11, 15],
    [2,  5,  8, 12, 19],
    [3,  6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
    ]
    target=14
    print(sol2.search_matrix(matrix,target))
# Time Complexity - O(log(n+m))
# Space Complexity - O(1)