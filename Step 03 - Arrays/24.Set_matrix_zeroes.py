# Brute Force
def matrix_zero1(m1):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if m1[i][j]==0:
                mark_row(m1,i)
                mark_col(m1,j)
    for a in range(len(m1)):
        for b in range(len(m1[0])):
            if m1[a][b]==-1:
                m1[a][b]=0
    return m1
            
def mark_row(m1,i):
    for j in range(len(m1[0])):
        if m1[i][j]!=0:
            m1[i][j]=-1
def mark_col(m1,j):
    for i in range(len(m1)):
        if m1[i][j]!=0:
            m1[i][j]=-1
m1=[[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
print(m1)
print(matrix_zero1(m1))
# Time Complexity ~ O(N*M)*O(N*M)+O(N*M) ~ O(N^3)
# Space Complexity - O(1)

# Better
def matrix_zero2(m2):
    row=[0]*len(m2[0])
    col=[0]*len(m2)
    for i in range(len(m2)):
        for j in range(len(m2[0])):
            if m2[i][j]==0:
                row[i]=1
                col[j]=1
    for a in range(len(m2)):
        for b in range(len(m2[0])):
            if row[a]==1 or col[b]==1:
                m2[a][b]=0
    return m2
            
m2=[[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
print(m2)
print(matrix_zero2(m2))
# Time Complexity ~ O(2(N*M))
# Space Complexity - O(N+M)

# Optimal
