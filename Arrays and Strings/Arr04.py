# Pradnyesh Choudhari
# Sat May 29 18:52:31 2021
# Sunny Buildings.
# Time Complexity O(n * m) Space Complexity O(1).


for i in range(int(input())):
    arr = list(map(int, input().split()))
    maxh = arr[0]
    count = 1
    for i in range(len(arr)):
        if arr[i] >= maxh:
            maxh = arr[i]
            count += 1
    print(count)
    



