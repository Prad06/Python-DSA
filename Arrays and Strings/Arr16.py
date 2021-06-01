# Pradnyesh Choudhari
# Tue Jun  1 01:05:44 2021
# Sorting in linear time. Dutch National Flag Problem.
# Time Complexity O(n) Space Complexity O(1).

def solve(arr):
    low = 0
    mid = 0
    high = len(arr)-1
    
    while mid<=high:
        curr = arr[mid]
        if curr == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        if curr == 1:
            mid += 1
        if curr == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
    
arr = list(map(int, input().split()))
print(solve(arr))


