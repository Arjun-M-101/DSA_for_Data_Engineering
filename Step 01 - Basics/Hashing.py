# HASHING - VERY VERY IMPORTANT
# Hashing is pre-storing & fetching

# Without hashing
# '''
list1 = [1,2,3,2,1,3,2,1,1,2]
num0=int(input())
cnt=0
for i in range(len(list1)):
    if num0 == list1[i]:
        cnt+=1
print(f"The number {num0} appears for {cnt} times")


# Number Hashing
array1 = list(map(int, input().split()))

# Assuming 12 is at max for the array
hash_array1 = [0]*13

# Pre-storing
for num in array1:
    hash_array1[num]+=1

n=(int(input("How many numbers you want to query? ")))
while n:
    number = int(input())
    # Fetching
    print(f"The number {number} appears for {hash_array1[number]} times")
    n-=1
    
# What if array has maximum of 10^9 size or larger size?
# Can we create hash array of size 10^9+1 like we did for above 13 for 12 elements? No!
# We cannot create array with larger size greater that 10^6 integer inside main.
# But it can be declared globally till 10^8.

# Character Hashing
# Small alphabets
array2 = input().split()

# Pre-storing for alphabets
hash_alpha=[0]*26

for alphabet in array2:
    hash_alpha[ord(alphabet)-ord('a')]+=1

n2=(int(input("How many alphabets you want to query? ")))
while n2:
    alp = input()
    # Fetching
    print(f"The alphabet {alp} appears for {hash_alpha[ord(alp)-ord('a')]} times")
    n2-=1
    
# All characters
array3 = input().split()

# Pre-storing for alphabets
hash_alpha2=[0]*256

for alphabet2 in array3:
    hash_alpha2[ord(alphabet2)]+=1

n3=(int(input("How many alphabets you want to query? ")))
while n3:
    alp2 = input()
    # Fetching
    print(f"The alphabet {alp2} appears for {hash_alpha2[ord(alp2)]} times")
    n3-=1
# For character hashing, we don't have range issue like we had for integers (10^8), because its max is 256.

# Number Hashing with HashMap - Continuation
array4 = list(map(int, input().split()))

# HashMap
hashdict1 = {}

# Pre-storing
for num2 in array4:
    hashdict1[num2]=hashdict1.get(num2,0)+1

n4=(int(input("How many numbers you want to query? ")))
while n4:
    number2 = int(input())
    # Fetching
    print(f"The number {number2} appears for {hashdict1.get(number2,0)} times")
    n4-=1
# Time Complexity - O(2N)
# Note: Dict stores data in order

# Character Hashing with HashMap - Continuation
array5 = input().split()

# HashMap
hashdict2 = {}

# Pre-storing
for alphabet2 in array5:
    hashdict2[alphabet2]=hashdict2.get(alphabet2,0)+1

n5=(int(input("How many alphabets you want to query? ")))
while n5:
    alpha2 = input()
    # Fetching
    print(f"The alphabet {alpha2} appears for {hashdict2.get(alpha2,0)} times")
    n5-=1
    
# Find the highest and lowest frequency element
array6 = list(map(int, input().split()))

# Assuming 12 is at max for the array
hash_array2 = [0]*13

# Pre-storing
for num3 in array6:
    hash_array2[num3]+=1

n=(int(input("How many numbers you want to query? ")))
while n:
    number3 = int(input())
    # Fetching
    print(f"The number {number3} appears for {hash_array2[number3]} times")
    n-=1
# Find highest and lowest frequency element
max_freq = 0
min_freq = float('inf')
max_elem = None
min_elem = None

for i, freq in enumerate(hash_array2):
    if freq > 0:  # only consider elements that actually appeared
        if freq > max_freq:
            max_freq = freq
            max_elem = i
        if freq < min_freq:
            min_freq = freq
            min_elem = i

print(f"Highest frequency element: {max_elem} appears {max_freq} times")
print(f"Lowest frequency element: {min_elem} appears {min_freq} times")
# '''