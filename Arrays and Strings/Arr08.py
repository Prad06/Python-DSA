# Pradnyesh Choudhari
# Sun May 30 00:40:02 2021
# Maximum sum of contigous subarray.
# Kadanes' Algorithm
# Time Complexity O(n) Space Complexity O(1).


def func(arr):
    msf = arr[0]   # msf --> Max so far
    mum = 0        # mum --> Max untill now
    start = 0
    end = 0
    s = 0
    
    for i in range(len(arr)):
        mum += arr[i]
        if mum > msf:
            msf = mum
            start = s
            end = i
        if mum < 0:
            mum = 0
            s = i + 1
            
    return msf, start, end

n = int(input())
arr = list(map(int, input().split()))
ans, start, end = func(arr)
print(ans)
for i in range(start, end+1):
    print(arr[i], end = " ")

