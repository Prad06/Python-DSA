# Pradnyesh Choudhari
# Sat May 29 16:21:14 2021
# Container containg max water.
# 2 Pointer approach.
# Time Complexity O(n) Space Complexity O(1).

def func(arr, n):
    left = 0
    right = n-1
    maxWater = 0
    
    while left < right:
        water = min(arr[left], arr[right]) * (right - left)
        maxWater = max(maxWater, water)
        if arr[left] >= right:
            right -= 1
        else:
            left += 1
            
    return maxWater

n = int(input())
arr = list(map(int, input().split()))
ans = func(arr, n)
print(ans)

