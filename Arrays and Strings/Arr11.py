# Pradnyesh Choudhari
# Mon May 31 17:23:27 2021
# Largest Possible Number.
# Time Complexity O(n^2) Space Complexity O(1).


def compare(a, b):
    return a + b >= b + a

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if compare(arr[j], arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = list(map(str, input().split()))
bubble_sort(arr)
print(*arr[::-1])