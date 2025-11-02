# RECURSION PROBLEMS WITH MULTIPLE FUNCTION CALLS
# Fibonacci
n1=int(input())
a,b = 0,1
for i in range(0,n1):
    print(a, end=' ')
    a,b=b,a+b
print('')
# Time Complexity - O(N)
# Space Complexity - O(1)

# Fibonacci using list
n2 = int(input())
if n2 == 0:
    list1 = []
elif n2 == 1:
    list1 = [0]
else:
    list1 = [0, 1]
    for i in range(2, n2):
        list1.append(list1[i-2] + list1[i-1])
print(list1)
# Time Complexity - O(N)
# Space Complexity - O(1)

# Fibonacci using recursion
def fibonacci1(n3):
    if n3<=1:
        return n3
    return fibonacci1(n3-2)+fibonacci1(n3-1)
n3=int(input())
print(fibonacci1(n3))
# Time Complexity ~ O(2^N)
# Space Complexity - O(1)

# Fibonacci series using recursion
def fibonacci2(n4,a,b):
    if n4==0:
        return
    print(a, end=' ')
    fibonacci2(n4-1,b,a+b)
n4=int(input())
a,b=0,1
fibonacci2(n4,a,b)
# Time Complexity - O(N)
# Space Complexity - O(1)