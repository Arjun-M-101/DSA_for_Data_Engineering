# RECURSION - BASICS
# Time Complexity = O(N)
# Print name
# Change of parameters
# '''
i = 0
name, number = input().split()
number=int(number)
def print_name(i,n,name):
    if i>=n: # Base condition
        return
    print(name) # Work
    print_name(i+1,n,name) # Recursive call with updated parameter

print_name(i,number,name)

# Print numbers
j = 1
number2 = int(input())
def print_numbers1(j,number2):
    if j>number2:
        return
    print(j)
    print_numbers1(j+1,number2)
print_numbers1(j,number2)

# Print numbers (Reverse)
k = int(input())
def print_numbers2(k):
    if k<=0:
        return
    print(k)
    print_numbers2(k-1)
print_numbers2(k)

# Back-Tracking
# Print numbers linearly (without using +)
a = int(input())
def print_numbers3(a):
    if a<=0:
        return
    print_numbers3(a-1)
    print(a)
print_numbers3(a)
# Print numbers in reverse (without using -)
b = 1
c = int(input())
def print_numbers4(b,c):
    if b>c:
        return
    print_numbers4(b+1,c)
    print(b)
print_numbers4(b,c)
# '''