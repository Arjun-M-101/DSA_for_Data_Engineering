# Brute Force
class Solution1:
    def fruit_basket(self, fruit_type:list, basket_limit:int)->int:
        max_length=float('-inf')
        for i in range(len(fruit_type)):
            basket=set()
            for j in range(i,len(fruit_type)):
                basket.add(fruit_type[j])
                if len(basket)<=2:
                    max_length=max(max_length,j-i+1)
                else:
                    break
        return max_length
if __name__ == '__main__':
    sol1=Solution1()
    fruit_type=[3,3,3,1,2,1,1,2,3,3,4]
    basket_limit=2
    print(sol1.fruit_basket(fruit_type,basket_limit))
# Time Complexity - O(i*j) ~ O(N^2)
# Space Complexity - O(3)

# Optimal
class Solution2:
    def fruit_basket(self, fruit_type:list, basket_limit:int)->int:
        left,right,N,max_length=0,0,len(fruit_type),float('-inf')
        hash_dict={}
        while right<N: # Move right till end
            # Add current fruit type and update count in hash_dict
            hash_dict[fruit_type[right]]=hash_dict.get(fruit_type[right],0)+1
            if len(hash_dict)>basket_limit: # If size exceeds
                hash_dict[fruit_type[left]]-=1 # Shrink window from left
                if hash_dict[fruit_type[left]]==0:
                    del hash_dict[fruit_type[left]] # Remove the fruit_type once its count becomes zero
                left+=1 # Move the left to the next identical fruit_type
            if len(hash_dict)<=basket_limit:
                max_length=max(max_length,right-left+1)
            right+=1
        return max_length
if __name__ == '__main__':
    sol2=Solution2()
    fruit_type=[3,3,3,1,2,1,1,2,3,3,4]
    basket_limit=2
    print(sol2.fruit_basket(fruit_type,basket_limit))
# Time Complexity - O(N)
# Space Complexity - O(3)