# Pradnyesh Choudhari
# Thu Jun  3 02:26:58 2021
# Print Zero sum subarrays.
# Time Complexity O(n) Space Complexity O(1).
from itertools import combinations

def func(arr):
    prefix_sum = [0]
    positions = {0: [0]}
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        prefix_sum.append(sum)
        if sum in positions:
            positions[sum].append(i)
        else:
            positions[sum] = [i]
    
    ans = []
    for i in positions:
        if len(positions[i]) >= 2:
            comb = combinations(positions[i], 2)
            ans += list(comb)
    return ans
        
    
arr = list(map(int, input().split()))
ans = func(arr)
for i in ans:
    if i[0] != 0:
        print(i[0]+1, i[1])
    else:
        print(0, i[1])


