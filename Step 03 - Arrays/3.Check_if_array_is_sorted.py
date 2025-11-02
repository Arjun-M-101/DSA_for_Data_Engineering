def check_sorted(arr):
    for i in range(1,len(arr)):
        if arr[i]>=arr[i-1]:
            continue
        else:
            return False
    return True
arr=[4,0,6,1,3,7,2,5]
#arr.sort() # To toggle sort
print(check_sorted(arr))
# O(N)