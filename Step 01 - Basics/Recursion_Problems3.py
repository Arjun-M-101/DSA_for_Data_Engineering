# Reverse array - Normal for method
# '''
array1 = list(map(int, input().split()))
print(array1)
left = 0
right = len(array1)-1
for i in range(len(array1)//2):
    if left<=right:
        array1[left],array1[right]=array1[right],array1[left]
        left+=1
        right-=1
print(array1)

# Reverse array - Two pointers with recursion
array2 = list(map(int, input().split()))
print(array2)
left2 = 0
right2 = len(array2)-1
def reverse_array2(left2,right2,array2):
    if left2>=right2:
        return array2
    array2[left2],array2[right2]=array2[right2],array2[left2]
    return reverse_array2(left2+1,right2-1,array2)
print(reverse_array2(left2,right2,array2))

# Reverse array - 1 pointer
array3 = list(map(int, input().split()))
print(array3)
left3 = 0
def reverse_array3(left3,array3):
    if left3>=len(array3)//2:
        return array3
    array3[left3],array3[len(array3)-1-left3]=array3[len(array3)-1-left3],array3[left3]
    return reverse_array3(left3+1,array3)
print(reverse_array3(left3,array3))
# '''

# Palindrome Check - TYPE 1
string1 = list(input())
i=0
def reverse_string1(string1,i):
    if i>=len(string1)//2:
        return True
    if string1[i] != string1[len(string1)-1-i]:
        return False
    return reverse_string1(string1,i+1)
print(reverse_string1(string1,i))
# Time complexity = O(N)
# Space complexity = O(N)

# Show if Palindrome or not (Checking after reversing fully) - TYP# 2
string_backup = input()
print(string_backup)
string2 = list(string_backup)
j=0
def reverse_string2(string2,j):
    if j>=len(string2)//2:
        return string2
    string2[j],string2[len(string2)-1-j]=string2[len(string2)-1-j],string2[j]
    return reverse_string2(string2,j+1)
string_reverse = reverse_string2(string2,j)
string_reverse="".join(string_reverse)
if string_backup==string_reverse:
    print(f"{string_reverse} is palindrome")
else:
    print(f"{string_reverse} is not palindrome")
# Time complexity = O(N)
# Space complexity = O(N)

# Show if Palindrome or not (Returning false immediately if found as not palindrome) - TYPE 3
string_backup2 = input()
print(string_backup2)
string3 = list(string_backup2)
j=0
def reverse_string3(string3,j):
    if j>=len(string3)//2:
        return string3
    if string3[j] == string3[len(string3)-1-j]:
        string3[j],string3[len(string3)-1-j]=string3[len(string3)-1-j],string3[j]
        return reverse_string3(string3,j+1)
    else:
        return False
result = reverse_string3(string3,j)
if result!=False:  
    string_reverse="".join(result)
    print(f"{string_reverse} is palindrome")
else:
    print("Not a palindrome")
# Time complexity = O(N)
# Space complexity = O(N)