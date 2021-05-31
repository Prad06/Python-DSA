# Pradnyesh Choudhari
# Mon May 31 21:09:54 2021
# Lonely element in sorted array.
# Time Complexity O(log n) Space Complexity O(1).

def search(arr, i, j):
    mid = (i + j) // 2
    if arr[mid] != arr[mid+1] and arr[mid] != arr[mid-1]:
        return arr[mid]
    
    if arr[mid] == arr[mid-1]:
        if (mid-1)%2 == 0:
            return search(arr, mid+1, j)
        else:
            return search(arr, i, mid-1)
    elif arr[mid] == arr[mid+1]:
        if mid%2 == 0:
            return search(arr, mid+1, j)
        else:
            return search(arr, i, mid-1)


arr = list(map(int, input().split()))
ans = search(arr, 0, len(arr)-1)
print(ans)


