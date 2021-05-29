# Pradnyesh Choudhari
# Sat May 29 15:18:01 2021
# Unique string Problem by concatenating of subsequences.
# Recursive approach
# Time Complexity O(2^n) Space Complexity O(n * 2^n)

import sys

def func(arr, i, s):
    if i == len(arr):
        if len(s) > 26:
            return 0
        freq = set()
        for i in s:
            if i not in freq:
                freq.add(i)
            else:
                return 0
        return len(s)
    
    op1 = -sys.maxsize - 1
    op2 = -sys.maxsize - 1

    if len(s + arr[i]) <= 26:
        op1 = func(arr, i+1, s+arr[i])
        
    op2 = func(arr, i+1, s)
    
    return max(op1, op2)

def uniqueChar(arr):
    s = ""
    return func(arr, 0, s)

n = int(input())
arr = []
for i in range(n):
    arr.append(input())
ans = uniqueChar(arr)    
print(ans)
