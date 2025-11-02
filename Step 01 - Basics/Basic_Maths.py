# Digit Extraction
# '''
n1=int(input())
while n1>0:
    remainder=n1%10
    print(remainder)
    n1=n1//10
    
# How many digits?
n2=int(input())
cnt=0
while n2>0:
    cnt+=1
    n2=n2//10
print(cnt)

# Also

from math import log10
n3=int(input())
cnt2=int(log10(n3))+1
print(cnt2)

# Time complexity is O(logN) for division operation
# Here O(log10N) because we're dividing for 10

# Reverse Number
n4=int(input())
reverse_num=0
while n4>0:
    last_digit=n4%10
    reverse_num=reverse_num*10+last_digit
    n4=n4//10
print(reverse_num)

# Palindrome Number
n5=int(input())
backup_num1=n5
reverse_num=0
while n5>0:
    last_digit=n5%10
    reverse_num=reverse_num*10+last_digit
    n5=n5//10
if backup_num1==reverse_num:
    print("Palindrome")
else:
    print("Not a palindrome")

# Armstrong Number
from math import log10
n6=int(input())
length=(int(log10(n6))+1) # or len(str(n6))
arm_sum=0
backup_num2=n6
while n6>0:
    digits=n6%10
    arm_sum=arm_sum+digits**length
    n6=n6//10
if arm_sum==backup_num2:
    print("Armstrong")
else:
    print("Not armstrong")

# Print all divisors
n7=int(input())
for i in range(1,n7+1):
    if n7%i==0:
        print(i)
# Time Complexity = O(N)
# This can be reduced

# Using sqrt & multiples & divisor method
from math import sqrt
n8=int(input())
list1=[]
for i in range(1,int(sqrt(n8))+1):
    if n8%i==0:
        list1.append(i)
        if n8//i!=i: # To avoid repeated divisors
            list1.append(n8//i)
# Time Complexity = O(sqrt(N))
list1.sort()
# Time Complexity = O(NlogN)
print(list1)
# Time Complexity = O(sqrt(N)) + O(NlogN)

# Without using sqrt. Only multiples & divisors method
n9=int(input())
list1=[]
for i in range(1,int(n9**0.5)+1):
    if n9%i==0:
        list1.append(i)
        if n9//i!=i: # To avoid repeated divisors
            list1.append(n9//i)
# Time Complexity = O(sqrt(N))
list1.sort()
# Time Complexity = O(NlogN)
print(list1)
# Time Complexity = O(sqrt(N)) + O(NlogN)

# Prime Number
# Brute Force (Extreme)
n10=int(input())
cnt3=0
for i in range(1,n10+1):
    if n10%i==0:
        cnt3+=1
if cnt3==2:
    print("Prime")
else:
    print("Not prime")
# Time Complexity = O(N)

# Brute Force (Optimized)
n11=int(input())
cnt4=0
for i in range(1,int(n11**0.5)+1):
    if n11%i==0:
        cnt4+=1
        if n11//i!=i:
            cnt4+=1
if cnt4==2:
    print("Prime")
else:
    print("Not prime")
# Time Complexity = O(sqrt(N))

# GCD & HCF
n12, n13 =map(int,input().split())
for i in range(1,min(n12,n13)+1):
    if n12%i==0 and n13%i==0:
        gcd = i
        print(i)
print(gcd)
# Time Complexity = O(min(a,b))

n14, n15 =map(int,input().split())
for i in range(min(n14,n15),0,-1):
    if n14%i==0 and n15%i==0:
        gcd = i
        print(i)
        break
print(gcd)
# Time Complexity = O(min(a,b)) (Still same)

# Euclidean ALgorithm
n16, n17 = map(int,input().split())
while n16 > 0 and n17 > 0:
    if n16 > n17:
        n16 = n16%n17
        print(n16)
    else:
        n17 = n17%n16
        print(n17)
if n16 == 0:
    gcd = n17
else:
    gcd = n16
print(gcd)
# Time Complexity = O(log((phi)(min(a,b)))))
# phi? number keeps changing

# LCM & GCD
n18, n19 = map(int, input().split())
backup_n18 = n18
backup_n19 = n19
while n18 > 0 and n19 > 0:
    if n18 > n19:
        n18 = n18%n19
    else:
        n19 = n19%n18
if n18 == 0:
    gcd = n19
else:
    gcd = n18
lcm = (backup_n18*backup_n19)//gcd
print(f"gcd is: {gcd}. lcm is {lcm}.")
# Time Complexity = O(log((phi)(min(a,b)))))
# '''