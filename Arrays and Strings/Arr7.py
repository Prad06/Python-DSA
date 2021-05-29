# Pradnyesh Choudhari
# Sat May 29 21:47:09 2021
# Move Zeros to the end.
# Time Complexity O(n) Space Complexity O(1).

arr = list(map(int, input().split()))
n = len(arr)
idx = 0

for i in range(n):
    if arr[i] != 0:
        arr[i], arr[idx] = arr[idx], arr[i]
        idx += 1
        
print(*arr)

    




