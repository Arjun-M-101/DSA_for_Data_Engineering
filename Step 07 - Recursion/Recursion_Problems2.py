# Print sum of N numbers
# 2 Methods i) Parameterized & ii) Functional

# Parameterized-Recursion
# '''
n1=int(input())
sum1=0
def print_sum1(n1,sum1):
    if n1<0:
        return
    print(sum1)
    print_sum1(n1-1,sum1+n1)
print_sum1(n1,sum1)

# Functional-Recursion
n2=int(input())
def print_sum2(n2):
    if n2 == 0:
        return 0
    return n2 + print_sum2(n2-1)
print(print_sum2(n2))

# Factorial
n3 = int(input())
def factorial(n3):
    if n3 == 0:
        return 1
    return n3 * factorial(n3-1)
print(factorial(n3))
# Time Complexity - O(N)
# Space Complexity - O(N)
# '''