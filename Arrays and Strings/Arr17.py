# Pradnyesh Choudhari
# Wed Jun  2 01:52:47 2021
# Balanced Sub-array problem. 
# Time Complexity O(n) Space Complexity O(n).

def func(arr):
    sum = 0
    ans = 0
    count = {0: -1}
    for i in range(len(arr)):
        item = arr[i]
        if item == 0:
            sum+=1
        else:
            sum-=1
        if sum in count:
            ans = max(ans, i-count.get(sum))
        else:
            count[sum] = i
    return ans
    
arr = list(map(int, input().split()))
print(func(arr))
    


