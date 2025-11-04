# Brute Force
class Solution1:
    def book_allocate(self, arr:list, N:int)->int:
        low=max(arr)
        high=sum(arr)
        for pages in range(low,high+1):
            studentCount=self.count_students(arr,pages)
            if studentCount==N:
                return pages
    def count_students(self, arr:list, pages:int)->int:
        student=1 # Initialize student
        student_pages=0 # Initialize page as 0
        for i in range(len(arr)):
            current_page=arr[i] # Take current page
            if student_pages+current_page<=pages: # Add with current page and check if sum of pages is <= target pages
                student_pages+=current_page # If so, sum up the pages
            else:
                student+=1 # Go to next student
                student_pages=current_page # Just give current page to student
        return student
            
if __name__ == '__main__':
    sol1=Solution1()
    arr=[25,46,28,49,24]
    N=4
    print(sol1.book_allocate(arr,N))
# Time Complexity - O((sum(arr)-max(arr))*N)
# Space Complexity - O(1)

# Optimal - Binary Search
class Solution2:
    def book_allocate(self, arr:list, N:int)->int:
        low=max(arr)
        high=sum(arr)
        while low<=high:
            mid=(low+high)//2
            studentCount=self.count_students(arr,mid)
            if studentCount>N:
                low=mid+1 # Increasing page limit for decreasing distribution
            else:
                high=mid-1 # Decreasing page limit for increasing distribution
        return low
    def count_students(self, arr:list, pages:int)->int:
        student=1 # Initialize student
        student_pages=0 # Initialize page as 0
        for i in range(len(arr)):
            current_page=arr[i] # Take current page
            if student_pages+current_page<=pages: # Add with current page and check if sum of pages is <= target pages
                student_pages+=current_page # If so, sum up the pages
            else:
                student+=1 # Go to next student
                student_pages=current_page # Just give current page to student
        return student
            
if __name__ == '__main__':
    sol2=Solution2()
    arr=[25,46,28,49,24]
    N=4
    print(sol2.book_allocate(arr,N))
# Time Complexity - O(log(sum(arr)-max(arr)*N)
# Space Complexity - O(1)