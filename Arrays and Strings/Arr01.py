# Pradnyesh Choudhari
# Fri May 28 21:41:45 2021
# Finding Majority Element more than n//2, n//3 times.
# Constraints Time O(n) and space O(1).

def func(n, arr):
    element1 = arr[0]
    ec1 = 1
    
    element2 = 0
    ec2 = 0
    
    # Finding both the elements occuring max times.
    for i in range(n):
        if element1 == arr[i]:
            ec1 += 1
        elif element2 == arr[i]:
            ec2 += 1
        elif ec1 == 0:
            element1 = arr[i]
            ec1 = 1
        elif ec2 == 0:
            element2 = arr[i]
            ec1 = 1
        else:
            ec1 -= 1
            ec2 -= 1
    
    ec1 = 0 
    ec2 = 0
    
    # Checking exactly how many times the elements occur.
    for i in range(n):
        if arr[i] == element1:
            ec1 += 1
        elif arr[i] == element2:
            ec2 += 1
   
    ans = []
    if ec1 > n//3:
        ans.append(element1)
    if ec2 > n//3:
        ans.append(element2)
    
    return ans
            
# Approach 1
# Constraints Time O(n) and space O(n).
# Using Dictionary

from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
count = Counter(arr)
for key, value in count.items():
    if value > (n//3): # Similarly for n//2
        print(key, end = " ")
        
# Approach 2
# Constraints Time O(n) and space O(1).
# For greater than n//2 times we can only have one element and for n//3 times
# when can only have maximum 2 elements.
 
ans = func(n, arr)
if len(ans) == 0:
    print("No majority element!")
else:
    print()
    print("Answer using approach2")
    print(*ans)
