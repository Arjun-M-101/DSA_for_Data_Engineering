# Optimal
def spiral1(a1):
    top,left=0,0
    right=len(a1[0])-1
    bottom=len(a1)-1
    ans=[]
    while top<=bottom and left<=right:
        for a in range(left,right+1):
            ans.append(a1[top][a])
        top+=1
        for b in range(top,bottom+1):
            ans.append(a1[b][right])
        right-=1
        if top<=bottom:
            for c in range(right,left-1,-1):
                ans.append(a1[bottom][c])
            bottom-=1
        if left<=right:
            for d in range(bottom,top-1,-1):
                ans.append(a1[d][left])
            left+=1
    return ans
a1=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
print(spiral1(a1))
# Time Complexity - O(N*M)
# Space Complexity - O(N*M)