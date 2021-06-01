# Pradnyesh Choudhari
# Tue Jun  1 00:57:53 2021
# Binary Search on rotated array.
# Time Complexity O(log n) Space Complexity O(1).

def func(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > arr[n-1]:
            if arr[mid] < target or target < arr[0]:
                start = mid+1
            else:
                end = mid-1
        else:
            if arr[mid] > target or target > arr[n-1]:
                end = mid-1
            else:
                start = mid+1
    return -1

arr = list(map(int, input().split()))
n = len(arr)
target = int(input())
print(func(arr, 0, n-1, target))


