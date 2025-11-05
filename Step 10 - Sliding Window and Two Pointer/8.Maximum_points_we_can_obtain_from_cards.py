class Solution1:
    def maximum_points(self, arr:list, k:int)->int:
        left_sum,right_sum,total_sum = 0,0,0
        for i in range(k):
            left_sum+=arr[i]
        right_index=len(arr)-1
        for j in range(k-1,-1,-1): # why k-1 is because we are starting from 1 right value
            left_sum-=arr[j]
            right_sum+=arr[right_index]
            right_index-=1
            total_sum=max(total_sum,left_sum+right_sum)
        return total_sum
if __name__ == '__main__':
    sol1=Solution1()
    arr=[6,2,3,4,7,2,1,7,1]
    k=4
    print(sol1.maximum_points(arr,k))
# Time Complexity - O(i+j)
# Space Complexity - O(1)